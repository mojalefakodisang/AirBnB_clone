#!/usr/bin/python3
"""base_model module"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initializes instances of a class"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    v = datetime.fromisoformat(v)
                if k == "updated_at":
                    v = datetime.fromisoformat(v)
                if k != '__class__':
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves an instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts objects of an instance into a dictionary"""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__

        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                v = v.isoformat()
            new_dict[k] = v

        return new_dict
