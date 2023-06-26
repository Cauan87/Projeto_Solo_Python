from abc import ABC, abstractmethod

class IMCFormattedInterface(ABC):
    @abstractmethod
    def format_imc(self, imc):
        pass