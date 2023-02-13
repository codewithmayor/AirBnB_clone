#!/usr/bin/python3
"""Test module for review model"""

from models.review import Review
from datetime import datetime
import unittest


class TestReview(unittest.TestCase):
    """Test module for review class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.id, str)

        self.assertEqual(len(review.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        review = Review()

        last_updated = review.updated_at
        review.save()

        self.assertIsInstance(review.updated_at, datetime)
        self.assertNotEqual(review.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["created_at"],
                         review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         review.updated_at.isoformat())
        self.assertEqual(review_dict["id"], review.id)
        self.assertEqual(review_dict["__class__"], "Review")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        review = Review()
        review.place_id = "root"
        review.user_id = "Ola"
        review.text = "Nice place"
        review_dict = review.to_dict()

        new_review = Review(**review_dict)

        self.assertEqual(review.created_at, new_review.created_at)
        self.assertEqual(review.id, new_review.id)
        self.assertEqual(review.created_at, new_review.created_at)
        self.assertEqual(review.created_at, new_review.created_at)
        self.assertEqual(new_review.place_id, "root")
        self.assertEqual(new_review.user_id, "Ola")
        self.assertEqual(new_review.text, "Nice place")
        self.assertEqual(str(review), str(new_review))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        review = Review()
        review_dict = review.to_dict()

        new_review = Review("hello", **review_dict)

        self.assertEqual(review.created_at, new_review.created_at)
        self.assertEqual(review.id, new_review.id)
        self.assertEqual(review.created_at, new_review.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        review = Review()
        review.text = "root"
        review.user_id = "Ola"
        review.place_id = "Ojota"

        review_dict = review.to_dict()

        new_review = Review(**review_dict)

        self.assertEqual(review.created_at, new_review.created_at)
        self.assertEqual(review.id, new_review.id)
        self.assertEqual(new_review.text, "root")
        self.assertEqual(new_review.user_id, "Ola")
        self.assertEqual(new_review.place_id, "Ojota")
        self.assertEqual(review.created_at, new_review.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        review = Review()
        review_dict = review.to_dict()
        review_dict["__class__"] = "MySomeClass"

        new_review = Review(**review_dict)
        self.assertNotEqual(new_review.__class__.__name__,
                            review_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        review = Review()
        review_dict = {"id": "something"}

        new_review = Review(**review_dict)

        with self.assertRaises(Exception):
            val = new_review.created_at
            val = new_review.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        review = Review()

        self.assertEqual(review.text, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")


if __name__ == "__main__":
    unittest.main()
