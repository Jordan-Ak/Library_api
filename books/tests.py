from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from datetime import datetime

from . import models


# Create your tests here.
"""
class BookTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username = 'testuser',
                                                         email = 'test@email.com',
                                                         password = 'secret')
        self.author = models.Author.objects.create(name = 'Clementina')
        self.publisher = models.Publisher.objects.create(name = 'Macmillan')
        self.genre = models.Genre.objects.create(name = 'Fantasy')
        self.book = models.Book.objects.create(name = 'spur',
                                                publisher = self.publisher, pub_date = datetime.now(),
                                                price = 2,)
        self.borrowed = models.Borrowed.objects.create(name = self.book, has_returned = False,
                                                        who_borrowed = self.user,)
        self.rating = models.Rating.objects.create(who_rated = self.user, book_rated = self.book,
                                                  rating = 3,)
        #self.quantity_book = models.Quantity_Book.objects.create(book = self.book, total_qty = 4,)
        #self.quantity_borrowed = models.Quantity_Borrowed.objects.create(who = self.user)


    def test_content(self):
        self.assertEqual(f'{self.author}','Lewis')
        self.assertEqual(f'{self.genre}','Fantasy')
        self.assertEqual(f'{self.publisher}','Publife')

"""