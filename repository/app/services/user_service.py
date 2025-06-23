from app.interfaces.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def greet_user(self, user_id: int):
        user = self.repo.get_user(user_id)
        print(f"Hola, {user.name} desde Repository Pattern!")