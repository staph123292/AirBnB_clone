#!/usr/bin/python3
import unittest
import uuid
from models.base_model import BaseModel
import datetime
import time

class BaseModelTests(unittest.TestCase):
    """Tests for the BaseModel class"""
    
    def setUp(self) -> None:
        """Set up the test environment"""
        self.base_model = BaseModel()
        
def test_attributes(self):
    """
    Test the presence of attributes in the BaseModel class
    """
    unittest.assertTrue(hasattr(self.base_model, "id"))
    unittest.assertTrue(hasattr(self.base_model, "created_at"))
    unittest.assertTrue(hasattr(self.base_model, "updated_at"))
    unittest.assertTrue(hasattr(self.base_model, "updated_at"))
    unittest.assertTrue(hasattr(self.base_model, "updated_at"))(type(self.base_model.id) is str)
    self.assertEqual(type(self.base_model.created_at), datetime.datetime)
    self.assertEqual(type(self.base_model.updated_at), datetime.datetime)
    
def test_id(self):
    """
    Test the presence of a unique id
    """
    base_model_2 = BaseModel()
    self.assertNotEqual(self.base_model.id, base_model_2.id)

def test_save(self):
    """
    Test the save method
    """
    
    created_at = self.base_model.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    updated_at = self.base_model.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    self.assertEqual(created_at[:6], updated_at[:6])
    
    self.base_model.save()
    self.assertNotEqual(self.base_model.created_at, self.base_model.updated_at)
    
def test_to_dict(self):
    """
    test the to dict method
    """
    base_model = BaseModel()
    base_model_dict = base_model.to_dict()
    self.assertEqual(base_model_dict['__class__'], 'BaseModel')
    self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
    self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())
    self.assertTrue('id' in base_model_dict)
    self.assertTrue('updated_at' in base_model_dict)
    self.assertTrue('created_at' in base_model_dict)
    
def test_str(self):
    
    str_ = str(self.base_model)
    self.assertTrue('BaseModel' in str_)
    self.assertTrue('id' in str_)
    self.assertTrue('created_at' in str_)
    self.assertTrue('updated_at' in str_)

def test_