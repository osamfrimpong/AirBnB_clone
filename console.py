#!/usr/bin/python3
import cmd
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Class definition for AirBnB console"""
    prompt = "(hbnb) "
    __allowed_classes = {'Amenity':Amenity, 'City': City, 'Place': Place, 'Review': Review, 'State':State, 'User':User}

    # Helper Functions
    def initial_class_name_checks(self, command_args, instance_id_check=False):
        """Validation checks on inputted commands.
        """
        if command_args == "":
            print("** class name missing **")
            return False
        if command_args.split()[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(command_args.split()) < 2 and instance_id_check:
            print("** instance id missing **")
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
        pass

    def do_destroy(self, command_args):
        """Handle deletion of object"""
        pass

    def do_all(self, command_args):
        """Prints all string representation of all instances in the console"""
        pass

    def do_update(self, command_args):
        """Update an instance based on class name"""



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
        
