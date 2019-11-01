from django.contrib.auth.models import Group

from rest_framework import serializers
from apps.accounts.models import *
from api.cross_serialisers import UserSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AccountProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = CitySerializer()
    department = DepartmentSerializer()
    office = OfficeSerializer()
    level = LevelSerializer()
    groups = GroupSerializer(many=True)
    
    class Meta:
        model = AccountProfile
        fields = '__all__'

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    refresh = serializers.CharField(max_length=255)
    access = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()
    groups = serializers.ListField()