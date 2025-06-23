from app.repositories.in_memory_user_repository import InMemoryUserRepository
from app.services.user_service import UserService

def main():
    user_id = int(input("Ingrese el ID del usuario (1-3): "))
    repo = InMemoryUserRepository()
    service = UserService(repo)
    service.greet_user(user_id)

if __name__ == "__main__":
    main()