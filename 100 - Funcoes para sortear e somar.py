# Exercício Python 100: Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
import random
lista = []

def sorteia():
    for c in range (5):
        aleatorio = random.randint(0,10)
        lista.append(aleatorio)


def somaPar():
    soma_pares = 0
    for d in lista:
        if d % 2 == 0:
            soma_pares += d
    return soma_pares

sorteia()
soma_pares = somaPar()
print(f'Sorteando 5 valores da lista: {lista}')
print(f'Somando valores pares: {soma_pares}')