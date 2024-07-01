print('Digite 3 numeros: ')
num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))
num3 = int(input('Digite o 3º numero: '))
if num1>num2:
   if num1>num3:
       print(f'O maior número foi {num1}')
else:
    if num2 > num3:
        print(f'O maior número foi {num2}')
    else:
        print(f'O maior número foi {num3}')