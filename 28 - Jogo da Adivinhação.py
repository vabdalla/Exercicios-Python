import random
numuser = int(input('Em que numero eu pensei? '))
print('-=-'*20)
print('PROCESSANDO')
num = random.randint(1,6)
print(f'VOCE PENSOU EM {numuser} ')
print(f'EU PENSEI EM {num} ')
if numuser == num:
    print(f'VOCE GANHOU POIS PENSEI EM {num} e voce em {numuser}')
else:
    print(f'EU GANHEI POIS PENSEI EM {num} e voce em {numuser}')
