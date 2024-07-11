# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela.
lista =[]
maior_numero = 0
for c in range(0,5):
    valor_digitado = int(input('Digite um valor: '))
    lista.append(valor_digitado)
    lista.sort()
    if valor_digitado >= maior_numero:
        print('Adicionado ao final da lista...')
        maior_numero=valor_digitado
    else:
        print(f'Adicionado na posição {lista.index(valor_digitado)} da lista')
print('-='*30)
print(f'Os valores digitados foram {lista}')
