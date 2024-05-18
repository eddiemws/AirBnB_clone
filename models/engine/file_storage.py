#!/usr/bin/python3
""" FileStorage class is file defines the storage system for
the project. It will use JSON format to serialize and deserialize objects"""
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
import json


class FileStorage:
    """
    This is  will serve as an Object relation mappingto interface or database.

    class private variables:
        __file_path (str)
        __objects (dict)
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ Returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Stores a new Object. """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file."""
        obj_dict = FileStorage.__objects
        objd = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(objd, myfile)

    def reload(self):
        """deserialize the JSON file."""
        try:
            with open(FileStorage.__file_path) as myfile:
                objdict = json.load(myfile)
                for i in objdict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
