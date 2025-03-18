from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list_view'),  # Remove the leading 'api/'
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path('books/create/', BookCreateView.as_view(), name='book_create_view'),
    path('books/update/', BookUpdateView.as_view(), name='book_update_view'),
    path('books/delete/', BookDeleteView.as_view(), name='book_delete_view'),
]
