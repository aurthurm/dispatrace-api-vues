
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'', views.NoticeViewSet, base_name="notice")

urlpatterns = [
     path('', views.NoticeList.as_view(), name='all-notices'),
]

urlpatterns += router.urls