#!/usr/bin/python3
"""File storage for project"""
import json
from models.base_model import BaseModel

class FileStorage:
	"""This is the storage engine for the project"""

	__file_path = 'file.json'
	__objects = {}

	def all(self):
		"""Returns the dictionary __objects"""
		return self.__objects

	def new(self,obj):
		"""Sets in __objects to existing dictionary"""
		if obj:
			key = '{}.{}'.format(obj.__class__.name__, obj.id)
			self.__objects[keys] = obj

	def save(self)
		"""Serializes __objecrs to the JSON file"""
		obj_dict = {}

		for key, obj in self.__objects.items():
			obj_dict[key] = obj.to_dict()
		with open(self.__file_path, 'w', encoding="UTF-8") as f:
			json.dump(obj_dict, f)

	def reload(self)
	"""Deserializes the JSON file to __objects"""
	try:
		with open(self.__file_path, 'r', encoding="UTF-8") as f:
			new_obj_dict = json.load(f)
		for key, value in new_obj_dict.items():
			obj = self.class_dict[value['__class']](**value)
			self.__objects[key] = obj
	except FileNotFoundError:
		pass
