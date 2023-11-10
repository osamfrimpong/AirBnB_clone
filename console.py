#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Class definition for AirBnB console"""
    prompt = "(hbnb) "
    __allowed_classes = {
        "BaseModel",
        "City",
        "Place",
        "User",
        "State",
        "Amenity",
        "Review"
    }


    def do_exit(self, args):
        return True
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def emptyline(self):
        pass


if __name__ == '__main__':
    # console_cmd = HBNBCommand()
    # if len(sys.argv) > 1:
    #     """ arguments passed to script"""
    #     for argument in sys.argv[1:]:
    #         console_cmd.onecmd(argument)
    #     print("non-interactive")
        
    # else:
    #     """Do in interactive mode"""
    #     console_cmd.cmdloop()
    #     print("interactive")
    HBNBCommand().cmdloop()
        
