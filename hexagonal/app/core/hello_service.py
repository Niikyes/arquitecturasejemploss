from app.core.ports import OutputPort

class HelloService:
    def __init__(self, output: OutputPort):
        self.output = output

    def say_hello(self, name: str) -> None:
        message = f"Hola, {name} desde arquitectura hexagonal!"
        self.output.send_message(message)