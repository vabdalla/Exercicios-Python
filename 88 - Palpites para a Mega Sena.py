# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
import random
quantos_jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantos_jogos} JOGOS -=-=-=')
lista_principal = []
lista_aleatorio = []
for c in range(0,quantos_jogos):
    lista_aleatorio = random.sample(range(0, 61),6)
    lista_principal.append(lista_aleatorio[:])
for v in range (0,len(lista_principal)):
    lista_principal[v].sort()
    print(f'Jogo {v+1}: {lista_principal[v]}')
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')