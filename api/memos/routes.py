from django.urls import path, re_path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'', views.MemoViewSet, base_name="memos")

urlpatterns = [
    path(r'', views.MemoListCreateAPIView.as_view(), name = 'memo-listcreate'),
    re_path(r'^(?P<pk>\d+)/$', views.MemoRetrieveUpdateAPIView.as_view(), name = 'memo-retrieveupdate'),
    path(r'comments/', views.CommentCreateUpdateAPIView.as_view(), name = 'comment-createudate'),
]

urlpatterns += router.urls


