from typing import Any
from django.test import TestCase
import factory
from django.core.exceptions import ValidationError
from .factories import CategoryFactory, ProductFactory, UserFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status



class CategoryTest(TestCase):

    def test_get_three_last_parent(self):
        top_category = CategoryFactory(name='laptop')
        second_category = CategoryFactory(parent=top_category)
        third_category = CategoryFactory(parent=second_category)
        fourth_category = CategoryFactory(parent=third_category)
        fifth_category = CategoryFactory(parent=fourth_category)

        parents = fifth_category.get_three_last_parent()
        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[0], fifth_category)
        self.assertEqual(parents[1], fourth_category)
        self.assertEqual(parents[2], third_category)


    def test_get_three_last_parent_less_than_three_parents(self):
        top_category = CategoryFactory()
        second_category = CategoryFactory(parent=top_category)
        third_category = CategoryFactory(parent=second_category)

        parents = third_category.get_three_last_parent()
        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[1], second_category)
        self.assertEqual(parents[2], top_category)

    def test_get_three_last_parent_no_parent(self):
        category = CategoryFactory()
        parents = category.get_three_last_parent()
        self.assertEqual(len(parents), 1)



class SignUpViewSetTest(APITestCase):
    def setUp(self):
        user = UserFactory()

    
    def test_signup_user(self):
        url = reverse('signup-list')
        data = {
            'username': 'testusername',
            'password': 'testpassword',
            'email': 'admin@gmail.com',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)