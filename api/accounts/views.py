from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions
from rest_framework.response import Response

from .serialisers import *
from api.cross_serialisers import UserSerializer
from apps.accounts.models import *

User = get_user_model()

class AccountProfileAPIView(generics.ListAPIView):
    serializer_class = AccountProfileSerializer

    def get_queryset(self):        
        queryset = AccountProfile.objects.exclude(user__username__iexact='dispatrace')
        return queryset

class AccountProfileUpdateRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = AccountProfile.objects.all()
    serializer_class = AccountProfileSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        update = request.data.get('account_data')
        user.first_name = update.get('firstname', user.first_name)
        user.last_name = update.get('lastname', user.last_name)
        user.email = update.get('email', user.email)
        user.save()
        instance.city = get_object_or_404(City, pk=int(update.get('city').get('id', instance.city.id)))
        instance.office = get_object_or_404(Office, pk=int(update.get('office').get('id', instance.office.id))) 
        instance.department = get_object_or_404(Department, pk=int(update.get('department').get('id', instance.department.id))) 
        instance.level = get_object_or_404(Level, pk=int(update.get('level').get('id', instance.level.id))) 
        instance.title = update.get('title', instance.title)
        instance.save()

        group_objects = update.get('groups', None)
        group_ids = [group_id.get('id') for group_id in group_objects]

        # add new selected groups if not already in instance.groups
        if group_ids:
            for group_id in group_ids:
                group = Group.objects.get(pk=int(group_id))
                if not group in instance.groups.all():
                    instance.groups.add(group)

        # Remove groups that were unselected
        for group in instance.groups.all():
            if not group.id in group_ids:
                instance.groups.remove(group)
        
        # reset user groups
        for group in user.groups.all():
            user.groups.remove(group)   
          
        # re add user groups to match exactly those in instance.groups
        for group in instance.groups.all():
            user.groups.add(group)
            
        serializer = AccountProfileSerializer(instance)
        return Response(serializer.data)


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        firstname = request.data.get('firstname')
        lastname = request.data.get('lastname')
        email = request.data.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = None
        if password == password2:
            user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken

class LoginCreateAPIView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            data = {}
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            data['username'] = user.username
            data['user_id'] = user.pk
            data['groups'] = user.groups.values_list('name', flat=True)
            serializer = TokenSerializer(data=data)
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class CityAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):        
        queryset = City.objects.all()
        return queryset

class OfficeAPIView(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):  
        city_id = self.request.GET.get('city', None)  
        city = get_object_or_404(City, pk=int(city_id))
        queryset = city.offices
        return queryset

class DepartmentAPIView(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):        
        office_id = self.request.GET.get('office', None)  
        city = get_object_or_404(Office, pk=int(office_id))
        queryset = city.departments
        return queryset

class LevelAPIView(generics.ListAPIView):
    serializer_class = LevelSerializer

    def get_queryset(self):        
        queryset = Level.objects.exclude(level__exact=0)
        return queryset

class GroupAPIView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):        
        queryset = Group.objects.all()
        return queryset