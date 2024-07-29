import random
dicionario = {}
print('Valores sorteados')
for d in range (1,5):
    dicionario[f'Jogador{d}'] = random.randint(1,6)
print(dicionario)
maior = 0
lista = []
print('-='*40)
print('  == RANKING DOS JOGADORES ==  ')
for k, v in dicionario.items():
    if k == 'Jogador1':
        maior = v
    if v >= maior:
        maior = v
        lista = v,k
# dicionario['Jogador'] = sorted(dicionario.values(), reverse=True)
print(sorted(dicionario.values(), reverse=True))
print(maior)
print(lista)