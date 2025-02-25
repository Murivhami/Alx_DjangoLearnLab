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

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Admin View
@login_required
def admin_view(request):
    if request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'admin_view.html')

# Librarian View
@login_required
def librarian_view(request):
    if request.user.userprofile.role != 'Librarian':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'librarian_view.html')

# Member View
@login_required
def member_view(request):
    if request.user.userprofile.role != 'Member':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'member_view.html')
