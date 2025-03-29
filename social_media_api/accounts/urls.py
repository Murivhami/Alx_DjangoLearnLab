from django.urls import path
from accounts.views import UserRegistrationView, LoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
]