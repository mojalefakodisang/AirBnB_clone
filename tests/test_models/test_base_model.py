#!/usr/bin/python3
"""
Test suite for base_model
"""
import os
import models
import unittest
import datetime
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class."""

    """-------------------- Tests for #3---------------------------"""
    def test_init(self):
        """Tests BaseModel instanciation"""
        model = BaseModel()

        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        """Tests if the __str__ method returns the wanted representation"""
        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))

    def test_save(self):
        """Tests if the updated_at attribute is updated"""
        model = BaseModel()
        updated = model.updated_at
        model.save()

        self.assertEqual(model.updated_at, updated)

    def test_to_dict(self):
        """Tests the returned dictionary after calling to_dict method"""
        model = BaseModel()
        dic = model.__dict__
        new_dic = model.to_dict()

        self.assertNotEqual(dic, new_dic)
        self.assertIn("__class__", new_dic)
        self.assertTrue(isinstance(new_dic["created_at"], str))
        self.assertTrue(isinstance(new_dic["updated_at"], str))

    """-------------------- Tests for #4 --------------------"""
    def test_init_kwargs(self):
        """Tests the instanciation with kwargs"""
        model = BaseModel()
        model_json = model.to_dict()
        new_model = BaseModel(**model_json)

        self.assertFalse(new_model is model)
        self.assertNotIn("__class__", new_model.__dict__)
        self.assertEqual(model.to_dict(), new_model.to_dict())
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)

    """-------------------- Tests for #5 --------------------"""

    def test_save_updates(self):
        """Tests the save method after the updated_at"""
        model = BaseModel()
        time = model.updated_at
        model.save()
        new_time = model.updated_at

        self.assertNotEqual(time, new_time)

    def test_save(self):
        """Tests that save method is called"""

        model = BaseModel()
        model.save()
        k = f"{type(model).__name__}.{model.id}"
        new_dict = {k: model.to_dict()}

        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

        with open("file.json", "r") as f:
            self.assertIn(model.id, f.read())

    def test_save_subclass(self):
        """Testing saving subclasses of BaseModel class"""
        class1 = User()
        class1.save()

        with open("file.json", "r") as f:
            self.assertIn(class1.id, f.read())


if __name__ == "__main__":
    unittest.main()
