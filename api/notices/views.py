from apps.notices.models import Notice, Category
from apps.accounts.models import City, Office, Department
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serialisers import *
from django.utils import timezone
from datetime import timedelta


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(creator=self.request.user)


class NoticeList(generics.ListAPIView):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        notices = Notice.objects.all()
        yesterday = timezone.now() - timedelta(days=1)
        notices = notices.filter(expiry__gt=yesterday)
        return notices


class CategoryCRUView(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(creator=self.request.user)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title', None)
        category = None
        if title:
            category = Category.objects.create(
                title = title,
                creator = self.request.user,
                created = timezone.now()
            )
            category.save()
        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        category_id = request.data.get('id', None)
        category_title = request.data.get('title', None)
        category = Category.objects.get(pk=category_id)
        category.title = category_title
        category.save()
        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(creator=self.request.user)

    def delete(self, request, *args, **kwargs):
        category_id = int(self.kwargs.get('pk'))
        category = Category.objects.get(pk=category_id)
        if category:
            category.delete()
        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class NoticeCUViewView(mixins.UpdateModelMixin, generics.CreateAPIView):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all()
    
    def post(self, request, *args, **kwargs):
        data = request.data.get('notice_data')

        category_id  = data.get('category').get('value', None)
        category = None
        if category_id:
            category = get_object_or_404(Category, pk=category_id)

        city_id  = data.get('city').get('value', None)
        city = None
        if city_id:
            city = get_object_or_404(City, pk=city_id)

        office_id  = data.get('office').get('value', None)
        office = None
        if office_id:
            office = get_object_or_404(Office, pk=office_id)

        department_id =data.get('department').get('value', None)
        department = None
        if department_id:
            department = get_object_or_404(Department, pk=department_id)

        if category:
            notice = Notice.objects.create(
                category = category,
                city = city,
                office = office,
                department = department,
                title = data.get('title', None),
                description = data.get('description', None),
                creator = self.request.user,
                expiry  = timezone.now() + timedelta(days=3)
            )
            notice.save()

        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        data = request.data.get('notice_data')
        notice_id = data.get('id', None)
        notice = None
        if notice_id:
            notice = get_object_or_404(Notice, pk=notice_id)

        category_id  = data.get('category').get('value', None)
        category = None
        if category_id:
            category = get_object_or_404(Category, pk=category_id)

        city_id  = data.get('city').get('value', None)
        city = None
        if city_id:
            city = get_object_or_404(City, pk=city_id)

        office_id  = data.get('office').get('value', None)
        office = None
        if office_id:
            office = get_object_or_404(Office, pk=office_id)

        department_id =data.get('department').get('value', None)
        department = None
        if department_id:
            department = get_object_or_404(Department, pk=department_id)

        print(f"Notice id: {notice_id}    :: notice {notice}")
        if notice:            
            notice.category = category
            notice.city = city
            notice.office = office
            notice.department = department
            notice.title = data.get('title', None)
            notice.description = data.get('description', None)
            notice.creator = self.request.user
            notice.expiry  = timezone.now() + timedelta(days=3)
            notice.save()

        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class NoticeDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all()

    def delete(self, request, *args, **kwargs):
        notice_id = int(self.kwargs.get('pk'))
        notice = Notice.objects.get(pk=notice_id)
        if notice:
            notice.delete()
        categories = Category.objects.filter(creator=self.request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)