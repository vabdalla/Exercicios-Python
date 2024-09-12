dicionario = {}
dicionario['nome'] = str(input('Nome do aluno: '))
dicionario['media'] = float(input(f'Media de {dicionario["nome"]}: '))
if dicionario['media'] < 5:
    dicionario['situação']='REPROVADO'
else:
    dicionario['situação'] = 'APROVADO'
for k,v in dicionario.items():
    print(f'{k} é igual a {v}')