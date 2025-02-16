from bookshelf.models import Book

Book.objects.filter(title = '1984').update(title = 'Nineteen Eighty-Four')
save()
