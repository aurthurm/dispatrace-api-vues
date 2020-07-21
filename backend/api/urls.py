from django.urls import path, include
import api.accounts.routes, api.notices.routes, api.memos.routes

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import ExtraTokenObtainPairView, get_user_data

app_name = 'api'
urlpatterns = [
    path('accounts/', include(api.accounts.routes)),
    path('notices/', include(api.notices.routes)),
    path('memos/', include(api.memos.routes)),
    # JWT AUTHENTICATION
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/extras/', ExtraTokenObtainPairView.as_view(), name="token-extras"), # MODIFIED
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', get_user_data, name='user'),
]