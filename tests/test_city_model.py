#!/usr/bin.python3
"""Test the City class"""

import unittest
from models.base_model import BaseModel
from models import storage
from models.city import City

class TestCity(unittest.TestCase):
    """City model test class"""
    
    def setUp(self):
        """Set up test dependencies"""
        self.city = City()
        self.city.name = ""
        self.city.state_id = ""

    def test_attributes(self):
        """Test that the appropriate attributes are set"""

        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_create_city(self):
        """Test creating a new city"""
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_new_instance_stored_in_objects(self):
        """Test new instance is stored in storage"""
        self.assertIn(self.city, storage.all().values())