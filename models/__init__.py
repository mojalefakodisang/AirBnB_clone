#!/usr/bin/env python
"""__init__.py module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()