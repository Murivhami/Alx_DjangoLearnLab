from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    book_details = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"<pre>{book_details}</pre>")

