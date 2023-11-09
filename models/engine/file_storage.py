#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):

        return FileStorage.__object

    def new(self, obj):

        """method related to managing a storage mechanism
           key: created the key of the instance
        """
        key = f"{type(obj).__name__} {obj.id}"
        """using the key in __object and setting the value to obj"""
        FileStorage.__object[key] = obj

    def save(self):

        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__object.items()}
            json.dump(d, f)

    def reload(self):

        """deserializes the JSON file to __objects only if it's a JSON file
           otherwise do nothing,no execption to be raised"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_d = json.load(f)
            obj_d = {k: self.clses()[v["__class__"]](**v)
                     for k, v in obj_d.items()}
