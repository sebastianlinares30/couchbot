from repositories.user_repositories import UserRepository

"""
This module acts as an intermediary layer between the login controller and the data repository.
"""

class LoginService:
    """
    Handles the application logic for user login.
    """
    def __init__(self) -> None:
        """
        Initializes the service by instantiating the UserRepository to handle database queries.
        """
        self.user_repository = UserRepository()

    def login(self, user):
        """
        Takes a User object, queries the database using the email and returns a success or failure status response.
        """
        # Queries the database repository using the email from the User object
        result = self.user_repository.find_user(user.email)

        # If a matching user record is found, return a successful status
        if result:
            return {"success": True}
        # Otherwise, return a failed status
        return {"success": False}