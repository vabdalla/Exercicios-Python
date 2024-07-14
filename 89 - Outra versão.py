ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([[nome], [nota1,nota2], [media]])
    quer_continuar = str(input('Quer continuar? [ S / N ] ')).upper()
    if quer_continuar == 'N':
        break
    print('-='*30)
    print(f'{'No.':<4} {'NOME':<10}{"MEDIA":>8}')
    print('-'*26)
    for i, a in enumerate(ficha):
        print(f'{i}{a[0]}{a[2]}')
    while True:
        print('-'*35)
        opc = int(input('Mostrar notas de qual aluno? (999 INTERROMPE): '))
        if opc == 999:
            print('Finalizando...')
            break
        if opc <= len(ficha):
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE')


