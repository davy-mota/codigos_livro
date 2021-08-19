sandwich_orders = ['Atum','Pastrami', 'Vegetariano', 'Frango', 'Pastrami', 'Carne Bovina', 'Pasta de Amendoim', 'Geleia', 'Pastrami']
finished_sandwhiches = []

print('Estamos sem pastrami e por isso os pedidos que contem pastrami serão cancelados. Obrigado pela compreensão!!!\n')

while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')
	 
while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	print('Preparei seu sanduiche de ' + sandwich_order)
	finished_sandwhiches.append(sandwich_order)
print('\nOs seguintes sanduiches foram preparados:\n')
for finished_sandwhich in finished_sandwhiches:
	print(finished_sandwhich)
	


