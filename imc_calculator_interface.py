from abc import ABC, abstractmethod

class IMCCalculatorInterface(ABC):
    @abstractmethod
    def calculate_imc(self, height, weight):
        pass