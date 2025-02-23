from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import TemplateView
from .models import Library

class DetailView(TemplateView):
    template_name = 'library_detail.html'
