num = int(input('Escreva um numero: '))
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
base = int(input('Escolha a base de conversão: '))
if base == 1:
    print(f'O numero {num} convertido em binário fica {bin(num)}')
    if base==2:
        print(f'O numero {num} convertido em octal fica {oct(num)}')
else:
        print(f'O numero {num} convertido em hexadecimal fica {hex(num)}')