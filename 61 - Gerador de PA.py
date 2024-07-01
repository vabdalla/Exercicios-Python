print('Gerador de PA')
print('-='*10)
resultado = 0
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
resultado = primeiro_termo+razao
d = 0
c = primeiro_termo
while d < 10:
    print(c, ' -> ', end='')
    c +=razao
    d+=1

    if d == 10:
        print('FIM')