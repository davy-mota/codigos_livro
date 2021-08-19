prompt = 'Quais sabores o senhor(a) deseja: \n'
sabores = ''

while sabores != 'quit':
	print(prompt)
	sabores = input()
	print('O sabor ' + sabores.title() + ' foi adicionado com sucesso!!!\n')
	
