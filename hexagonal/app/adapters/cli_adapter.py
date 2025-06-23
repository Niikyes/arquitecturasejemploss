from app.core.hello_service import HelloService
from app.adapters.print_output import ConsolePrinter

def run_cli():
    name = input("¿Cuál es tu nombre?: ")
    printer = ConsolePrinter()
    hello_service = HelloService(printer)
    hello_service.say_hello(name)