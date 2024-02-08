#!/usr/bin/env python
"""Console module that implemets the console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class that implements the console"""
    
    prompt = "(hbnb) "
        
    def do_create(self, args):
        args = args.split()
        subclasses = models.storage.fetch_subclasses(BaseModel)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in subclasses:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()
            
    def do_show(self, args):
        subclasses = models.storage.fetch_subclasses(BaseModel)
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in subclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            target_id = f"{args[0]}.{args[1]}"
            objects = models.storage.all()
            if target_id not in objects.keys():
                print("** no instance found **")
            else:
                for k, v in objects.items():
                    if k == target_id:
                        print(v)
    
    def do_destroy(self, args):
        subclasses = models.storage.fetch_subclasses(BaseModel)
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in subclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            target_id = f"{args[0]}.{args[1]}"
            objects = models.storage.all()
            if target_id not in objects.keys():
                print("** instance not found **")
            else:
                del objects[target_id]
                models.storage.save()
    
    def do_all(self, args):
        all_list = []
        args = args.split()
        objects = models.storage.all()
        subclasses = models.storage.fetch_subclasses(BaseModel)
        if len(args) >= 0:
            if len(args) == 0:
                for obj in objects.values():
                    all_list.append(str(obj))
                print(all_list)
            else:
                if args[0] not in subclasses:
                    print("** class doesn't exist **")
                else:
                    for obj in objects.values():
                        all_list.append(str(obj))
                    print(all_list)
        
    def do_quit(self, args):
        """Quits or exits the console"""
        return True
    
    def do_EOF(self, args):
        """Quits or exits the console"""
        return True
    
    def emptyline(self):
        """Passes when an empty line is passed"""
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()