from app.core.ports import OutputPort

class ConsolePrinter(OutputPort):
    def send_message(self, message: str) -> None:
        print(message)