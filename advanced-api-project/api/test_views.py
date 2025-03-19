from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book

class BookAPITestCase(APITestCase):
    def test_create_book(self):
       data = {'title':'Test Book', 'author': 'John Doe', 'publication_year':2022}
       response = self.client.post('/api/books/', data)
       self.assertEqual(response
