from django.urls import path, include
from blog.views import RegisterView, LogoutView, LoginView

urlpatterns = [
    path('Register/', RegisterView.as_view(), name = 'register'),
    path('Logout/', LogoutView.as_view(), name = 'logout'),
    path('Login/', LoginView.as_view(), name = 'login'),
    path('accounts/', LogoutView.as_view(), name = 'accounts/profile/'),

]