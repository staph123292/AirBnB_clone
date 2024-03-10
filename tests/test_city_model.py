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