#!/usr/bin/python3
""" City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class.

    Attr:
        state_id (str)
        name (str)
    """
    name = ""
    state_id = ""
