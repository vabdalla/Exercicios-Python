# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
import math
quer_continuar = str
numero = 0
lista = []
contador = 0
while quer_continuar != 'N':
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    contador+=1
    quer_continuar = input('Quer continuar? [ S / N ]: ') .upper()
total = sum(lista)
print(f'Voce digitou {contador} numeros e a média foi {total / len(lista)}')
print(f'O maior valor digitado foi {max(lista)} e o menor foi {min(lista)}')
