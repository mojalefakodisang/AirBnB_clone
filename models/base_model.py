#!/usr/bin/env python
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        if kwargs is True:
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
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
        
    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                v = v.isoformat()
            new_dict[k] = v

        return new_dict