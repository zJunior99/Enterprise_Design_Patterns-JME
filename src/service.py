from typing import Optional, List
from src.models import User
from src.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repo = repository

    def register_user(self, name: str, email: str) -> User:
        if not name or not email:
            raise ValueError("Name and email are required")
        if "@" not in email:
            raise ValueError("Invalid email format")
        return self.repo.save(User(name=name, email=email))

    def get_user(self, user_id: int) -> Optional[User]:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return user

    def list_users(self) -> List[User]:
        return self.repo.get_all()

    def remove_user(self, user_id: int) -> bool:
        return self.repo.delete(user_id)