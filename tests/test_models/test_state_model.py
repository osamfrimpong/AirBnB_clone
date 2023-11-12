#!/usr/bin/python3
"""
    State class tests
"""
from models.base_model import BaseModel
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_State_inheritence(self):
        raw_state = State()
        self.assertIsInstance(raw_state, BaseModel)

    def test_State_attributes(self):
        raw_state = State()
        self.assertTrue("name" in raw_state.__dir__())

    def test_State_attributes_type(self):
        raw_state = State()
        name = getattr(raw_state, "name")
        self.assertIsInstance(name, str)

