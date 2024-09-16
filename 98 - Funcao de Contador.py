# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador (inicio, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    if inicio>fim and passo >= 0:
        passo=passo*-1
        fim=fim-2
    else:
        fim = fim - 2

    for c in range(inicio,fim+1, passo):
        print(c,  end=' ')
        # sleep(0.25)

    print('FIM!')
    print('-=' * 20)


print('Contagem de 1 até 10 de 1 em 1')
inicio = 1
fim = 10
passo = 1
contador(inicio,fim,passo)
print('Contagem de 10 até 0 de 2 em 2')
inicio = 10
fim = -2
passo = -2
contador(inicio,fim,passo)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim, passo)