# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dicionario = {}
lista = []
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Media de {dicionario["nome"]} '))
if dicionario["media"] >= 7:
    dicionario['situação'] = 'Aprovado'
elif dicionario['media'] < 5:
    dicionario['situação'] = 'Reprovado'
else:
    dicionario['situação'] = 'Recuperação'
print(dicionario)
print('-='*40)
for k,v in dicionario.items():
    print(f'{k} é igual a {v}')