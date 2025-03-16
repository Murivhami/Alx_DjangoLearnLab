from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def__str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name=books)


    def__str_(self):
        return self.title



    def__str__(self):
        return self.title
# Create your models here.
