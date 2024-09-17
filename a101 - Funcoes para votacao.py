# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
# uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime

def voto(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        status = 'NEGADO'
    elif idade >= 16 and idade < 18:
        status = 'OPCIONAL'
    else:
        status = 'OBRIGATORIO'
    return status,idade
ano_nascimento = int(input('Digite seu ano de nascimento: '))
status_voto, idade = voto(ano_nascimento)
print(f'Com {idade} anos: VOTO {voto(ano_nascimento)[0]}')