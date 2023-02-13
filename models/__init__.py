#!/usr/bin/python3
from .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "Amenity": Amenity
}

storage = FileStorage()
storage.reload()
