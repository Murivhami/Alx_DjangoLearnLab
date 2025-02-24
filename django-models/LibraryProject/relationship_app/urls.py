from django.urls import path
from .views import list_books, LibraryDetailView, UserCreationForm, login
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

urlpatterns = [
    path("",views.list_books, name="list_books"),
    path("",views.library_detail, name="library_detail"),
    path("",views.register, name="login"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
                                       
    

]
