#!/usr/bin/python3

"""
Test the Amenity class
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class
    """
    
    def test_attributes(self):
        """
        Test the presence of attributes in the Amenity class
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
