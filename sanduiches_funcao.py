def list_sandwich(*lista):
	print('\nOs seguintes itens foram pedidos: \n')
	for itens in lista:
		print(itens)
		
	
list_sandwich('Pão')
list_sandwich('Queijo', 'Presunto')
list_sandwich('Ovo', 'Tomate', 'Alface')


