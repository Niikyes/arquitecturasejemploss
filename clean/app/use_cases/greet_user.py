from app.domain.entities import User
from app.interfaces.greet_output import GreetOutput

class GreetUser:
    def __init__(self, output: GreetOutput):
        self.output = output

    def execute(self, name: str) -> None:
        user = User(name)
        greeting = f"Hola, {user.name} desde Clean Architecture!"
        self.output.present_greeting(greeting)