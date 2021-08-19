def build_car(modelo, fabricante, **car_info):
	carro = {}
	carro['modelo'] = modelo
	carro['fabricante'] = fabricante
	
	for key, value in car_info.items():
		carro[key] = value
	return carro
	
make_car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(make_car)
