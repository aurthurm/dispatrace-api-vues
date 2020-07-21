from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q, F
from django.utils import timezone

from apps.memos.models import Memo, PUBLIC, PRIVATE, V_URGENT, MODERATE, NORMAL
from .serialisers import *
from api.utils import get_ref_number
from .permissions import *


class MemoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MemoSerializer

    def get_queryset(self):
        queryset = Memo.objects.all()
        look_up_value, memo_state = self.request.GET.get('q', None), self.request.GET.get('mstate', None)
        if look_up_value is not None:
            queryset = queryset.filter(
						Q(reference_number__icontains=look_up_value) | 
						Q(subject__icontains=look_up_value) |
						Q(message__icontains=look_up_value)
                        )
        elif memo_state is not None:
            request_user_id = self.request.user.id
            request_user = self.request.user
            request_user_username = request_user.username
            if memo_state == 'closed':
                """
                Display a Archived memos where request user is either adressed to or cc.
                Why see memos that didnt concern you from inception :)
                """
                queryset = queryset.filter(
                        Q(is_open__exact=False) & Q(archived__exact=False),
                        Q(sender__exact=request_user) | Q(to__exact=self.request.user) | Q(recipients__username__contains=self.request.user.username)
                    ).distinct()
            elif memo_state == 'archived':
                """
                Display a Archived memos where request user is either adressed to or cc.
                Why see memos that didnt concern you from inception :)
                """
                queryset = queryset.filter(
                        Q(archived__exact=True),
                        Q(sender__exact=request_user) #Q(to__exact=self.request.user) | Q(recipients__username__contains=self.request.user.username)
                    ).distinct()
            elif memo_state == 'outgoing':
                """
                Display a Memo List defined by:
                1. Memos i created and still being reviewed by others but not archived yet.
                2. Memos i received and has already commented but still awaits commenting by next user.
                """
                queryset = queryset.filter(Q(archived__exact=False))
                queryset = queryset.filter(
                        Q(sender__exact=request_user) & Q(sent__exact=True) & Q(is_open__exact=True) |
                        Q(sent__exact=True) & Q(is_open__exact=True) & Q(recipients__username__contains=request_user_username) & Q(memocomment_comment__commenter__exact=request_user) | 
                        Q(is_open__exact=True) & Q(receptors__username__contains=request_user_username) 
                    ).distinct()
            elif memo_state == 'drafts':
                """
                Display a Memo List defined by:
                1. Memos i create but havent sent them yet.
                """
                queryset = queryset.filter(
                        Q(sent__exact=False) & Q(is_open__exact=True) & Q(sender__exact=request_user)
                    ).distinct()
            elif memo_state == 'incoming':	
                """
                Display a Memo List defined by:
                1. Memos i received but awaiting my commenting.
                2. If memo.to let memo remain in intray before close even after comenting
                """
                queryset = queryset.filter(
                        Q(sent__exact=True) & Q(is_open__exact=True) & ~Q(sender__exact=request_user), # ... and exclude those i created myself
                        Q(recipients__username__contains=request_user_username) & ~Q(memocomment_comment__commenter__exact=request_user) | #   if am recient exclude those i commented
                        Q(to__exact=request_user) 
                    ).distinct()
                queryset = queryset.filter(
                        ~Q(receptors__username__contains=request_user_username)
                    )                    
            else:
                pass
        else: # there are no look_ups or memo_state queries
            queryset = queryset.filter(sent__exact=True, archived__exact=False)
        return queryset

    def create(self, *args, **kwargs):   
        request_user_id = self.request.user.id
        request_user = self.request.user
        new_data = self.request.data.get('form_data')
        recipients = []
        for user_name in new_data.get('recipients', []).split(','): 
            user_name = user_name.strip()
            if len(user_name) != 0:
                recipients.append(get_object_or_404(User, username__exact=user_name.strip()))
        accesibility = new_data.get('accesibility', None)
        if accesibility == "Private":
            accesibility = PRIVATE
        else:
            accesibility = PUBLIC
        priority = new_data.get('priority', None)
        if priority == "Normal":
            priority = NORMAL
        elif priority == "Moderate":
            priority = MODERATE
        else:
            priority = V_URGENT
        commenting = new_data.get('commenting', True)
        if commenting == "Required":
            commenting = True
        else:
            commenting = False
        new_memo = Memo.objects.create(
            sender = request_user,
            to = get_object_or_404(User, username__exact=new_data.get('to', None)),
            is_open = True,
            archived = False,
            created = timezone.now(),
            reference_number = get_ref_number(user=request_user),
            subject = new_data.get('subject', None),
            message = new_data.get('content', None),
            accesibility = accesibility,
            mem_priority = priority,
            commenting_required = commenting,
        )        
        new_memo.recipients.set(recipients)
        new_memo.save()
        serializer = MemoSerializer(new_memo) 
        
        return Response({'data': serializer.data})
        

class MemoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def get(self, request, *args, **kwargs):
        memo_id = self.kwargs.get('pk', None)
        memo = get_object_or_404(Memo, pk=memo_id)
        serializer = MemoSerializer(memo)
        extra_context = {}
        if memo.is_open:
            extra_context['can_comment'] = can_comment(self.request.user, memo)
            comments = memo.memocomment_comment.all()
            if comments.count() != 0:
                can_edit_comm =  is_recent_commenter(self.request.user, memo)
                can_edit_memo = False
            else:
                can_edit_comm = False            
                can_edit_memo = True
            extra_context['has_commented'] = has_commented(self.request.user, memo)
            extra_context['can_edit_comment'] = can_edit_comm
            extra_context['can_close'] = can_close(self.request.user, memo)
            extra_context['can_edit_memo'] = can_edit_memo
        else:
            extra_context['can_comment'] = False
            extra_context['can_close'] = False
            extra_context['can_edit_comment'] = False
            extra_context['can_edit_memo'] = False

        return Response({'data': serializer.data, 'extras': extra_context })

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        send_memo = request.data.get('send')
        close_memo = request.data.get('close')
        if send_memo:
            instance.sent = True
            instance.save()
        elif close_memo:
            instance.is_open = False
            instance.save()
        else:
            update = request.data.get('memo_form')
            # Retrieve New Data
            to = get_object_or_404(User, username=update.get('to', None))
            recipients = []
            for user_name in update.get('recipients', []).split(','): 
                user_name = user_name.strip()
                if len(user_name) != 0:
                    recipients.append(get_object_or_404(User, username__exact=user_name.strip()))
            subject = update.get('subject', None)
            message = update.get('content', None)
            accesibility = update.get('accesibility', None)
            if accesibility == "Private":
                accesibility = PRIVATE
            else:
                accesibility = PUBLIC
            priority = update.get('priority', None)
            if priority == "Normal":
                priority = NORMAL
            elif priority == "Moderate":
                priority = MODERATE
            else:
                priority = V_URGENT
            commenting = update.get('commenting', True)
            if commenting == "Required":
                commenting = True
            else:
                commenting = False
            instance.to = to
            instance.recipients.set(recipients)
            instance.subject = subject
            instance.message = message
            instance.accesibility = accesibility
            instance.commenting_required = commenting
            instance.mem_priority = priority
            instance.save()

        serializer = MemoSerializer(instance)        

        return Response({'data': serializer.data})
        

class MemoCreateAPIView(generics.CreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def create(self, *args, **kwargs):
        request_user_id = self.request.user.id
        request_user = self.request.user
        new_data = self.request.data.get('form_data')
        recipients = []
        for user_name in new_data.get('recipients', []).split(','): 
            user_name = user_name.strip()
            if len(user_name) != 0:
                recipients.append(get_object_or_404(User, username__exact=user_name.strip()))
        accesibility = new_data.get('accesibility', None)
        if accesibility == "Private":
            accesibility = PRIVATE
        else:
            accesibility = PUBLIC
        priority = new_data.get('priority', None)
        if priority == "Normal":
            priority = NORMAL
        elif priority == "Moderate":
            priority = MODERATE
        else:
            priority = V_URGENT
        commenting = new_data.get('commenting', True)
        if commenting == "Required":
            commenting = True
        else:
            commenting = False
        new_memo = Memo.objects.create(
            sender = request_user,
            to = get_object_or_404(User, username__exact=new_data.get('to', None)),
            is_open = True,
            archived = False,
            created = timezone.now(),
            reference_number = get_ref_number(user=request_user),
            subject = new_data.get('subject', None),
            message = new_data.get('content', None),
            accesibility = accesibility,
            mem_priority = priority,
            commenting_required = commenting,
        )        
        new_memo.recipients.set(recipients)
        new_memo.save()
        serializer = MemoSerializer(new_memo) 
        
        return Response({'data': serializer.data})

class CommentCreateUpdateAPIView(mixins.UpdateModelMixin, generics.CreateAPIView):
    serializer_class = MemoCommentSerializer

    def post(self, request, *args, **kwargs):
        request_user = self.request.user
        request_data = self.request.data
        memo = get_object_or_404(Memo, pk=int(request_data.get('memo_id')))
        comment_text = request_data.get('comment')
        if memo and comment_text:
            comment = MemoComment.objects.create(
                memo = memo,
                comment = comment_text,
                timestamp = timezone.now(),
                commenter = request_user
            )
            comment.save()
        serializer = MemoSerializer(memo)
        return Response(serializer.data) 

    def put(self, request, *args, **kwargs):
        request_data = self.request.data
        memo = get_object_or_404(Memo, pk=int(request_data.get('memo_id')))
        comment = get_object_or_404(MemoComment, pk=int(request_data.get('comment_id')))
        comment_text = request_data.get('comment')
        if comment and comment_text:
            comment.comment = comment_text
            comment.comment = comment_text
            comment.save()
        serializer = MemoSerializer(memo)
        return Response(serializer.data) 