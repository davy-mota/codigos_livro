prompt = 'Informe a sua idade para a compra do ingresso: '
ingressos = ''
active = True

while active == True:
	print(prompt)
	ingressos = int(input())
	if ingressos <= 3:
		print('O seu ingresso é gratuito!!!')
	elif ingressos > 3 and ingressos <=12:
		print('O ingresso custará 10 dolares!!!')
	elif ingressos > 12:
		print('O ingresso custará 15 dolares!!!')
	print('Digite "quit" se deseja para o programa ou tecle "ENTER" para continuar.' )
	saida = input()
	#if saida == 'quit':
	#	break;
	if saida == 'quit':
		active = False
	
