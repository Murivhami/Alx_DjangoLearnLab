from bookshelf.models import Book

book = Book.objects.get('1984')
book.delete = '1984'
book.save()

Book.objects.get()
