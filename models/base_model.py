#!/usr/bin/python3
"""
    Base Model
    
    Contains the base model class
"""

import uuid
import datetime


class BaseModel:
    """
    All attributes and methods
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the object with optional arguments and keyword arguments. If keyword arguments are provided,
        it sets the corresponding attributes. If no keyword arguments are provided,
        it sets default values for id, created_at, and updated_at and adds the object to the storage.

        Args:
            *args: unused
            **kwargs: Arbitrary keyword arguments
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        Returns the string representation of the object
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Saves the current object to the storage
        """
        from models import storage

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()

        return obj_dict
