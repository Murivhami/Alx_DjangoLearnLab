from django.http import HttpResponse
from .models import Book

def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    
    # Create a simple text response with book titles and authors
    book_details = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    
    # Return the text as the HttpResponse
    return HttpResponse(f"<pre>{book_details}</pre>")
