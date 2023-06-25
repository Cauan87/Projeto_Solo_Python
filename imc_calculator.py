def calculate_imc(height, weight):
    height_in_meters = height / 100
    imc = float(weight / (height_in_meters ** 2))
    return imc