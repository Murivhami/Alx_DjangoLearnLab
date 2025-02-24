from django.urls import path
from .views import list_books, LibraryDetailView, login

urlpatterns = [
    path("",views.list_books, name="list_books"),
    path("",views.library_detail, name="library_detail"),
    path("",views.login, name="login"),
]
