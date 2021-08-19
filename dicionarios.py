pessoa = {'String': 'Cadeia de caracteres', 'Inteiro': 'Tipo de dado que representa algum subconjunto finito dos inteiros matemáticos', 'Lista': 'Sequência ou coleção ordenada de valores', 'Dicionario': 'Tipo de mapeamento nativo do Python'}

for chave, valor in pessoa.items():
	print(valor)

pessoa['Identação'] = 'Termo aplicado ao código fonte de um programa para ressaltar ou definir a estrutura do algoritmo.'
pessoa['Alfanumerico'] = 'Conjunto de caracteres alfabéticos e numéricos.'

for chave, valor in pessoa.items():
	print(valor)
