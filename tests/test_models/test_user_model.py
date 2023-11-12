#!/usr/bin/python3
'''
    User class tests
'''
import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):

    def test_User_inheritance(self):
        first_user = User()
        self.assertIsInstance(first_user, BaseModel)

    def test_User_attributes(self):

        first_user = User()
        self.assertTrue("email" in first_user.__dir__())
        self.assertTrue("first_name" in first_user.__dir__())
        self.assertTrue("last_name" in first_user.__dir__())
        self.assertTrue("password" in first_user.__dir__())

    def test_type_email(self):
        first_user = User()
        name = getattr(first_user, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        first_user = User()
        name = getattr(first_user, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):

        first_user = User()
        name = getattr(first_user, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        first_user = User()
        name = getattr(first_user, "password")
        self.assertIsInstance(name, str)
