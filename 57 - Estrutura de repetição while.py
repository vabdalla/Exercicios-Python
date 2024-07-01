sexo = input('Digite seu sexo : [M/F] ') .upper()
while sexo != 'M' and sexo!='F':
    print('Dados inválidos, digite novamente: ')
    sexo = input('Digite seu sexo : [M/F] ') .upper()
print(f'Sexo {sexo} registrado com sucesso')

