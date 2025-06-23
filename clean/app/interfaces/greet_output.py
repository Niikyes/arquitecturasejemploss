from abc import ABC, abstractmethod

class GreetOutput(ABC):
    @abstractmethod
    def present_greeting(self, message: str) -> None:
        pass