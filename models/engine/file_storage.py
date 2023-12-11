#!/usr/bin/python3
"""Module for FileStorage class."""
from datetime import datetime
import json
import os


class FileStorage:
    """This class is for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}
    models = (
        "BaseModel",
        "User", "City", "State", "Place",
        "Amenity", "Review"
    )

    def __init__(self):
        """Constructor"""
        pass

    def all(self):
        """This returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON storage file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as to_file:
            json.dump(new_dict, to_file)

    def reload(self):
        """This deserializes the JSON file to objects if the file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                model_classes = self.class_dict()

                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in model_classes:
                        self.__objects[key] = model_classes[class_name](**val)
        except (FileNotFoundError):
            pass

    def class_dict(self):
        """Returns a dictionary of classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return class_dict

    def classes(self):
        """Return the list of available model classes."""
        return self.models

    def attributes(self):
        """Return a dictionary of attributes for each model class."""
        return self.class_dict()

    def find_by_id(self, model, obj_id):
        """Find and return an element of model by its id"""
        if model not in self.models:
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        return self.__objects[key]

    def delete_by_id(self, model, obj_id):
        """Delete an element of model by its id"""
        if model not in self.models:
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        del self.__objects[key]
        self.save()

    def find_all(self, model=""):
        """Find all instances or instances of model"""
        if model and model not in self.models:
            raise NameError(model)

        results = [val for key, val in self.__objects.items()
                   if key.startswith(model)]
        return results

    def update_one(self, model, obj_id, field, value):
        """Updates an instance"""
        if model not in self.models:
            raise NameError(model)

        key = f"{model}.{obj_id}"
        if key not in self.__objects:
            raise NameError(obj_id, model)

        instance = self.__objects[key]
        if field not in ("id", "updated_at", "created_at"):
            setattr(instance, field, type(getattr(instance, field))(value))
            instance.updated_at = datetime.utcnow()
            self.save()
