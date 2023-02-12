#!/usr/bin/python3
""" Review module for the HBNB project """
from base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""
