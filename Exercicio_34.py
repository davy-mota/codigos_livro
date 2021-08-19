lista_convidados = ['sabotagem', 'kevin', 'Avicci']

print('Eai mano ' + lista_convidados[0].title() + ' te convido para a minha festa, conto com a sua presença.')
print('Fala ' + lista_convidados[1].title() + ' cola na festa pai, conto com a sua presença. Esquece!!!')
print('I count on your presence ' + lista_convidados[2].title() + '.\n')

print('O ' + lista_convidados[2] + ' não poderá comparecer.\n')

lista_convidados[2] = 'daleste'

print('Eai mano ' + lista_convidados[0].title() + ' te convido para a minha festa, conto com a sua presença.')
print('Fala ' + lista_convidados[1].title() + ' cola na festa pai, conto com a sua presença. Esquece!!!')
print('Cola na festa ' + lista_convidados[2].title() + '\n')

print(len(lista_convidados))

print('\nConseguiremos convidar mais três pessoas, pois a mesa será maior!!!\n')

lista_convidados.insert(0, 'felipe')
lista_convidados.insert(2, 'daniel')
lista_convidados.append('dario')

print('Eai mano ' + lista_convidados[1].title() + ' te convido para a minha festa, conto com a sua presença.')
print('Fala ' + lista_convidados[3].title() + ' cola na festa pai, conto com a sua presença. Esquece!!!')
print('Cola na festa ' + lista_convidados[4].title())
print('Cola aí ' + lista_convidados[0].title() + '.')
print('Cola aí ' + lista_convidados[2].title() + '.')
print('Cola aí ' + lista_convidados[5].title() + '.\n')

print(len(lista_convidados))

print('\nA mesa que estava programada não conseguirá chegar a tempo e por isso não terá como manter a lista com todos os convidados!!!')

print('Perdão pelo transtorno ' + lista_convidados[5].title() + '.')
lista_convidados_popped = lista_convidados.pop()
print('Perdão pelo transtorno ' + lista_convidados[4].title() + '.')
lista_convidados_popped = lista_convidados.pop()
print('Perdão pelo transtorno ' + lista_convidados[3].title() + '.')
lista_convidados_popped = lista_convidados.pop()
print('Perdão pelo transtorno ' + lista_convidados[2].title() + '.')
lista_convidados_popped = lista_convidados.pop()
print('Você ainda está na lista ' + lista_convidados[1].title() + '.')
print('Você ainda está na lista ' + lista_convidados[0].title() + '.\n')

print(len(lista_convidados))

del lista_convidados[1]
del lista_convidados[0]

print(len(lista_convidados))



