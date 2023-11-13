#!/usr/bin/python3
"""Defines the console to perform operations"""
import ast
import cmd
import json
import re
from shlex import split
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Class definition for AirBnB console"""
    prompt = "(hbnb) "
    __allowed_classes = {'Amenity':Amenity, 'City': City, 'Place': Place, 'Review': Review, 'State':State, 'User':User, 'BaseModel':BaseModel}


    # Helper Functions
    def initial_class_name_checks(self, command_args, instance_id_check=False, is_update=False):
        """Validation checks on inputted commands.
        """
        contains_dict = False
        if len(re.findall(r"{.*}", command_args)) == 1:
            contains_dict = True
            splitted_command_args = command_args.split(maxsplit=2)
        else:
            splitted_command_args = command_args.split() 

        if command_args == "":
            print("** class name missing **")
            return False
        if splitted_command_args[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(splitted_command_args) < 2 and instance_id_check:
            print("** instance id missing **")
            return False
        
        if is_update and not contains_dict and len(splitted_command_args) == 2:
            print("** attribute name missing **")
            return False
        
        if is_update and not contains_dict and len(splitted_command_args) == 3:
            print("** value missing **")
            return False
        
        if is_update and contains_dict and len(splitted_command_args) < 3:
            print("** invalid value **")
            return False
        return True
    # Helper Functions end

    def do_exit(self, command_args):
        """Handle Exit of Console"""
        return True
    
    def do_quit(self, command_args):
        """Handle Exit of Console"""
        return True
    
    def do_EOF(self, command_args):
        """Handle End Of File"""
        return True
    
    def emptyline(self):
        """Handle empty commands in console"""
        pass

    def default(self, command_args):
        """Handles every other non-defined or invalid command"""
        allowed_extra_commands = {"all": self.do_all,
                    "show": self.do_show,
                    "count": self.do_count,
                    "destroy": self.do_destroy,
                    "update": self.do_update}
        
        pattern = r"^(\w+)\.(\w+)\((.*)\)"
        string_search = re.match(pattern, command_args)

        if string_search is not None:
            found_list = string_search.groups()
            if len(found_list) >= 2 and found_list[0] in self.__allowed_classes.keys() and found_list[1] in allowed_extra_commands.keys():
                if found_list[1] == "all":
                    self.do_all(found_list[0])
                elif found_list[1] == "show":
                    self.do_show(f"{found_list[0]} {found_list[2]}")
                elif found_list[1] == "destroy":
                    self.do_destroy(f"{found_list[0]} {found_list[2]}")
                elif found_list[1] == "count":
                    self.do_count(found_list[0])
                else:
                    
                    """for update"""
                    class_name = found_list[0]
                    content = found_list[2].split(", ") if len(re.findall(r"{.*}", found_list[2])) == 0 else found_list[2].split(", ",maxsplit=1) 
                    if len(content) == 3:
                        self.do_update(f"{class_name} {content[0]} {content[1]} {content[2]}")
                    else:
                        """
                        Update with dict
                        """
                        self.do_update(f"{class_name} {content[0]} {content[1]}")
            else:
                 super().default(command_args)
        else:
            super().default(command_args)

    def do_create(self, command_args):
        """Handle creation of object in console"""
        if not self.initial_class_name_checks(command_args):
            return
        else:
            object_to_create = HBNBCommand.__allowed_classes[command_args.split()[0]]()
            object_to_create.save()
            print(object_to_create.id)

    def do_show(self, command_args):
        """Prints the string representation of object in console"""
        
        if not self.initial_class_name_checks(command_args, instance_id_check=True):
            return
        
        else:
            command_args_list = command_args.split()
            key_to_find = f"{command_args_list[0]}.{command_args_list[1]}"
            stored_objects_in_database = storage.all()
            found_item = stored_objects_in_database.get(key_to_find, None)
            if found_item is not None:
                print(found_item)
            else:
                print("** no instance found **")
                return

    def do_destroy(self, command_args):
        """Handle deletion of object"""
        if not self.initial_class_name_checks(command_args, instance_id_check=True):
            return
        
        else:
            command_args_list = command_args.split()
            key_to_find = f"{command_args_list[0]}.{command_args_list[1]}"
            stored_objects_in_database = storage.all()
            found_item = stored_objects_in_database.get(key_to_find, None)
            if found_item is not None:
                del stored_objects_in_database[key_to_find]
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, command_args):
        """Prints all string representation of all instances in the console"""
        stored_objects_in_database = storage.all()
        if command_args == "":
            print([f"{str(value)}" for key, value in stored_objects_in_database.items()])
            return
        elif command_args.split()[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print([f"{str(value)}" for key, value in stored_objects_in_database.items() if key.split('.')[0] == command_args.split()[0]])
            return

    def do_update(self, command_args):
        """Update an instance based on class name"""
        if not self.initial_class_name_checks(command_args, instance_id_check=True, is_update=True):
            return
        
        else:
            command_args_list = split(command_args) if len(re.findall(r"{.*}", command_args)) == 0 else command_args.split(maxsplit=2)
            key_to_find = f"{command_args_list[0]}.{command_args_list[1]}"
            stored_objects_in_database = storage.all()
            found_item = stored_objects_in_database.get(key_to_find, None)
            if found_item is not None:
                """Do the update here"""
                if len(command_args_list) >= 4:
                    if command_args_list[2] in found_item.__class__.__dict__.keys():
                        type_of_variable = type(found_item.__class__.__dict__[command_args_list[2]])
                        found_item.__dict__[command_args_list[2]] = type_of_variable(command_args_list[3])
                elif len(command_args_list) == 3:
                    value_as_dict = ast.literal_eval(command_args_list[2])
                    
                    for index, value in value_as_dict.items():
                        if index in found_item.__class__.__dict__.keys():
                            type_of_variable = type(found_item.__class__.__dict__[index])
                            found_item.__dict__[index] = type_of_variable(value)
                storage.save()

            else:
                print("** no instance found **")
                return
            
    def do_count(self, arguments):
        """Implement counting"""
        number_of_items = 0
        for found_item in storage.all().values():
            if found_item.__class__.__name__ == arguments:
                number_of_items += 1
        print(number_of_items)





if __name__ == '__main__':
    # console_cmd = HBNBCommand()
    # if len(sys.command_argsv) > 1:
    #     """ command_argsuments passed to script"""
    #     for command_argsument in sys.command_argsv[1:]:
    #         console_cmd.onecmd(command_argsument)
    #     print("non-interactive")
        
    # else:
    #     """Do in interactive mode"""
    #     console_cmd.cmdloop()
    #     print("interactive")
    HBNBCommand().cmdloop()
        
