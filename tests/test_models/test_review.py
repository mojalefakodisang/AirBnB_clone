#!/usr/bin/python3
"""Module that tests Review model"""
import os
import time
import datetime
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class that tests for Review model

    Argsr
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "Review.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_Review_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.review').__doc__
        class_doc = __import__('models.review').review.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_Review_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        Review1 = Review()
        time.sleep(1)
        Review2 = Review()

        """Checking if the instances are not the same"""
        self.assertNotEqual(Review1.id, Review2.id)
        self.assertNotEqual(Review1.created_at, Review2.created_at)
        self.assertNotEqual(Review1.updated_at, Review2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(Review1.id, str)
        self.assertIsInstance(Review1.text, str)
        self.assertIsInstance(Review1.user_id, str)
        self.assertIsInstance(Review1.place_id, str)
        self.assertIsInstance(Review1.created_at, datetime.datetime)
        self.assertIsInstance(Review1.updated_at, datetime.datetime)

    def test_Review_initialization_argument(self):
        """Testing initialization with arguments"""
        Review1 = Review()
        Review2 = Review(**Review1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(Review1.id, Review2.id)
        self.assertEqual(Review1.updated_at, Review2.updated_at)
        self.assertEqual(Review1.created_at, Review2.created_at)

    def test_Review_str_method(self):
        """Testing Review str method"""
        Review1 = Review()

        self.assertTrue(str(Review1).startswith("[Review]"))

        self.assertIn(Review1.id, str(Review1))
        self.assertIn("created_at", str(Review1))
        self.assertIn("updated_at", str(Review1))

    def test_Review_to_dict_method(self):
        """Testing Review to_dict method"""
        Review1 = Review()

        my_dict = Review1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing Review for save method"""
        Review1 = Review()
        Review2 = Review(**Review1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(Review1.created_at, Review2.created_at)
        self.assertEqual(Review1.updated_at, Review2.updated_at)
        self.assertEqual(Review1.created_at, Review1.updated_at)
        self.assertEqual(Review2.created_at, Review2.updated_at)

        time.sleep(1)
        Review1.save()
        Review2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(Review1.created_at, Review1.updated_at)
        self.assertNotEqual(Review2.created_at, Review2.updated_at)


if __name__ == "__main__":
    unittest.main()
