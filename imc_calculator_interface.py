from abc import ABC, abstractmethod

class IMCCalculatorInterface(ABC):
    @abstractmethod
    def calculate(self, height, weight):
        pass