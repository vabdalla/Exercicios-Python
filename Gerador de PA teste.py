print('Gerador de PA\n', '-='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
contador_while = 0
c = primeiro_termo
print(c, end='')
while contador_while < 9:
    c+=razao
    contador_while+=1
    print(' -> ', c, end='')
    if contador_while == 9:
        print(' -> Pausa')
termos_total = 10
termos_amais = int(input('Quantos termos a mais? '))
d = 0
while termos_amais != 0:
    while d < termos_amais:
        c+=razao
        d += 1
        termos_total+=termos_amais
        print(c, ' -> ', end='')
        if d == termos_amais:
            print('Pausa')


print(f'Progressão finalizada com {termos_total}')