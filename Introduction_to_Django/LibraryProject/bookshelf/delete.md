from bookshelf.models import Book

book = Book.objects.delete(author = 'George Orwell')
book.save()

Book.objects.get()
