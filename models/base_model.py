#!/usr/bin/python3

""" This is the main file/class that serves as the base for all other models """


from datetime import datetime
import uuid
import models

class BaseModel:
    """ Definition of BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        __init__ instantiate BaseModel class
        """

        if kwargs.keys():
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != "__class__":
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        name_of_class = self.__class__.__name__
        return f"[{name_of_class}] ({self.id}) {self.__dict__}"
        

    def to_dict(self):
        dictionary_of_object = self.__dict__.copy()
        dictionary_of_object['created_at'] = self.created_at.isoformat()
        dictionary_of_object['__class__'] = self.__class__.__name__
        dictionary_of_object['updated_at'] = self.updated_at.isoformat()
        return dictionary_of_object

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()