from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from imc_calculator import IMCCalculator
from format_imc import IMCFormatted

app = Flask(__name__, static_url_path='/static')

calculator = IMCCalculator()
formatter = IMCFormatted()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/imc_result', methods=['GET', 'POST'])
def imc_result():
    if request.method == 'POST':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        imc = calculator.calculate_imc(height, weight)
        imc_formatted= formatter.format_imc(imc)
        return render_template('imc_result.html', imc=imc_formatted)


if __name__ == '__main__':
    app.run(debug=True)
