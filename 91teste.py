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