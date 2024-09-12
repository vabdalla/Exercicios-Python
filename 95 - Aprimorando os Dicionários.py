# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista_gols = []
lista_times = []
quer_continuar = str
dicionario_jogadores = {}

while True:
    c = 0

    dicionario_jogadores['nome'] = str(input('Nome do jogador: '))
    numero_partidas = int(input(f'Quantas partidas {dicionario_jogadores['nome']} jogou? '))
    for c in range (numero_partidas):
        gols = int(input(f'Quantos gols na partida {c+1}: '))
        lista_gols.append(gols)
    dicionario_jogadores['gols'] = lista_gols
    quer_continuar = str(input('Quer continuar? [S / N] ')).upper()
    lista_times.append(dicionario_jogadores)
    if quer_continuar == 'N':
        break
print(lista_times)