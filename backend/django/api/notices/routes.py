
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'', views.NoticeViewSet, base_name="notice")

urlpatterns = [
     path('', views.NoticeList.as_view(), name='notices-list'),
     path('categories/', views.CategoryList.as_view(), name='categories'),
     path('category/', views.CategoryCRUView.as_view(), name='category'),
     re_path('category/(?P<pk>\d+)/$', views.CategoryDeleteView.as_view(), name='category-delete'),
     path('notice/', views.NoticeCUViewView.as_view(), name='notice-cu'),
     re_path('notice/(?P<pk>\d+)/$', views.NoticeDeleteView.as_view(), name='notice-delete'),
]

urlpatterns += router.urls