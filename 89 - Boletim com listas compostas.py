# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista_temp = []
lista_principal = []
lista_numeros = []
quer_continuar = str
lista_teste = []
media = []
while True:
    lista_temp.append(str(input('Nome: ')))
    lista_temp.append(float(input('Nota 1: ')))
    lista_numeros.append(lista_temp[1])
    lista_temp.append(float(input('Nota 2: ')))
    lista_numeros.append(lista_temp[2])
    lista_teste.append(lista_numeros[:])
    lista_principal.append(lista_temp[:])
    lista_temp.clear()
    lista_numeros.clear()

    quer_continuar = input('Quer continuar? [ S / N ] ').upper()
    if quer_continuar == 'N':
        break
for v in range (0,len(lista_principal)):
    media.append(sum(lista_teste[v])/2)
print('-='*40)
print('No. NOME       MEDIA' )
print('-='*40)
for cont in range(0, len(lista_teste)):
    print(f'{cont}   {lista_principal[cont][0]}       {media[cont]}')
print('-='*40)
qual_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
while True:
    print(f'Notas de {lista_principal[qual_aluno][0]} são {lista_principal[qual_aluno][1:]}')
    qual_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if qual_aluno == 999:
        break
print('FINALIZANDO')
