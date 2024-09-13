# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dicionario = {}
lista_gols = []
dicionario['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dicionario['nome']} jogou? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c + 1}: '))
    lista_gols.append(gols)
    dicionario['gols'] = lista_gols
dicionario['total'] = sum(lista_gols)
print('-='*30)
print(dicionario)
print('-='*30)
for k,v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dicionario['nome']} jogou {partidas} partidas')
for c in range(partidas):
    print(f'Na partida {c}, fez {dicionario['gols'][c]} gols.')
print(f'Foi um total de {dicionario['total']} gols.')