current_users = ['Taynara', 'Lucas', 'Joel', 'michel', 'Alisson']
new_users = ['Taynara', 'lucas', 'Joel', 'heugenio', 'andreia']

users_lower = []

for i in current_users:
	users_lower.append(i.lower())

for i in new_users:
    if i.lower() in users_lower:
        print('O usuário: {} Já está cadastrado!'.format(i))
    else:
        print('O usuário: {} Está disponível!'.format(i))

