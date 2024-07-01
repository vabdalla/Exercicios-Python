anonasc = int(input('Ano de nascimento: '))
aniversario = (anonasc-2024)*-1
alistamento = 18-aniversario
print(f'Quem nasceu em {anonasc} tem {aniversario} anos em 2024')
if alistamento<0:
    print(f'Seu alistamento foi no ano de {anonasc+18}')
elif alistamento==0:
    print('Voce deve se alistar IMEDIATAMENTE')
else:
    print(f'Ainda faltam {alistamento} anos para o alistamento')