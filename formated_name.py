def get_formated_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' +  last_name
	return full_name.title()
	
musician =  get_formated_name('jimmi', 'hendrix', 'pereira')
print(musician)
