#!/usr/bin/python3
"""Tests for the file_storage module"""
from datetime import datetime
import json
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import models
import os
import unittest


class testFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    # -------------------- Tests for #5--------------------
    def test_instanciation(self):
        """Test FileStorage instanciation"""
        new = FileStorage()

        self.assertIsInstance(new, FileStorage)

    def self_file_path(self):
        """Test for the __file_path attribute"""
        self.storage = FileStorage()

        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertTrue(self.storage._FileStorage__file_path.endswith(".json"))

    def test_objects(self):
        """Tests the __objects attribute"""
        self.storage = FileStorage()

        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Tests for all method"""
        self.storage = FileStorage()
        all_obj = self.storage.all()

        self.assertIsNotNone(all_obj)
        self.assertIsInstance(all_obj, dict)

    def test_new(self):
        """Tests for the new method"""
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        k = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(k, self.storage.all())

    def test_save(self):
        """Tests for the save method"""
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)

        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()

        k = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(k, new_storage.all())
        self.assertIsInstance(new_storage.all()[k], BaseModel)

    def test_reload(self):
        """Test for the reload method"""
        user1 = BaseModel()
        user1.save()
        self.assertTrue(os.path.isfile("file.json"))
        all_objs = models.storage.all()
        expected = {k: v.to_dict() for k, v in all_objs.items()}
        models.storage.reload()
        with self.subTest():
            output = {k: v.to_dict() for k, v in all_objs.items()}
            self.maxDiff = None
            self.assertEqual(output, expected)
        with self.subTest():
            objs = file_storage.FileStorage._FileStorage__objects
            self.assertEqual(all_objs, objs)

    def test_reload_with_no_json_file(self):
        """Test to check that no exception is raised:
        when the file doesn't exist"""
        self.storage = FileStorage()

        self.storage.reload()


if __name__ == "__main__":
    unittest.main()
