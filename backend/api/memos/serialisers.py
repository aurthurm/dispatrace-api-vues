from rest_framework import serializers
from apps.memos.models import Memo, MemoComment
from api.cross_serialisers import UserSerializer
from django.contrib.auth.models import User

class MemoCommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(many=False)
    class Meta:
        model = MemoComment
        fields = ['id', 'comment', 'commenter', 'timestamp']
        read_only_fields = ['id', 'commenter']


class MemoSerializer(serializers.ModelSerializer):
    to = UserSerializer(many=False)
    sender = UserSerializer(many=False)
    recipients = UserSerializer(many=True)
    receptors = UserSerializer(many=True)
    url = serializers.SerializerMethodField(read_only=True)
    memocomment_comment = MemoCommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Memo
        fields = [            
            'url',
            'id',
            'recipients',
            'to',
            'sender',
            'is_open',
            'archived',
            'sent',
            'created',
            'date_sent',
            'reference_number',
            'subject',
            'slug',
            'message',
            'accesibility',
            'mem_priority',
            'commenting_required',
            'memocomment_comment',
            'comment_count',
            'receptors',
        ]
        read_only_fields = ['id', 'sender', 'slug', 'created', 'date_sent', 'comment_count']
        depth = 2

    def get_url(self, obj):
        return obj.get_api_url()

    def get_comment_count(self, obj):
        return obj.memocomment_comment.all().count()