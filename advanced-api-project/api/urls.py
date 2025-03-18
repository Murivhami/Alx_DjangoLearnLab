from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlspatterns = [
  path('api/books/', views.BookListView.as_view(), name = 'book_list_view'),
  path('/books/<int:pk>/', views.BookDetailView.as_view(), name = 'book_detail_view'),
  path('/books/create/', views.BookCreateView.as_view(), name = 'book_create_view'),
  path('books/update/', views.BookUpdateView.as_view(), name = 'book_update_view'),
  path('books/delete/', views.BookUpdateView.as_view(), name = 'book_update_view'),
]
