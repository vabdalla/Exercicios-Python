valor_digitado = contador = 1
outro_contador = 0
while contador <=11:
    valor_digitado = int(input('Digite um número: '))
    if valor_digitado < 0:
        break
    outro_contador = 0
    while outro_contador <=10:
        print(f'{valor_digitado} * {outro_contador} = {valor_digitado * outro_contador}')
        outro_contador += 1
