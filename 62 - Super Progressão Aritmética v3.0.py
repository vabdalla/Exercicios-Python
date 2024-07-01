print('Gerador de PA')
print('-='*10)
resultado = 0
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
resultado = primeiro_termo+razao
d = 0
c = primeiro_termo
termos_amais = -1
while termos_amais != 0:
    while d < 10:
        print(c, ' -> ', end='')
        c +=razao
        d+=1

        if d == 10:
            print('PAUSA')
    termos_amais = int(input('Quantos termos a mais voce quer mostrar? '))
    d=0
    while d < termos_amais:
        print(c, ' -> ', end='')
        c +=razao
        d+=1

        if d == termos_amais:
            print('PAUSA')