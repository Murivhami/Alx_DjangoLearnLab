from django.db import models
from django.contrib.auth.models import User, UserProfile

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
     class Meta:
         permissions = [
             ("can_add_book", "Can add book"),
             ("can_change_book", "Can change book"),
             ("can_delete_book", "Can delete book"),
             

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    

def __str__(self):
    return self.name

#Role based views
    class UserProfile(models.Model):
        ROLES=(
            ('admin', 'Admin'),
            ('librarian', 'Librarian'),
            ('member', 'Member'),

    role = models.CharField(max_length=12, choices=ROLES, default='member')


    

