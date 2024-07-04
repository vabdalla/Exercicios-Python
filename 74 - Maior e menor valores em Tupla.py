# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
# que estão na tupla.
import random
numeros_aleatórios = random.sample(range(1, 11), 5)
print(f'Os valores sorteados foram: {numeros_aleatórios}')
print(f'O maior valor sorteado foi {max(numeros_aleatórios)}')
print(f'O menor valor sorteado foi {min(numeros_aleatórios)}')