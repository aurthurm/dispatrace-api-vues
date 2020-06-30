
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
    path(r'password-reset/', views.PasswordReset.as_view(), name = 'password-reset'),
    path(r'country-settings/', views.CountrySettingsView.as_view(), name = 'country-settings'),
    re_path(r'country-settings/(?P<pk>\d+)/$', views.CountryDeleteView.as_view(), name = 'country-delete'),
    path(r'city-settings/', views.CitySettingsView.as_view(), name = 'city-settings'),
    re_path(r'city-settings/(?P<pk>\d+)/$', views.CityDeleteView.as_view(), name = 'city-delete'),
    path(r'office-settings/', views.OfficeSettingsView.as_view(), name = 'office-settings'),
    re_path(r'office-settings/(?P<pk>\d+)/$', views.OfficeDeleteView.as_view(), name = 'office-delete'),
    path(r'department-settings/', views.DepartmentSettingsView.as_view(), name = 'department-settings'),
    re_path(r'department-settings/(?P<pk>\d+)/$', views.DepartmentDeleteView.as_view(), name = 'department-delete'),
    path(r'level-settings/', views.LevelSettingsView.as_view(), name = 'level-settings'),
    re_path(r'level-settings/(?P<pk>\d+)/$', views.LevelDeleteView.as_view(), name = 'level-delete'),
]

urlpatterns += router.urls
