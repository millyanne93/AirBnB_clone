#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""

import json
import os
import datetime


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

    def class_dict(self):
        """Returns a dictionary of classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return class_dict


    def save(self):
        """Serializes objects to JSON storage file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as to_file:
            json.dump(new_dict, to_file)

    def reload(self):
        """This deserializes the JSON file to objects if the file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                model_classes = self.class_dict

                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in model_classes:
                        self.__objects[key] = model_classes[class_name](**val)
        except FileNotFoundError:
            pass

