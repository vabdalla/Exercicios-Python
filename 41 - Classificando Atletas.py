anonasc = int(input('Ano de nascimento: '))
idade = 2024-anonasc
classe = str
if idade<=9:
    classe = 'MIRIM'
elif idade>9 and idade<=14:
    classe = 'INFANTIL'
elif idade>14 and idade<=19:
    classe = 'JUNIOR'
elif idade>19 and idade<=25:
    classe = 'Senior'
else:
    classe = 'Master'
print(f'O atleta tem {idade} anos')
print(f'Classificação: {classe}')