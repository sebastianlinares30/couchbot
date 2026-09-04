from repositories.user_repositories import UserRepository

class LoginService:
    """
    Handles the application logic for user login.
    """

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def login(self, user):
        result = self.user_repository.find_user(user.email)

        if result:
            return {"success": True}
        return {"success": False}