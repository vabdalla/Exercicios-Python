# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
quer_continuar = 'S'
lista = []
dicionario = {}
contador_pessoas = 0
soma_idade = 0
lista_mulheres = []
dicionario_mulheres = {}
while quer_continuar == 'S':
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('[M/F]: ')).upper()
    while dicionario['sexo'] not in ['F', 'M']:
        print('ERRO! Por favor digite só M ou F')
        dicionario['sexo'] = str(input('[M/F]: ')).upper()
    dicionario['idade'] = int(input('Idade: '))
    soma_idade += dicionario['idade']
    quer_continuar = str(input('Quer continuar? [S / N]: ')).upper()
    while quer_continuar not in ['S', 'N']:
        print('ERRO! Por favor digite só S ou N')
        quer_continuar = str(input('Quer continuar? [S / N]: ')).upper()
    contador_pessoas += 1
    lista.append(dicionario.copy())
    if dicionario['sexo'] == 'F':
        lista_mulheres.append(dicionario.copy())
#pegando o valor da key 'nome'
nomes = [dicionario_mulheres['nome'] for dicionario_mulheres in lista_mulheres]

#media idade
media_idade = soma_idade/contador_pessoas
#extrair nome e idade apenas das pessoas com idade acima da média
pessoas_acima_da_media = [(dicionario.items())
                          for dicionario in lista if dicionario['idade'] > media_idade]
print(f'A) Ao todo temos {contador_pessoas} pessoas cadastradas')
print(f'B) A média da idade é de {media_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram:  {nomes}')
print(f'D) Pessoas acima da média: {pessoas_acima_da_media}')
