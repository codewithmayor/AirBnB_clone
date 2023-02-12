#!/usr/bin/python3
"""This modules defines the parent class to all classes in our hbnb clone"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """A parent class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
		models.storage.new(self)

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    val = datetime.strptime(kwargs["created_at"],
                                            "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    val = datetime.strptime(kwargs["updated_at"],
                                            "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """Returns user-friendly string version of attributes"""
        dictt = self.to_dict()
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return "[{:s}] ({:s}) {}".format(cls, self.id, dictt)

    def save(self):
        """Updates the current time and to file storage"""
        self.updated_at = datetime.utcnow()
		models.storage.save()

    def to_dict(self):
        """Returns dictionary all keys of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
