# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
quer_continuar = 'sim'
contador = 0
while quer_continuar != 'N':
    valor_digitado = int(input('Digite um valor: '))
    lista.append(valor_digitado)
    contador += 1
    quer_continuar = input('Quer continuar? [ S / N ]').upper()
print(f'Voce digitou {contador} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO foi encontrado na lista')