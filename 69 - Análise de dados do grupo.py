print('-'*20,'\nCADASTRE UMA PESSOA: \n', '-'*20)
maior_de_idade = 0
quantidade_homens = 0
quantidade_mulheres_menos_vinte = 0
quer_continuar = 'S'
while quer_continuar == 'S':
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: [M / F] ')).upper()
    quer_continuar = str(input('Quer continuar? [S / N] ')).upper()
    print('-' * 20, '\nCADASTRE UMA PESSOA: \n', '-' * 20)
    if idade >= 18:
        maior_de_idade += 1

    if sexo == 'M':
        quantidade_homens += 1

    if sexo == 'F' and idade < 20:
        quantidade_mulheres_menos_vinte += 1
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maior_de_idade}')
print(f'Ao todo temos {quantidade_homens} homens cadastrados')
print(f'E temos {quantidade_mulheres_menos_vinte} mulheres com menos de 20 anos')