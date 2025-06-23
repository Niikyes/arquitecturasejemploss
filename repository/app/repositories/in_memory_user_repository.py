from app.interfaces.user_repository import UserRepository
from app.domain.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {
            1: User(1, "Juniper"),
            2: User(2, "Alicia"),
            3: User(3, "Carlos")
        }

    def get_user(self, user_id: int) -> User:
        return self.users.get(user_id, User(0, "Desconocido"))