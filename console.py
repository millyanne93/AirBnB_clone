#!/usr/bin/python3
"""
The console module
"""

import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # Exit commands
    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        pass

    # Create command
    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it,
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in ["BaseModel", "Place", "State",
                                  "City", "Amenity", "Review", "User"]:
                print("** class doesn't exist **")
            else:
                new_instance = getattr(storage.models, class_name)()
                new_instance.save()
                print(new_instance.id)

    # Show command
    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                instance = storage.find_by_id(args[0], args[1])
                print(instance)
            except (NameError, SyntaxError):
                print("** no instance found **")

    # Destroy command
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                storage.delete_by_id(args[0], args[1])
            except (NameError, SyntaxError):
                print("** no instance found **")

    # All command
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        match = re.match(r"^(\w+)\.all\(\)$", arg)

        if match:
            class_name = match.group(1)
            try:
                instances = storage.find_all(class_name)
                print([str(instance) for instance in instances])
            except storage.ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            args = arg.split()
            if not args:
                print("** class name missing **")
            else:
                try:
                    instances = storage.find_all(*args)
                    print([str(instance) for instance in instances])
                except (NameError, SyntaxError):
                    print("** class doesn't exist **")
                except TypeError:
                    print("** invalid arguments **")

    # Update command
    def do_update(self, arg):
        """Updates an instance by adding or updating attribute"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            try:
                instance = storage.find_by_id(class_name, instance_id)
                if instance:
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                else:
                    print("** no instance found **")
            except (NameError, SyntaxError):
                print(f"** no instance found **")

    # Count command
    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if not args or not args[0]:
            print("** class name missing **")
        else:
            try:
                instances = storage.find_all(args[0])
                print(len(instances))
            except (NameError):
                print("** class doesn't exist **")

    def do_models(self, arg):
        """Print all registered Models"""
        print(*storage.models)

    def handle_class_methods(self, arg):
        """Handle Class Methods <cls>.all(), <cls>.show() etc"""
        try:
            if arg.endswith('()'):
                arg = arg[:-2]  # Remove the trailing '()'
            class_name, method_name = arg.split('.')
            cls = getattr(storage.models, class_name)
            if hasattr(cls, method_name) and
            callable(getattr(cls, method_name)):
                method = getattr(cls, method_name)
                result = method()
                print(result)
            else:
                print("** invalid method **")
        except AttributeError:
            print("** invalid method **")
        except (NameError):
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")

    def default(self, arg):
        """Override default method to handle class methods"""
        class_method_pattern = r"^(\w+)\.(\w+)\(\)$"
        match = re.match(class_method_pattern, arg)

        if match:
            class_name = match.group(1)
            method_name = match.group(2)

            if class_name not in ["BaseModel", "Place", "State",
                                  "City", "Amenity", "Review", "User"]:
                print("** class doesn't exist **")
                return

            if method_name == 'count':
                self.do_count(class_name)
            else:
                print("** invalid method **")
        else:
            return cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
