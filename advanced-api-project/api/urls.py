from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlspatterns = [
  path('api/books/', views.BookListView.as_view(), name = 'book_list_view'),
  path('books/<int:pk>/', views.BookDetailView.as_view(), name = 'book_detail_view'),
  path('api/books/', views.BookListView.as_view(), name = 'book_list_view'),
  path('api/books/', views.BookListView.as_view(), name = 'book_list_view'),
 
  
