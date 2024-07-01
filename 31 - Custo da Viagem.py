distancia = float(input('Digite a distancia percorrida em KM: '))
if distancia<=200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print(f'O valor a ser pago será de R${preco}')
