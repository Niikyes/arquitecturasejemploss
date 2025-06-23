from app.use_cases.greet_user import GreetUser
from app.infrastructure.cli_output import ConsoleGreetOutput

def main():
    name = input("¿Cuál es tu nombre?: ")
    output = ConsoleGreetOutput()
    use_case = GreetUser(output)
    use_case.execute(name)

if __name__ == "__main__":
    main()