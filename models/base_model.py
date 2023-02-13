#!/usr/bin/python3
"""Base Model Module """
import uuid
from datetime import datetime


class BaseModel:
    """Base Model Class
        The base model class is the base for
        all other classes
    """

    def __init__(self, *args, **kwargs):
        """Constructor for baseModel"""

        if len(kwargs) == 0:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                # Don't copy __class__ attribute
                if key == "__class__":
                    continue

                # Set created_at and updated_at to instances of datetime
                if key in ["created_at", "updated_at"]:
                    self.__setattr__(key, datetime.fromisoformat(value))
                    continue

                self.__setattr__(key, value)

    def __str__(self):
        """String representation of object instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save function
        Updates the update_at instance attribute
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict function
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__

        return new_dict
