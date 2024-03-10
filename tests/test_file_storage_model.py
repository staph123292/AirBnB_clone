#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    """Test case for file storage model"""
    
    def setUp(self):
        """
        Set up the test fixture. This method is called before the test is executed.
        """
        self.storage = FileStorage()
        self.model = BaseModel
    
    def tearDown(self):
        """Deletes data file after test"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test getting all model objs from storage"""
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertIs(all_objects, self.storage._FileStorage__objects)

    def test_new(self):
        """Test adding a new obj in __objects"""
        self.storage.new(self.model)
        object_key = "{}.{}".format(
                self.model.__class__.__name__, self.model.id
        )
        self.assertIn(object_key, self.storage._FileStorage__objects)

    def test_save_permissions(self):
        """Test permissions to read and write in storage file"""
        self.storage.new(self.model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            content = f.read()
        self.assertTrue(
                os.access(self.storage._FileStorage__file_path, os.R_OK)
        )
        self.assertTrue(
                os.access(self.storage._FileStorage__file_path, os.W_OK)
        )