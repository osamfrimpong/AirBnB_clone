#!/usr/bin/python3
"""module being imported"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that manages users objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
