qnts_valores = contador = numeros = 0

while True:
    numeros = int(input('Digite um numero: '))
    if numeros == 999:
        break
    contador += numeros
    qnts_valores += 1
print(f'A soma dos {qnts_valores} valores vale {contador}')