#!/usr/bin/python3
"""Tests for the file_storage module"""
from datetime import datetime
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import os
import unittest


class testFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def test_docs(self):
        """Checking for documentation of the file"""
        file_storage = __import__('models.engine.file_storage')
        all_method_doc = file_storage.FileStorage.all.__doc__
        new_method_doc = file_storage.FileStorage.new.__doc__
        save_method_doc = file_storage.FileStorage.save.__doc__
        reload_method_doc = file_storage.FileStorage.reload.__doc__

        class_doc = file_storage.FileStorage.__doc__

        self.assertTrue(class_doc and len(class_doc) > 0)
        self.assertTrue(all_method_doc and len(all_method_doc) > 0)
        self.assertTrue(new_method_doc and len(new_method_doc) > 0)
        self.assertTrue(save_method_doc and len(save_method_doc) > 0)
        self.assertTrue(reload_method_doc and len(reload_method_doc) > 0)

    # -------------------- Tests for #5--------------------
    def test_instanciation(self):
        """Test FileStorage instanciation
        and that the attributes are callable"""
        new = FileStorage()

        self.assertIsInstance(new, FileStorage)
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

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
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

    def test_reload_with_no_json_file(self):
        """Test to check that no exception is raised:
        when the file doesn't exist"""
        self.storage = FileStorage()

        self.storage.reload()


if __name__ == "__main__":
    unittest.main()
