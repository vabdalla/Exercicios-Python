velocidade = int(input('Digite a velocidade do carro: '))
if velocidade>80:
    print('Voce foi multado!')
    print(f'O valor da multa será R${(velocidade-80)*7}')
else:
    print('Voce NÃO foi multado!')