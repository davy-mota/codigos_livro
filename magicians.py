def show_magicians(list_magicians):
	print('=============LISTA ORIGINAL============')
	while list_magicians:
		magicos = list_magicians.pop()
		print(magicos)

def make_great(copy_magycians):
	print('=============LISTA COM AS ALTERAÇÕES==============')
	while copy_magicians:
		magicos = copy_magicians.pop()
		print(magicos + ' O Grande')
		



list_magicians = ['Houdini', 'David Blaine', 'Criss Angel']	
copy_magicians = list_magicians[:]

show_magicians(list_magicians)
make_great(list_magicians)
