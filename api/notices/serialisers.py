from rest_framework import serializers
from apps.notices.models import Notice, Category


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    notice_categories = NoticeSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'