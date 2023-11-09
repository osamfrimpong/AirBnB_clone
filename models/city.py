#!/usr/bin/python3
"""Citty module to take from"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    the public class that will inherit BaseModel
    """
    state_id = ""
    name = ""
