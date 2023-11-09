#!/usr/bin/python3
"""modle being imported"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    public attrbutes that inherits BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
