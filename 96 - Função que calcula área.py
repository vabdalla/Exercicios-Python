# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area (a,b):
    print(f'A área do retângulo é igual a: {b*a}m²')
largura = float(input('Qual a largura? (m) '))
altura = float(input('Qual a altura? (m) '))
area(altura,largura)
