#!/usr/bin/python3

"""
    Review class tests
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_Review_inheritance(self):
        raw_review = Review()
        self.assertIsInstance(raw_review, BaseModel)

    def test_Review_attributes(self):
        raw_review = Review()
        self.assertTrue("place_id" in raw_review.__dir__())
        self.assertTrue("user_id" in raw_review.__dir__())
        self.assertTrue("text" in raw_review.__dir__())

    def test_Review_attributes(self):
        raw_review = Review()
        place_id = getattr(raw_review, "place_id")
        user_id = getattr(raw_review, "user_id")
        text = getattr(raw_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
