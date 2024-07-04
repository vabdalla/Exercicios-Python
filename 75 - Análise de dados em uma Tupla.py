# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
        int(input('Digite um número: ')))
print (numeros)
contador_de_nove = 0
numeros_pares = []
for c in numeros:
    if c == 9:
        contador_de_nove+=1
    if c % 2 == 0:
        numeros_pares.append(c)
print(f'O 9 aparece {contador_de_nove} vezes')
if 3 in numeros:
    posicao_do_tres = numeros.index(3)
    print(f'O valor 3 aparece na posicao {posicao_do_tres} ')

print(numeros_pares)

