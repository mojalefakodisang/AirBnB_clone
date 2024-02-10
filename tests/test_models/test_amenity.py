#!/usr/bin/python3
"""Module that tests Amenity model"""
import os
import time
import datetime
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class that tests for Amenity model

    Args:
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "Amenity.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_Amenity_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.amenity').__doc__
        class_doc = __import__('models.amenity').amenity.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_Amenity_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        Amenity1 = Amenity()
        time.sleep(1)
        Amenity2 = Amenity()

        """Checking if the instances are not the same"""
        self.assertNotEqual(Amenity1.id, Amenity2.id)
        self.assertNotEqual(Amenity1.created_at, Amenity2.created_at)
        self.assertNotEqual(Amenity1.updated_at, Amenity2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(Amenity1.id, str)
        self.assertIsInstance(Amenity1.created_at, datetime.datetime)
        self.assertIsInstance(Amenity1.updated_at, datetime.datetime)

    def test_Amenity_initialization_argument(self):
        """Testing initialization with arguments"""
        Amenity1 = Amenity()
        Amenity2 = Amenity(**Amenity1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(Amenity1.id, Amenity2.id)
        self.assertEqual(Amenity1.updated_at, Amenity2.updated_at)
        self.assertEqual(Amenity1.created_at, Amenity2.created_at)

    def test_Amenity_str_method(self):
        """Testing Amenity str method"""
        Amenity1 = Amenity()

        self.assertTrue(str(Amenity1).startswith("[Amenity]"))

        self.assertIn(Amenity1.id, str(Amenity1))
        self.assertIn("created_at", str(Amenity1))
        self.assertIn("updated_at", str(Amenity1))

    def test_Amenity_to_dict_method(self):
        """Testing Amenity to_dict method"""
        Amenity1 = Amenity()

        my_dict = Amenity1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing Amenity for save method"""
        Amenity1 = Amenity()
        Amenity2 = Amenity(**Amenity1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(Amenity1.created_at, Amenity2.created_at)
        self.assertEqual(Amenity1.updated_at, Amenity2.updated_at)
        self.assertEqual(Amenity1.created_at, Amenity1.updated_at)
        self.assertEqual(Amenity2.created_at, Amenity2.updated_at)

        time.sleep(1)
        Amenity1.save()
        Amenity2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(Amenity1.created_at, Amenity1.updated_at)
        self.assertNotEqual(Amenity2.created_at, Amenity2.updated_at)


if __name__ == "__main__":
    unittest.main()
