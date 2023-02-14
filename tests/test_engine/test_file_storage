#!/usr/bin/python3
"""Test module for base model"""

from models import storage
from models.base_model import BaseModel
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """Test module for base class"""

    def test_new_object(self):
        """test_new_object function
        Tests that when a new object is created
        it is added to storage
        """

        base = BaseModel()

        objects = storage.all()
        self.assertIs(objects[f"{base.__class__.__name__}.{base.id}"], base)

    def test_reload(self):
        """test_reload function
        Tests that reload rightfully loads all objects
        from the file storage
        """

        test_dict = {
            "id": "d472f74d-19fe-4c98-8c4f-9f56d55994be",
            "created_at": "2023-02-08T13:14:57.812022",
            "updated_at": "2023-02-08T13:14:57.812030",
            "name": "tinubu",
            "friend": "Dami",
            "__class__": "BaseModel"
        }

        dict_key = f"{test_dict['__class__']}.{test_dict['id']}"

        # Add new object directly to storage
        with open("file.json", "w", encoding="utf-8") as f:
            json.dump({dict_key: test_dict}, f)
            f.close()

        # Reload storage and test that object was loaded
        storage.reload()

        objects = storage.all()
        self.assertEqual(objects[dict_key].id, test_dict["id"])
        self.assertEqual(objects[dict_key].friend, test_dict["friend"])
        self.assertEqual(
            objects[dict_key].created_at.isoformat(), test_dict["created_at"])


if __name__ == "__main__":
    unittest.main()
