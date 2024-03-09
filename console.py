#!/bin/bash/python3
import cmd
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        And saves it into a json file
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")
    
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
        
        
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
