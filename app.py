from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='/static')

def calculate_imc(height, weight):
    height_in_meters = height / 100
    imc = float(weight / (height_in_meters ** 2))
    return imc

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/imc_result', methods=['GET', 'POST'])
def imc_result():
    if request.method == 'POST':
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        imc = calculate_imc(height, weight)
        return render_template('imc_result.html', imc=imc)


if __name__ == '__main__':
    app.run(debug=True)
