#!/usr/bin/python3

"""
    user class test
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    def test_City_inheritance(self):
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)

    def test_User_attributes(self):
        my_city = City()
        self.assertTrue("state_id" in my_city.__dir__())
        self.assertTrue("name" in my_city.__dir__())

    def test_type_name(self):
        my_city = City()
        name = getattr(my_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        my_city = City()
        name = getattr(my_city, "state_id")
        self.assertIsInstance(name, str)
