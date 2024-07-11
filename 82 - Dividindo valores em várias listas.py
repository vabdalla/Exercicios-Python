# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_completa = []
lista_pares = []
lista_impares = []
quer_continuar = 's'
numero_digitado = int
while quer_continuar != 'N':
    numero_digitado = int(input('Digite um número: '))
    lista_completa.append(numero_digitado)
    if numero_digitado % 2 == 0:
        lista_pares.append(numero_digitado)
    else:
        lista_impares.append(numero_digitado)
    quer_continuar = input('Quer continuar? [ S / N ]').upper()
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares  é {lista_pares}')
print(f'A lista de impares é {lista_impares}')