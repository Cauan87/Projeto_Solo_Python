from format_imc_interface import IMCFormattedInterface

class IMCFormatted(IMCFormattedInterface):
    def format_imc(self, imc):
        return "{:.2f}".format(imc)