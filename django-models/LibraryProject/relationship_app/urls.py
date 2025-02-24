from django.urls import path
from .views import list_books, LibraryDetailView, UserCreationForm, login

urlpatterns = [
    path("",views.list_books, name="list_books"),
    path("",views.library_detail, name="library_detail"),
    path("",views.register, name="login"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name=")

]
