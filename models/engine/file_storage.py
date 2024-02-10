#!/usr/bin/python3
"""file_storage module with FileStorage class"""
import os
import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class to implement de- and serialization"""

    __objects = {}
    __file_path = "file.json"

    def fetch_subclasses(self, cls):
        """Fetches all the subclasses that in inherits cls

        Returns:
            dict: return a dictionary with key being class and value subclass
        """
        subclasses = set([cls]).union(cls.__subclasses__())
        return {c.__name__: c for c in subclasses}

    def all(self):
        """Returns all objects loaded from storage

        Returns:
            dict: a dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """Makes a key from object class and id
        ex. <cls.name>.<obj.id>

        Args:
            obj (_type_): _description_
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects stored in the self.__objects in to a file
        """
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict()
                       for key, value in self.__objects.items()}, f)

    def reload(self):
        """Deserializes objects from a file into self.__objects dictionary
        """
        subclasses = self.fetch_subclasses(BaseModel)
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                self.__objects = {k: subclasses[v['__class__']](**v)
                                  for k, v in objects.items()
                                  if v['__class__'] in subclasses}
