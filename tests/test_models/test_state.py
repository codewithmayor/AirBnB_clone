#!/usr/bin/python3
"""Test module for state model"""

from models.state import State
from datetime import datetime
import unittest


class TestState(unittest.TestCase):
    """Test module for state class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.id, str)

        self.assertEqual(len(state.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        state = State()

        last_updated = state.updated_at
        state.save()

        self.assertIsInstance(state.updated_at, datetime)
        self.assertNotEqual(state.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["created_at"],
                         state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         state.updated_at.isoformat())
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["__class__"], "State")

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        state = State()
        state.name = "root"
        state_dict = state.to_dict()

        new_state = State(**state_dict)

        self.assertEqual(state.created_at, new_state.created_at)
        self.assertEqual(state.id, new_state.id)
        self.assertEqual(state.created_at, new_state.created_at)
        self.assertEqual(state.created_at, new_state.created_at)
        self.assertEqual(new_state.name, "root")
        self.assertEqual(str(state), str(new_state))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        state = State()
        state_dict = state.to_dict()

        new_state = State("hello", **state_dict)

        self.assertEqual(state.created_at, new_state.created_at)
        self.assertEqual(state.id, new_state.id)
        self.assertEqual(state.created_at, new_state.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        state = State()
        state.name = "root"
        state.bolu = "you"

        state_dict = state.to_dict()

        new_state = State(**state_dict)

        self.assertEqual(state.created_at, new_state.created_at)
        self.assertEqual(state.id, new_state.id)
        self.assertEqual(new_state.name, "root")
        self.assertEqual(new_state.bolu, "you")
        self.assertEqual(state.created_at, new_state.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        state = State()
        state_dict = state.to_dict()
        state_dict["__class__"] = "MySomeClass"

        new_state = State(**state_dict)
        self.assertNotEqual(new_state.__class__.__name__,
                            state_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        state = State()
        state_dict = {"id": "something"}

        new_state = State(**state_dict)

        with self.assertRaises(Exception):
            val = new_state.created_at
            val = new_state.updated_at

    def test_default_instance_attributes(self):
        """
        Test that default values for instance attributes
        are set to the correct class attributes
        """

        state = State()

        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
