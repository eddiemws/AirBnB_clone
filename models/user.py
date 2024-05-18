#!/usr/bin/python3
""" User Class that Inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User User.

    Attributes:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
