#!/usr/bin/python3
"""Module that tests State model"""
import os
import time
import datetime
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class that tests for State model

    Args:
        unittest (unittest): function used to test cases
    """

    @classmethod
    def setUp(self):
        self.temp_file = ["file.json", "State.txt"]

    @classmethod
    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def test_State_documentation(self):
        """Checking for documentation of the file"""

        """Importing module documentations"""
        mod_doc = __import__('models.state').__doc__
        class_doc = __import__('models.state').state.__doc__

        self.assertTrue(len(mod_doc) > 0)
        self.assertTrue(len(class_doc) > 0)

    def test_State_initialization_no_argument(self):
        """Testing initialization without any arguments"""
        State1 = State()
        time.sleep(1)
        State2 = State()

        """Checking if the instances are not the same"""
        self.assertNotEqual(State1.id, State2.id)
        self.assertNotEqual(State1.created_at, State2.created_at)
        self.assertNotEqual(State1.updated_at, State2.updated_at)

        """Checking instances of each instance"""
        self.assertIsInstance(State1.id, str)
        self.assertIsInstance(State1.name, str)
        self.assertIsInstance(State1.created_at, datetime.datetime)
        self.assertIsInstance(State1.updated_at, datetime.datetime)

    def test_State_initialization_argument(self):
        """Testing initialization with arguments"""
        State1 = State()
        State2 = State(**State1.to_dict())

        """Checking if instances are equal"""
        self.assertEqual(State1.id, State2.id)
        self.assertEqual(State1.updated_at, State2.updated_at)
        self.assertEqual(State1.created_at, State2.created_at)

    def test_State_str_method(self):
        """Testing State str method"""
        State1 = State()

        self.assertTrue(str(State1).startswith("[State]"))

        self.assertIn(State1.id, str(State1))
        self.assertIn("created_at", str(State1))
        self.assertIn("updated_at", str(State1))

    def test_State_to_dict_method(self):
        """Testing State to_dict method"""
        State1 = State()

        my_dict = State1.to_dict()
        self.assertIsInstance(my_dict, dict)

        """Checking if these instances are in the dictionary"""
        self.assertIn("id", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save_method(self):
        """Testing State for save method"""
        State1 = State()
        State2 = State(**State1.to_dict())

        """Checking if the updated times are equal before saving"""
        self.assertEqual(State1.created_at, State2.created_at)
        self.assertEqual(State1.updated_at, State2.updated_at)
        self.assertEqual(State1.created_at, State1.updated_at)
        self.assertEqual(State2.created_at, State2.updated_at)

        time.sleep(1)
        State1.save()
        State2.save()

        """Checking if the file save exists and not empty"""
        self.assertTrue(os.path.exists(self.temp_file[0]))
        self.assertTrue(os.path.getsize(self.temp_file[0]) > 0)

        """Checking if the updated times are equal before saving"""
        self.assertNotEqual(State1.created_at, State1.updated_at)
        self.assertNotEqual(State2.created_at, State2.updated_at)


if __name__ == "__main__":
    unittest.main()
