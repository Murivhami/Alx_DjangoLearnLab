from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
  path('api/books/', BookListView.as_view(), name = 'book_list_view'),
  path('api/books/<int:pk>/', BookDetailView.as_view(), name = 'book_detail_view'),
  path('api/books/create/', BookCreateView.as_view(), name = 'book_create_view'),
  path('api/books/update/', BookUpdateView.as_view(), name = 'book_update_view'),
  path('api/books/delete/', BookDeleteView.as_view(), name = 'book_delete_view'),
]
