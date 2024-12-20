from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import SignupView, LoginView, UserListCreateView, UserDetailView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('users', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
]
