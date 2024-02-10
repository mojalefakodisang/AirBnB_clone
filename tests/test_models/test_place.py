#!/usr/bin/python3
"""Module that tests Place model"""
import os
import time
import datetime
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class that tests for Place model

    Args:
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "Place.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_Place_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.place').__doc__
        class_doc = __import__('models.place').place.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_Place_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        Place1 = Place()
        time.sleep(1)
        Place2 = Place()

        """Checking if the instances are not the same"""
        self.assertNotEqual(Place1.id, Place2.id)
        self.assertNotEqual(Place1.created_at, Place2.created_at)
        self.assertNotEqual(Place1.updated_at, Place2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(Place1.id, str)
        self.assertIsInstance(Place1.created_at, datetime.datetime)
        self.assertIsInstance(Place1.updated_at, datetime.datetime)

    def test_Place_initialization_argument(self):
        """Testing initialization with arguments"""
        Place1 = Place()
        Place2 = Place(**Place1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(Place1.id, Place2.id)
        self.assertEqual(Place1.updated_at, Place2.updated_at)
        self.assertEqual(Place1.created_at, Place2.created_at)

    def test_Place_str_method(self):
        """Testing Place str method"""
        Place1 = Place()

        self.assertTrue(str(Place1).startswith("[Place]"))

        self.assertIn(Place1.id, str(Place1))
        self.assertIn("created_at", str(Place1))
        self.assertIn("updated_at", str(Place1))

    def test_Place_to_dict_method(self):
        """Testing Place to_dict method"""
        Place1 = Place()

        my_dict = Place1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing Place for save method"""
        Place1 = Place()
        Place2 = Place(**Place1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(Place1.created_at, Place2.created_at)
        self.assertEqual(Place1.updated_at, Place2.updated_at)
        self.assertEqual(Place1.created_at, Place1.updated_at)
        self.assertEqual(Place2.created_at, Place2.updated_at)

        time.sleep(1)
        Place1.save()
        Place2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(Place1.created_at, Place1.updated_at)
        self.assertNotEqual(Place2.created_at, Place2.updated_at)


if __name__ == "__main__":
    unittest.main()
