from apps.notices.models import Notice, Category
from rest_framework import generics, viewsets
from .serialisers import *

class NoticeList(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class Category(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer