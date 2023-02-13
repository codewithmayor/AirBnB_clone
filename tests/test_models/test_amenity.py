#!/usr/bin/python3
"""Test module for amenity model"""

from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """Test module for amenity class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        amenity = Amenity()

        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.id, str)

        self.assertEqual(len(amenity.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        amenity = Amenity()

        last_updated = amenity.updated_at
        amenity.save()

        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertNotEqual(amenity.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["created_at"],
                         amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["id"], amenity.id)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        amenity = Amenity()
        amenity.name = "root"

        amenity_dict = amenity.to_dict()

        new_amenity = Amenity(**amenity_dict)

        self.assertEqual(amenity.created_at, new_amenity.created_at)
        self.assertEqual(amenity.id, new_amenity.id)
        self.assertEqual(amenity.created_at, new_amenity.created_at)
        self.assertEqual(amenity.created_at, new_amenity.created_at)
        self.assertEqual(new_amenity.name, "root")
        self.assertEqual(str(amenity), str(new_amenity))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        new_amenity = Amenity("hello", **amenity_dict)

        self.assertEqual(amenity.created_at, new_amenity.created_at)
        self.assertEqual(amenity.id, new_amenity.id)
        self.assertEqual(amenity.created_at, new_amenity.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        amenity = Amenity()
        amenity.name = "root"

        amenity_dict = amenity.to_dict()

        new_amenity = Amenity(**amenity_dict)

        self.assertEqual(amenity.created_at, new_amenity.created_at)
        self.assertEqual(amenity.id, new_amenity.id)
        self.assertEqual(new_amenity.name, "root")
        self.assertEqual(amenity.created_at, new_amenity.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        amenity_dict["__class__"] = "MySomeClass"

        new_amenity = Amenity(**amenity_dict)
        self.assertNotEqual(new_amenity.__class__.__name__,
                            amenity_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        amenity = Amenity()
        amenity_dict = {"id": "something"}

        new_amenity = Amenity(**amenity_dict)

        with self.assertRaises(Exception):
            val = new_amenity.created_at
            val = new_amenity.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        amenity = Amenity()

        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
