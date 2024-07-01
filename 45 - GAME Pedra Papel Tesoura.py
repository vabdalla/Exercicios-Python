import random
computador = [0, 1, 2]
jogo = ['Pedra','Papel','Tesoura' ]
jogadacomputador = random.choice(computador)
resultado = str
print('SUAS OPÇÕES: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogadauser = int(input('Qual a sua jogada? '))
if jogadacomputador!=jogadauser:
    if jogadacomputador==0 and jogadauser==1:
        resultado = 'JOGADOR VENCE'
    elif jogadacomputador==0 and jogadauser==2:
        resultado = 'COMPUTADOR VENCE'
    elif jogadacomputador==1 and jogadauser==0:
        resultado = 'COMPUTADOR VENCE'
    elif jogadacomputador==1 and jogadauser==2:
        resultado = 'JOGADOR VENCE'
else:
    resultado = 'EMPATE'

print('JO')
print('KEN')
print('PÔ!!!')
print('-='*20)
print(f'Computador jogou {jogo[jogadacomputador]}')
print(f'Jogador jogou {jogo[jogadauser]}')
print('-='*20)
print(resultado)





