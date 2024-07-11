# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = 0
somador = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero != 999:
        somador+=numero
        contador += 1
print(f'Voce digitou {contador} numeros e a soma entre eles foi {somador}')
