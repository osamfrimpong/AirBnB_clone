#!/usr/bin/python3

"""
    The test for amenity class
"""

import unittest
import os
import pep8
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel



class TestAmenity(unittest.TestCase):
    def test_Amenity_inheritence(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
        
