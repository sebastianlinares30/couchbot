from models.user import User
from repositories.user_repositories import UserRepository

class SignUpService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def create_user(self, user:User):
        self.user_repository.create_user(user)
        return {"success": True}