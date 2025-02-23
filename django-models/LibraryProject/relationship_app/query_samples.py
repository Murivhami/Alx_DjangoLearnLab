from django.db import models
books_by_author = Books.object.filter(author = 'John')

books = Library.object.all()

librar = Librarian.objects.get('librar')
