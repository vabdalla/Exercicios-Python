import random
print('-='*20, '\n Vamos jogar par ou impar\n', '-='*20)
valor_digitado = int
valor_computador = int
soma = int
parouimparuser = str
resultado = str
vitoria = str
contador_vitorias = 0
contador_derrotas = 0
while contador_derrotas<1:
    valor_digitado = int(input('Digite um valor: '))
    parouimparuser = input('Par ou Impar: [P/I] ').upper()
    valor_computador = random.randint(1, 5)
    soma = valor_computador + valor_digitado
    if soma % 2 != 0:
        resultado = 'IMPAR'
    else:
        resultado = 'PAR'
    if parouimparuser == 'P' and resultado == 'PAR':
        vitoria = 'Voce Ganhou'
        contador_vitorias += 1
    elif parouimparuser == 'I' and resultado == 'IMPAR':
        vitoria = 'Voce Ganhou'
        contador_vitorias += 1
    else:
        vitoria = 'Voce PERDEU'
        contador_derrotas += 1
    print(f'Voce jogou {valor_digitado} e o computador {valor_computador}. Total de {soma}: DEU {resultado}')
    if contador_vitorias > 0:
        print(vitoria)
        print('VAMOS JOGAR NOVAMENTE...\n', '=-' * 10)
print(vitoria)
print('=-'*10)
print(f'GAME OVER! Voce venceu {contador_vitorias} vezes')
