from imc_calculator_interface import IMCCalculatorInterface

class IMCCalculator(IMCCalculatorInterface):
    def calculate_imc(self, height, weight):
        height_in_meters = height / 100
        imc = float(weight / (height_in_meters ** 2))
        return imc