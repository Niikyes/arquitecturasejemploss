from app.interfaces.greet_output import GreetOutput

class ConsoleGreetOutput(GreetOutput):
    def present_greeting(self, message: str) -> None:
        print(message)