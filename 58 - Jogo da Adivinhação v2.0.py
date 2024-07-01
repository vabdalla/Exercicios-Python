import random

print('Sou seu computador... ')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que voce consegue adivinhar qual foi? ')
numero_user = int(input('Qual é seu palpite? '))
numero_computador = random.randint(0,10)
while numero_user != numero_computador:
    print('Você ERROU')
    print(f'Eu pensei no numero {numero_computador} e voce chutou {numero_user}')
    print('TENTE NOVAMENTE')
    numero_user = int(input('Qual é seu palpite? '))
    numero_computador = random.randint(0, 10)
print('VOCE ACERTOU!')
print(f'Eu pensei no numero {numero_computador} e voce chutou {numero_user}')
