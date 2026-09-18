from models.user import User
from repositories.user_repositories import UserRepository

"""
This module handles the application business logic for user registration.
It acts as an intermediary layer between the controller and the repository.
"""

class SignUpService:
    def __init__(self) -> None:
        """
        Initializes the service by instantiating the UserRepository to handle database interactions.
        """
        self.user_repository = UserRepository()

    def create_user(self, user:User):
        """
        Takes a User object and hands it off to the repository layer to be inserted into the database.
        """
        # Calls the create_user method to add the new user
        self.user_repository.create_user(user)
        return {"success": True}