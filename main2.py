#!/usr/bin/env python 
from models.base_model import BaseModel

print("===")
new = BaseModel()
new_dict = new.to_dict()
print(str(new))
print("===")
new_obj = BaseModel(**new_dict)
print(str(new_obj))