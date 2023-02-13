#!/usr/bin/python3
"""Test module for user model"""

from models.user import User
from datetime import datetime
import unittest


class TestUser(unittest.TestCase):
    """Test module for user class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.id, str)

        self.assertEqual(len(user.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        user = User()

        last_updated = user.updated_at
        user.save()

        self.assertIsInstance(user.updated_at, datetime)
        self.assertNotEqual(user.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["__class__"], "User")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        user = User()
        user.password = "root"
        user.last_name = "Ola"
        user.first_name = "Damiloju"
        user.email = "test@gmail.com"
        user_dict = user.to_dict()

        new_user = User(**user_dict)

        self.assertEqual(user.created_at, new_user.created_at)
        self.assertEqual(user.id, new_user.id)
        self.assertEqual(user.created_at, new_user.created_at)
        self.assertEqual(user.created_at, new_user.created_at)
        self.assertEqual(new_user.first_name, "Damiloju")
        self.assertEqual(new_user.last_name, "Ola")
        self.assertEqual(new_user.email, "test@gmail.com")
        self.assertEqual(new_user.password, "root")
        self.assertEqual(str(user), str(new_user))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        user = User()
        user_dict = user.to_dict()

        new_user = User("hello", **user_dict)

        self.assertEqual(user.created_at, new_user.created_at)
        self.assertEqual(user.id, new_user.id)
        self.assertEqual(user.created_at, new_user.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        user = User()
        user.password = "root"
        user.last_name = "Ola"
        user.first_name = "Damiloju"
        user.email = "test@gmail.com"

        base_dict = user.to_dict()

        new_user = User(**base_dict)

        self.assertEqual(user.created_at, new_user.created_at)
        self.assertEqual(user.id, new_user.id)
        self.assertEqual(new_user.first_name, "Damiloju")
        self.assertEqual(new_user.last_name, "Ola")
        self.assertEqual(new_user.password, "root")
        self.assertEqual(new_user.email, "test@gmail.com")
        self.assertEqual(user.created_at, new_user.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        user = User()
        user_dict = user.to_dict()
        user_dict["__class__"] = "MySomeClass"

        new_user = User(**user_dict)
        self.assertNotEqual(new_user.__class__.__name__,
                            user_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        user = User()
        user_dict = {"id": "something"}

        new_user = User(**user_dict)

        with self.assertRaises(Exception):
            val = new_user.created_at
            val = new_user.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        user = User()

        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.email, "")


if __name__ == "__main__":
    unittest.main()
