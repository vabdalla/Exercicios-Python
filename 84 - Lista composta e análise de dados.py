# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
quer_continuar = str
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    quer_continuar = input('Quer continuar? [ S / N ] ').upper()
    if quer_continuar == 'N':
        break
print(f'Ao todo voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}KG. Peso de:  ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

