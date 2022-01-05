def car_information(manufacturer, model, **extra_information):
    car = {'Fabricante': manufacturer, 'Modelo': model}
    for key, value in extra_information.items():
        car[key] = value
        return car



car = car_information('Ferrari', 'Nao sei nada de carro', alguma_informacao='opa')
print(car)