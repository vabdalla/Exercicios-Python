# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário
# se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos_amais = 0
contador_de_termos = 10
print(f'{primeiro_termo} -> ', end='')
for c in range(primeiro_termo, 9):
    primeiro_termo+=razao
    print(f'{primeiro_termo} -> ', end='')
    if c==8:
        print('PAUSA ')
termos_amais = int(input('Quantos termos voce quer mostrar a mais? '))
contador_de_termos+=termos_amais
while termos_amais != 0:
    for d in range(0,termos_amais):
        primeiro_termo+=razao
        print(f'{primeiro_termo} -> ', end='')
        if d == termos_amais-1:
            print('PAUSA ')
    termos_amais = int(input('\nQuantos termos voce quer mostrar a mais? '))
    contador_de_termos += termos_amais
print(f'A progressão foi finalizada com {contador_de_termos} termos mostrados')