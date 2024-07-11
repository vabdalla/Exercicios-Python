# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.
lista_aberto = []
lista_fechado = []
cont_aberto = 0
cont_fechado = 0
incorreta = 0
expressao = input('Digite a expressão: ')
for c, v in enumerate(expressao):
    if v == '(':
        lista_aberto.append(v)
        cont_aberto+=1
    elif v == ')':
        lista_fechado.append(v)
        cont_fechado+=1
    if cont_fechado > cont_aberto:
        incorreta+=1

if len(lista_aberto) == len(lista_fechado) and incorreta == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')

