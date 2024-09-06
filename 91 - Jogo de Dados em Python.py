# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
import time

dicionario = {}
lista = []
for c in range(1,5):
    numero = random.randint(1,6)
    dicionario[f'Jogador{c}'] = numero
    print(f'O jogador{c} tirou: {numero}')
valores_ordenados = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
dicionario_valores_ordenados = dict(valores_ordenados)
print('RANKING DOS JOGADORES: ')
for k,v in dicionario_valores_ordenados.items():
    print(f'Jogador {k} tirou {v} no dado')
    time.sleep(1)