from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name='John Doe')
#test case for creating books
    def test_create_book(self):
        author = Author.objects.create(name='John Doe')
        data = {'title':'Test Book','publication_year': 2022, 'author': author.id, }
        response = self.client.post('/api/books/create/', data, format= 'json')
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Test Book')


#test case for retrieving
    def test_get_book(self):
        author = Author.objects.create(name='John Doe')
        book = Book.objects.create(title='Test Book',publication_year=2022, author=author)
        response = self.client.get('/api/books/', format= 'json')
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book_data['title']== 'Test Book'for book_data in response.data))
       # data = {'author': 'John Doe'}
        #response = self.client.post('/api/books/', data, format= 'json')
        #self.assertEqual(response.status_code, 400)
        #self.assertEqual('title', response.data)

#test case for updating
    def test_update_book(self):
       author = Author.objects.create(name='John Doe')
       book = Book.objects.create(title='Test Book', publication_year=2022, author=author)
       print('Original book data:', Book.objects.values())

       updated_data = {
        'title': 'Updated Test Book',
        'publication_year': 2023,
        'author': author.id
}
       response = self.client.put(f'/api/books/update/{book.id}/', updated_data, format='json')
       print("Response Status Code:", response.status_code)
       print("Response Data:", response.data)

    
       self.assertEqual(response.status_code, status.HTTP_200_OK)

   
       self.assertEqual(response.data['title'], updated_data['title'])
       self.assertEqual(response.data['publication_year'], updated_data['publication_year'])

    
       print('Updated book data:', Book.objects.values())

# Deleting test case
    def test_delete_book(self):
        author = Author.objects.create(name= 'Tshedza')
        book = Book.objects.create(title='Test Book', publication_year=2022, author=author)

        print('Book in database:', Book.objects.all())
        response = self.client.delete(f'/api/books/delete/{book.id}/', format='json')
    
    
        print("Response Status Code:", response.status_code)

    
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
        remaining_books = Book.objects.filter(id=book.id)
        self.assertEqual(remaining_books.count(), 0)


        print('Books in database after deletion:', Book.objects.all())



    
    