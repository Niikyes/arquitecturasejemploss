from abc import ABC, abstractmethod
from app.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass