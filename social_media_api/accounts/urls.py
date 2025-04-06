from django.urls import path
from .views import UserRegistrationView, LoginView, FollowUser, UnfollowUser
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('follow/<int:user_id>/', FollowUser.as_view(), name='FollowUser'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='UnfollowUser'),
]
