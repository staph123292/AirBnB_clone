#!/bin/bash/python3
import cmd
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import datetime

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        And saves it into a json file
        """
        if not line:
            print("** class name missing **")
            return
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")
    
    def emptyline(self) -> bool:
        """
        Empty line input handler
        """
        
        return super().emptyline()
    
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        else:
            line = line.split()
            try:
                objects_dictionary = storage.all()[line[0] + "." + line[1]].to_dict()
                print(objects_dictionary)
            except KeyError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
    
    def do_destroy(self, line):
        """
        A function to destroy an instance of a class. It takes a 'line'
        parameter and does the deletion based on the input provided in the 'line'. 
        """
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            try:
                del storage.all()[line[0] + "." + line[1]]
                storage.save()
            except KeyError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")        
    
    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not line:
            print([str(i) for i in storage.all().values()])
        else:
            line = line.split()
            try:
                print([str(i) for i in storage.all().values() if type(i).__name__ == line[0]])
            except KeyError:
                print("** class doesn't exist **")
    
    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if not line:
            print("** class name missing **")
            return
        else:
            line = line.split()
            try:
                objects = storage.all()[line[0] + "." + line[1]]
                if len(line) < 3:
                    print("** attribute name missing **")
                    return
                if len(line) < 4:
                    print("** value missing **")
                    return
                
                attribute_name = line[2]
                attribute_value = line[3][1:-1]
                
                if attribute_name in ["created_at", "updated_at"]:
                    print(f"Can't update {attribute_name}")
                    return
                if hasattr(objects, attribute_name):
                    attribute_value = type(getattr(objects, attribute_name))(attribute_value)
                    setattr(objects, attribute_name, attribute_value)
                    objects.save()
                else:
                    setattr(objects, attribute_name, attribute_value)
                    objects.save()
            except KeyError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
        
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
