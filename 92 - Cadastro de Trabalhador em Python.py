# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
# se aposentar.
import datetime
dicionario = {}
dicionario['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
#data atual
data = datetime.datetime.today()
#ano atual
ano_atual = data.year
dicionario['idade'] = ano_atual - ano_nasc
dicionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dicionario['ctps'] != 0:
    dicionario['ano_contratacao'] = int(input('Ano de Contratação: '))
    aposentadoria = 55 - (ano_atual - dicionario['ano_contratacao'])
    dicionario['salario'] = float(input('Salário: '))
    dicionario['aposentadoria'] = aposentadoria
print('-='*30)
for k,v in dicionario.items():
    print(f'{k} tem o valor {v}')

