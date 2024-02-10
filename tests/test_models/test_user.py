#!/usr/bin/python3
"""Module that tests User model"""
import os
import time
import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class that tests for User model

    Args:
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "user.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_user_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.user').__doc__
        class_doc = __import__('models.user').user.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_user_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        user1 = User()
        time.sleep(1)
        user2 = User()

        """Checking if the instances are not the same"""
        self.assertNotEqual(user1.id, user2.id)
        self.assertNotEqual(user1.created_at, user2.created_at)
        self.assertNotEqual(user1.updated_at, user2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_user_initialization_argument(self):
        """Testing initialization with arguments"""
        user1 = User()
        user2 = User(**user1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.updated_at, user2.updated_at)
        self.assertEqual(user1.created_at, user2.created_at)

    def test_user_str_method(self):
        """Testing user str method"""
        user1 = User()

        self.assertTrue(str(user1).startswith("[User]"))

        self.assertIn(user1.id, str(user1))
        self.assertIn("created_at", str(user1))
        self.assertIn("updated_at", str(user1))

    def test_user_to_dict_method(self):
        """Testing user to_dict method"""
        user1 = User()

        my_dict = user1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing user for save method"""
        user1 = User()
        user2 = User(**user1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(user1.created_at, user2.created_at)
        self.assertEqual(user1.updated_at, user2.updated_at)
        self.assertEqual(user1.created_at, user1.updated_at)
        self.assertEqual(user2.created_at, user2.updated_at)

        time.sleep(1)
        user1.save()
        user2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(user1.created_at, user1.updated_at)
        self.assertNotEqual(user2.created_at, user2.updated_at)


if __name__ == "__main__":
    unittest.main()
