from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from imc_calculator import calculate_imc
from imc_calculator_interface import IMCCalculatorInterface

class IMCCalculator(IMCCalculatorInterface):
    def calculate(self, height, weight):
        height_in_meters = height / 100
        imc = float(weight / (height_in_meters ** 2))
        return imc

app = Flask(__name__, static_url_path='/static')
calculator = IMCCalculator()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/imc_result', methods=['GET', 'POST'])
def imc_result():
    if request.method == 'POST':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        imc = calculator.calculate(height, weight)
        format_imc = "{:.2f}".format(imc)
        return render_template('imc_result.html', imc=format_imc)


if __name__ == '__main__':
    app.run(debug=True)
