#!/usr/bin/python3
"""Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class.

    Attr:
        place_id (str)
        text (str)
        user_id (str)
    """
    place_id = ""
    text = ""
    user_id = ""
