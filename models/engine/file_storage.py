#!/usr/bin/python3
"""_
FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class to manage storage of objects in JSON file
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        Returns a dictionary containing all objects
        """
        return FileStorage.__objects
    
    def new(self, object) -> None:
        """
        A function to add a new object to the FileStorage, using the object's type name and id as the key.
        
        Args:
            object: The object to be added to the FileStorage.
        
        Returns:
            None
        """
        key = f"{type(object).__name__}.{str(object.id)}"
        FileStorage.__objects[key] = object
    
    def save(self) -> None:
        """
        Save the objects to a file in JSON format.
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objects, f)
            
    def all(self) -> dict:
        """
        Return a dictionary containing all objects.
        """
        return FileStorage.__objects
    
    def reload(self) -> None:
        """
        Reloads the objects from the JSON file. If the file does not exist, it does nothing.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
                
                for key, value in FileStorage.__objects.items():
                    class_name = value['__class__']
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
