from django.db import models
from django.contrib.auth.models import User, UserProfile

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    ROLE = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]

    role = models.CharField(max_length=10, choices=ROLE, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    

def __str__(self):
    return self.name
