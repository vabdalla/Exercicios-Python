# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
sequencia = [0,1]
quantos_termos = int(input('Quantos termos voce quer mostrar? '))
print('~'*30)
for c in range(2,quantos_termos):
    sequencia.append(sequencia[c-1]+sequencia[c-2])
print(sequencia, 'FIM', end='')