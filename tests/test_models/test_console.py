#!/usr/bin/python3
"""
Defines unittests for console.py.
"""
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        """Test for the right promt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Test for empty line input"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())