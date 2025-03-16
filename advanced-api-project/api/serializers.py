from rest_framework import serializers
from .models import Author, Book

#Manage data conversion, validationa and representation for the models.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

#An author can have many books, but a book can only belong to one author. 

        def validate_publication_year(self, value):
            current_year = datetime.now().year
            if value > current_year:
                raise serializers.ValidationError(f'Publication year cannot be in the future')
            return value
