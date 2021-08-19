def make_album(name, title, number_tracks=''):
	informacoes = 'O artista ' + name.title() + ' é o dono do album ' + title
	return informacoes
	
while True:
	print('\n----------------- Insira o nome do artista e o titulo do album!!! -----------------')
	nome = input('Insira o nome do artista:')
	if nome == 'q':
		print('\nObrigado por usar o meu programa <3')
		break
	titulo = input('Insira o nome do album:')
	if titulo == 'q':
		print('\nObrigado por usar o meu programa <3')
		break
	
	print('\nO artista ' + nome.title() + ' é o dono do album ' + titulo.title())
