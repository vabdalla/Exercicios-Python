# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'Ec Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
posicao_chapecoense = times.index('Chapecoense')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 ultimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)})')
print(f'O Chapecoense está na {times.index('Chapecoense')+1} posição')
