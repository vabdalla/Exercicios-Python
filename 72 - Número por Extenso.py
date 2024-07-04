# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
# (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# escolha = int(input('Tente novamente Digite um numero entre 0 e 20: '))

while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <=20:
        print(f'Voce digitou o número {tupla[escolha]}')
        break
