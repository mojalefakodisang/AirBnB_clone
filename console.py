#!/usr/bin/python3
"""Console module that implemets the console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class that implements the console"""

    prompt = "(hbnb) "
    __from_match = False

    def get_class(self, name):
        """Gets a class ready for initialization

        Args:
            name (str): name of the class

        Returns:
            class: returns a class matching name of the class
        """
        return models.storage.fetch_subclasses(BaseModel).get(name)

    def handle_args_err(self, args, exp_len=1, all=False):
        """Handles errors and tokenize arguments

        Args:
            args (str): arguments
            exp_len (int, optional): expected arguments. Defaults to 1.
            all (bool, optional):.
            Defaults to False.

        Returns:
            bool, list: if err is True and list of arguments
        """
        err = False
        args = args.split()
        objects = models.storage.all()
        if not args and not all:
            err = True
            print("** class name missing **")
        elif args and not self.get_class(args[0]):
            err = True
            print("** class doesn't exist **")
        elif len(args) == 1 and exp_len >= 2:
            err = True
            print("** instance id missing **")
        elif all:
            if len(args) > 0:
                if not self.get_class(args[0]):
                    err = True
                    print("** class doesn't exist **")
        elif exp_len >= 2 and not all:
            target_id = f"{args[0]}.{args[1]}"
            if target_id not in objects.keys():
                err = True
                print("** no instance found **")
            elif exp_len == 4:
                if len(args) < 3:
                    err = True
                    print("** attribute name missing **")
                elif len(args) < 4:
                    err = True
                    print("** value missing **")

        return err, args

    def do_create(self, args):
        """Creates an instance of a class
        ex. create BaseModel

        Args:
            args (str): arguments
        """
        err, line = self.handle_args_err(args)
        if not err and self.get_class(line[0]):
            my_class = self.get_class(line[0])
            new_instance = my_class()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """Prints string representation of an instance
        ex. show <class.__name__> <id>

        Args:
            args (str): arguments
        """
        err, line = self.handle_args_err(args, 2)
        if not err:
            target_id = f"{line[0]}.{line[1]}"
            objects = models.storage.all()
            for k, v in objects.items():
                if k == target_id:
                    print(v)

    def do_destroy(self, args):
        """Deletes an instance of a class
        ex. destroy <class.__name__> <id>

        Args:
            args (str): arguments
        """
        err, line = self.handle_args_err(args, 2)
        if not err:
            objects = models.storage.all()
            target_id = f"{line[0]}.{line[1]}"
            if target_id in objects.keys():
                del objects[target_id]
                models.storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        ex. all or all <class.__name__>

        Args:
            args (str): arguments
        """
        all_list = []
        err, line = self.handle_args_err(args, 0, True)
        if not err:
            all_objects = [obj for k, obj in models.storage.all().items()]

            if line:
                all_objects = [obj for obj in all_objects
                               if obj.__class__.__name__ == line[0]]

            obj_str = [obj.__str__() for obj in all_objects]
            if self.__from_match:
                print("[" + ", ".join(obj_str) + "]")
            else:
                print(obj_str)

    def do_update(self, args):
        """Updates instance
        ex. update <class.__name__> <id> <key> <value>

        Args:
            args (str): arguments
        """
        not_update = ["id", "created_at", "updated_at"]
        err, line = self.handle_args_err(args, 4)
        if not err:
            objects = models.storage.all()
            target_id = f"{line[0]}.{line[1]}"
            for k, v in objects.items():
                if k == target_id:
                    if args[2] not in not_update:
                        setattr(v, line[2], line[3])
                        v.save()

    def do_quit(self, args):
        """Quits or exits the console"""
        return True

    def do_EOF(self, args):
        """Quits or exits the console"""
        return True

    def emptyline(self):
        """Passes when an empty line is passed"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()