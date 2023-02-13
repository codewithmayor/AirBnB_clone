#!/usr/bin/python3
"""Test module for place model"""

from models.place import Place
from datetime import datetime
import unittest


class TestPlace(unittest.TestCase):
    """Test module for place class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.id, str)

        self.assertEqual(len(place.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        place = Place()

        last_updated = place.updated_at
        place.save()

        self.assertIsInstance(place.updated_at, datetime)
        self.assertNotEqual(place.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["created_at"],
                         place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         place.updated_at.isoformat())
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        place = Place()
        place.city_id = "root"
        place.user_id = "root"
        place.name = "Ola"
        place_dict = place.to_dict()

        new_place = Place(**place_dict)

        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(place.id, new_place.id)
        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(new_place.city_id, "root")
        self.assertEqual(new_place.user_id, "root")
        self.assertEqual(new_place.name, "Ola")
        self.assertEqual(str(place), str(new_place))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        place = Place()
        place_dict = place.to_dict()

        new_place = Place("hello", **place_dict)

        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(place.id, new_place.id)
        self.assertEqual(place.created_at, new_place.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        place = Place()
        place.name = "root"
        place.d = "u"

        place_dict = place.to_dict()

        new_place = Place(**place_dict)

        self.assertEqual(place.created_at, new_place.created_at)
        self.assertEqual(place.id, new_place.id)
        self.assertEqual(new_place.name, "root")
        self.assertEqual(new_place.d, "u")
        self.assertEqual(place.created_at, new_place.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        place = Place()
        place_dict = place.to_dict()
        place_dict["__class__"] = "MySomeClass"

        new_place = Place(**place_dict)
        self.assertNotEqual(new_place.__class__.__name__,
                            place_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        place = Place()
        place_dict = {"id": "something"}

        new_place = Place(**place_dict)

        with self.assertRaises(Exception):
            val = new_place.created_at
            val = new_place.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_of_rooms, 0)
        self.assertEqual(place.number_of_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
