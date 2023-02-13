#!/usr/bin/python3
"""Test module for city model"""

from models.city import City
from datetime import datetime
import unittest


class TestCity(unittest.TestCase):
    """Test module for city class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        city = City()

        self.assertIsInstance(city, City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.id, str)

        self.assertEqual(len(city.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        city = City()

        last_updated = city.updated_at
        city.save()

        self.assertIsInstance(city.updated_at, datetime)
        self.assertNotEqual(city.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["created_at"],
                         city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         city.updated_at.isoformat())
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["__class__"], "City")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        city = City()
        city.state_id = "root"
        city.name = "Ola"
        city_dict = city.to_dict()

        new_city = City(**city_dict)

        self.assertEqual(city.created_at, new_city.created_at)
        self.assertEqual(city.id, new_city.id)
        self.assertEqual(city.created_at, new_city.created_at)
        self.assertEqual(city.created_at, new_city.created_at)
        self.assertEqual(new_city.state_id, "root")
        self.assertEqual(new_city.name, "Ola")
        self.assertEqual(str(city), str(new_city))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        city = City()
        city_dict = city.to_dict()

        new_city = City("hello", **city_dict)

        self.assertEqual(city.created_at, new_city.created_at)
        self.assertEqual(city.id, new_city.id)
        self.assertEqual(city.created_at, new_city.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        city = City()
        city.name = "root"
        city.state_id = "odj"

        city_dict = city.to_dict()

        new_city = City(**city_dict)

        self.assertEqual(city.created_at, new_city.created_at)
        self.assertEqual(city.id, new_city.id)
        self.assertEqual(new_city.name, "root")
        self.assertEqual(new_city.state_id, "odj")
        self.assertEqual(city.created_at, new_city.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        city = City()
        city_dict = city.to_dict()
        city_dict["__class__"] = "MySomeClass"

        new_city = City(**city_dict)
        self.assertNotEqual(new_city.__class__.__name__,
                            city_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        city = City()
        city_dict = {"id": "something"}

        new_city = City(**city_dict)

        with self.assertRaises(Exception):
            val = new_city.created_at
            val = new_city.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        city = City()

        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
