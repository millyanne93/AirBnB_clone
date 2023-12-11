#!/usr/bin/python3
"""Module for FileStorage class."""
from datetime import datetime
import json
import os


class FileStorage:
    """This class is for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def find_all(self, cls_name=""):
        """Find all instances of a class"""
        if cls_name:
            return [obj for key, obj in self.__objects.items() if cls_name in key]
        return list(self.__objects.values())

    def classes(self):
        """Returns a dictionary of classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """This deserializes the JSON file to objects if the file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                model_classes = self.classes()

                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in model_classes:
                        self.__objects[key] = model_classes[class_name](**val)
        except (FileNotFoundError):
            pass
