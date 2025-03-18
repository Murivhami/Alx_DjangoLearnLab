from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DeleteView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
