
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'', views.AccountProfileViewSet, base_name="accounts")

urlpatterns = [    
    path(r'', views.AccountProfileAPIView.as_view(), name="account-profile"),
    re_path(r'^(?P<pk>\d+)/$', views.AccountProfileUpdateRetrieveAPIView.as_view(), name="account-retrieveupdate"),
    path(r'signup/', views.UserCreateAPIView.as_view(), name = 'signup'),
    path(r'signin/', views.LoginCreateAPIView.as_view(), name = 'signin'),
    path(r'cities/', views.CityAPIView.as_view(), name = 'cities'),
    path(r'offices/', views.OfficeAPIView.as_view(), name = 'offices'),
    path(r'departments/', views.DepartmentAPIView.as_view(), name = 'departments'),
    path(r'levels/', views.LevelAPIView.as_view(), name = 'levels'),
    path(r'groups/', views.GroupAPIView.as_view(), name = 'groups'),
]

urlpatterns += router.urls