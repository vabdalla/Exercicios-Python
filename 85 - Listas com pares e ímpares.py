# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista_principal = [[], []]
numero = 0
for c in range(0,7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        lista_principal[0].append(numero)
    else:
        lista_principal[1].append(numero)
lista_principal[0].sort()
lista_principal[1].sort()
print(f'Os valores pares digitados foram: {lista_principal[0]}')
print(f'Os valores impares digitados foram: {lista_principal[1]}')
