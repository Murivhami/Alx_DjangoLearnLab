from bookshelf.models import Book

book = Book.object.delete(author = 'George Orwell')
book.save()

Book.objects.get()
