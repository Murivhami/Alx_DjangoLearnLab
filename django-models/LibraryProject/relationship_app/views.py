from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login


class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role-checking functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'

# Views with role-based access control
@user_passes_test(is_admin, login_url='/403/')
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/403/')
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/403/')
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html')

    
