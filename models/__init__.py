#!/usr/bin/python3
""" Initialize and set up the file storage for models in the directory."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
