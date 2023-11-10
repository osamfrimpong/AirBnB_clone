#!/usr/bin/python3
"""
init methods for models module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
