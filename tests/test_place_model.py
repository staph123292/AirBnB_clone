#!/usr/bin/python3

import unittest
from models.place import place
from models.base_model import BaseModel
from models import storage

class Testplace(unittest.TestCase):
    
    def setUp(self):
        self.place = place()
        
    def test_create_place(self):
        """Test creating a new place"""
        self.assertEqual(str(type(self.place)), "<class 'models.place.place'>")
        self.assertIsInstance(self.place, place)
        self.assertTrue(issubclass(type(self.place), BaseModel))
    
    def test_new_instance_stored_in_objects(self):
        """Test new instance is stored in storage"""
        self.assertIn(self.p, storage.all().values())
        
    def test_attributes(self):
        """Test that the apropriate attributes are set"""
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])