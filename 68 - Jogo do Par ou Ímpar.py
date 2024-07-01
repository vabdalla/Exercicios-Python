import random
print('-='*20, '\n Vamos jogar par ou impar\n', '-='*20)
valor_digitado = int(input('Digite um valor: '))
valor_computador = random.randint(1,10)
soma = valor_computador+valor_digitado
parouimparuser = input('Par ou Impar: [P/I]') .upper()
resultado = str
vitoria = str
while vitoria != 'Voce PERDEU':
    if soma % 2 != 0:
        resultado = 'IMPAR'
    else:
        resultado = 'PAR'
    if parouimparuser == 'P' and resultado == 'PAR':
        vitoria = 'Voce Ganhou'
    elif parouimparuser == 'I' and resultado == 'IMPAR':
        vitoria = 'Voce Ganhou'
    else:
        vitoria = 'Voce PERDEU'
        print(vitoria)
print(f'Voce jogou {valor_digitado} e o computador {valor_computador}. Total de {soma}: DEU {resultado}')
print(vitoria)

