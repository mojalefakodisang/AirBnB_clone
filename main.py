#!/usr/bin/env python
from models.base_model import BaseModel

new = BaseModel()
print("===")
print(str(new))
print("===")
new_dict = new.to_dict()
print(new_dict)
print("== Created ==")
new = BaseModel()
new_dict = new.to_dict()
print(new_dict)
print("== Updated ==")
new.save()
new_dict = new.to_dict()
print(new_dict)