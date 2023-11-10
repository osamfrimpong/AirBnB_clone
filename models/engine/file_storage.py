#!/usr/bin/python3
import json

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:

    __file_path = "data_store.json"
    __objects = {}

    list_of_classes = {'Amenity':Amenity, 'City': City, 'Place': Place, 'Review': Review, 'State':State, 'User':User}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        object_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[object_key] = obj

    def save(self):
        objects_serialized = {key: object.to_dict() for key, object in self.__objects.items()}
        with open(self.__file_path, 'w') as database_file:
            json.dump(objects_serialized, database_file)
            

    def reload(self):
        try:
            with open(self.__file_path, 'r') as database_file:
                json_string = json.load(database_file)
                for object_content in json_string.values():
                    name_of_object_class = object_content["__class__"]
                    object_class = self.list_of_classes[name_of_object_class]

                    self.new(object_class(**object_content))

        except FileNotFoundError:
            pass