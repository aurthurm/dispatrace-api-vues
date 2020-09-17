from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serialisers import *
from api.cross_serialisers import UserSerializer
from apps.accounts.models import *

User = get_user_model()

class AccountProfileAPIView(generics.ListAPIView):
    serializer_class = AccountProfileSerializer

    def get_queryset(self):        
        queryset = AccountProfile.objects.exclude(user__username__iexact='dispatrace')
        queryset = queryset.exclude(user__username__iexact='AnonymousUser')
        return queryset

class AccountProfileUpdateRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = AccountProfile.objects.all()
    serializer_class = AccountProfileSerializer

    def get(self, request, *args, **kwargs):
        profile_id = self.kwargs.get('pk', None)
        profile = get_object_or_404(AccountProfile, pk=profile_id)
        serializer = AccountProfileSerializer(profile)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        update = request.data.get('account_data')
        user.first_name = update.get('firstname', user.first_name)
        user.last_name = update.get('lastname', user.last_name)
        user.email = update.get('email', user.email)
        user.save()
        instance.city = get_object_or_404(City, pk=int(update.get('city').get('id', instance.city.id if instance.city != None else None)))
        instance.office = get_object_or_404(Office, pk=int(update.get('office').get('id', instance.office.id if instance.office != None else None))) 
        instance.department = get_object_or_404(Department, pk=int(update.get('department').get('id', instance.department.id if instance.department != None else None))) 
        instance.level = get_object_or_404(Level, pk=int(update.get('level').get('id', instance.level.id if instance.level != None else None))) 
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
        country_id = self.request.GET.get('country', None)
        queryset = City.objects.all()
        if country_id:
            country = get_object_or_404(Country, pk=country_id)
            queryset = queryset.filter(country=country)
        return queryset

class OfficeAPIView(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):  
        city_id = self.request.GET.get('city', None)
        queryset = None
        if city_id != 'null':  
            city = get_object_or_404(City, pk=int(city_id))
            queryset = city.offices
        return queryset

class DepartmentAPIView(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):        
        office_id = self.request.GET.get('office', None)  
        queryset = None
        if office_id != 'null':
            office = get_object_or_404(Office, pk=int(office_id))
            queryset = office.departments
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

class PasswordReset(APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data.get('user_data', None)
        password1 = data.get('password1', None)
        password2 = data.get('password2', None)
        username = data.get('username', None)
        user_id = data.get('user_id', None)
        user = None
        if username and user_id and password1 == password2:
            user = User.objects.get(username__exact=username, pk=user_id)

        if user:
            user.set_password(password1)
            user.save()
            profile = user.accountprofile_user
            profile.force_password_change = False
            profile.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)


class CountrySettingsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        country_name = request.data.get('country', None)
        if country_name:
            country, created = Country.objects.get_or_create(
                name = country_name
            )
            if created:
                country.save()
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        country_name = request.data.get('country', None)
        country_id = request.data.get('id', None)
        if country_name and country_id:
            country = Country.objects.get(pk=country_id)
            country.name = country_name
            country.save()
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

class CountryDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  CountrySerializer

    def get_queryset(self):
        return Country.objects.all()

    def delete(self, request, *args, **kwargs):
        country_id = self.kwargs.get('pk')
        country = Country.objects.get(pk=country_id)
        if country:
            country.delete()
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

class CitySettingsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        country_id = request.data.get('country', None)
        abbr = request.data.get('abbreviation', None)
        city_name = request.data.get('city', None)
        office_ids = request.data.get('offices', None)
        if country_id and abbr and city_name:
            country = get_object_or_404(Country, pk=country_id)
            if country:
                city, created = City.objects.get_or_create(
                    country = country,
                    name = city_name,
                    abbreviation = abbr
                )
                if created:
                    city.save()

                    # add new selected offices
                    if office_ids:
                        for office_id in office_ids:
                            if office_id != None:
                                office = Office.objects.get(pk=int(office_id))
                                if not office in city.offices.all():
                                    city.offices.add(office)

        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        country_id = request.data.get('country', None)
        abbr = request.data.get('abbreviation', None)
        city_name = request.data.get('city', None)
        city_id = request.data.get('id', None)
        office_ids = request.data.get('offices', None)
        if country_id and city_id and abbr and city_name:
            city = get_object_or_404(City, pk=city_id)
            country = get_object_or_404(Country, pk=country_id)
            if city and country:
                city.country = country
                city.name = city_name
                city.abbreviation = abbr
                city.save()

                if office_ids:
                    for _off in city.offices.all():
                        city.offices.remove(_off)

                    for office_id in office_ids:
                        if office_id != None:
                            office = Office.objects.get(pk=int(office_id))
                            if not office in city.offices.all():
                                city.offices.add(office)

        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)


class CityDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  CitySerializer

    def get_queryset(self):
        return City.objects.all()

    def delete(self, request, *args, **kwargs):
        city_id = self.kwargs.get('pk')
        city = City.objects.get(pk=city_id)
        if city:
            city.delete()
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

class OfficeSettingsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Office.objects.all()
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        country_id = request.data.get('country', None)
        city_id = request.data.get('city', None)
        office_name = request.data.get('branch', None)
        abbr = request.data.get('abbreviation', None)
        department_ids = request.data.get('departments', None)
        if country_id and city_id and office_name and abbr:
            country = get_object_or_404(Country, pk=country_id)
        if city_id:
            city = get_object_or_404(City, pk=city_id)
        if country and city:
                office, created = Office.objects.get_or_create(
                    country = country,
                    name = office_name,
                    abbreviation = abbr
                )
                if created:
                    office.save()
                    city.offices.add(office)
                    city.save()

                    # add new selected offices
                    if department_ids:
                        for dept_id in department_ids:
                            if dept_id != None:
                                department = Department.objects.get(pk=int(dept_id))
                                if not department in office.departments.all():
                                    office.departments.add(department)

        queryset = Office.objects.all()
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        country_id = request.data.get('country', None)
        city_id = request.data.get('city', None)
        office_id = request.data.get('id', None)
        office_name = request.data.get('branch', None)
        abbr = request.data.get('abbreviation', None)
        department_ids = request.data.get('departments', None)
        if country_id and city_id and office_id and abbr and office_name:
            city = get_object_or_404(City, pk=city_id)
            country = get_object_or_404(Country, pk=country_id)
            office = get_object_or_404(Office, pk=office_id)
            if city and country and office:
                office.country = country
                office.name = office_name
                office.abbreviation = abbr
                office.save()
                if not office in city.offices.all():
                    city.offices.add(office)
                    city.save()

                if department_ids:
                    for _dept in office.departments.all():
                        office.departments.remove(_dept)

                    for dept_id in department_ids:
                        if dept_id != None:
                            department = Department.objects.get(pk=int(dept_id))
                            if not department in office.departments.all():
                                office.departments.add(department)

        queryset = Office.objects.all()
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

class OfficeDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  OfficeSerializer

    def get_queryset(self):
        return Office.objects.all()

    def delete(self, request, *args, **kwargs):
        office_id = self.kwargs.get('pk')
        office = Office.objects.get(pk=office_id)
        if office:
            office.delete()
        queryset = Office.objects.all()
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

class DepartmentSettingsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        department_name = request.data.get('department', None)
        abbr = request.data.get('abbreviation', None)
        if department_name and abbr:
            department, created = Department.objects.get_or_create(
                name = department_name,
                abbreviation = abbr
            )
            if created:
                department.save()

        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        department_id = request.data.get('id', None)
        department_name = request.data.get('department', None)
        abbr = request.data.get('abbreviation', None)
        if department_id and department_name and abbr:
            department = get_object_or_404(Department, pk=department_id)
            if department:
                department.name = department_name
                department.abbreviation = abbr
                department.save()

        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

class DepartmentDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  DepartmentSerializer

    def get_queryset(self):
        return Department.objects.all()

    def delete(self, request, *args, **kwargs):
        department_id = self.kwargs.get('pk')
        department = Department.objects.get(pk=department_id)
        if department:
            department.delete()
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

class LevelSettingsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        name = request.data.get('levelname', None)
        _level = request.data.get('level', None)
        if name and _level:
            level, created = Level.objects.get_or_create(
                name = name,
                level = _level
            )
            if created:
                level.save()

        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        level_id = request.data.get('id', None)
        name = request.data.get('levelname', None)
        _level = request.data.get('level', None)
        if level_id and name and _level:
            level = get_object_or_404(Level, pk=level_id)
            if level:
                level.name = name
                level.level = _level
                level.save()

        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)

class LevelDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  LevelSerializer

    def get_queryset(self):
        return Level.objects.all()

    def delete(self, request, *args, **kwargs):
        level_id = self.kwargs.get('pk')
        level = Level.objects.get(pk=level_id)
        if level:
            level.delete()
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)