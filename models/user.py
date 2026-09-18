"""
This module defines the User data model.
User is defined by the attributes first name, last name, and email across the application layer.
"""
class User:
    def __init__(self,first_name:str=None,last_name:str=None,email:str=None) -> None:
        """
        Initializes a User instance with default parameters for first name, last name, and email.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email