#!/usr/bin/python3
"""File storage module"""
import json


class FileStorage:
    """File Storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """new function
        Sets obj in __objects dictionary with a key of
        <class name>.id
        """

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save function
        Serializes __objects to the JSON file specified by
        __file_path
        """

        objects = FileStorage.__objects.copy()

        # Convert objects stored in __object to their dict representation
        for key, value in objects.items():
            objects[key] = value.to_dict()

        # Write objects to file
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects, f, indent=2)
            f.close()

    def reload(self):
        """reload function
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models import classes

        try:
            # Read objects from file if file exists
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
                f.close()

            # Serialize dictionaries back to object instances
            for key, value in objects.items():
                FileStorage.__objects[key] = classes[value["__class__"]](
                    **value)

        except Exception:
            pass
