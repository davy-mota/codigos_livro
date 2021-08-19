lista_usuarios = []

if lista_usuarios:
	for lista_usuario in lista_usuarios:
		if lista_usuario == 'admin':
			print('Olá admin, gostaria de ver um relatório de status?')
		else:
			print('Olá {}, obrigado por fazer login novamente.'.format(lista_usuario.title()))
else:		
	print('Precisamos encontrar alguns usuários!')




