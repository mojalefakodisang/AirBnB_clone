#!/usr/bin/python3
"""Module that tests City model"""
import os
import time
import datetime
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class that tests for City model

    Args:
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "City.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_City_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.city').__doc__
        class_doc = __import__('models.city').city.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_City_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        City1 = City()
        time.sleep(1)
        City2 = City()

        """Checking if the instances are not the same"""
        self.assertNotEqual(City1.id, City2.id)
        self.assertNotEqual(City1.created_at, City2.created_at)
        self.assertNotEqual(City1.updated_at, City2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(City1.id, str)
        self.assertIsInstance(City1.created_at, datetime.datetime)
        self.assertIsInstance(City1.updated_at, datetime.datetime)

    def test_City_initialization_argument(self):
        """Testing initialization with arguments"""
        City1 = City()
        City2 = City(**City1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(City1.id, City2.id)
        self.assertEqual(City1.updated_at, City2.updated_at)
        self.assertEqual(City1.created_at, City2.created_at)

    def test_City_str_method(self):
        """Testing City str method"""
        City1 = City()

        self.assertTrue(str(City1).startswith("[City]"))

        self.assertIn(City1.id, str(City1))
        self.assertIn("created_at", str(City1))
        self.assertIn("updated_at", str(City1))

    def test_City_to_dict_method(self):
        """Testing City to_dict method"""
        City1 = City()

        my_dict = City1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing City for save method"""
        City1 = City()
        City2 = City(**City1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(City1.created_at, City2.created_at)
        self.assertEqual(City1.updated_at, City2.updated_at)
        self.assertEqual(City1.created_at, City1.updated_at)
        self.assertEqual(City2.created_at, City2.updated_at)

        time.sleep(1)
        City1.save()
        City2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(City1.created_at, City1.updated_at)
        self.assertNotEqual(City2.created_at, City2.updated_at)


if __name__ == "__main__":
    unittest.main()
