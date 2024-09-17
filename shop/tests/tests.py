from typing import Any
from django.test import TestCase
import factory
from django.core.exceptions import ValidationError
from .factories import CategoryFactory, ProductFactory

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




