from bookshelf.models import Book

books = Book.objects.get('1984')
books.save()
