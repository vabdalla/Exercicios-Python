frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if inverso==junto:
    print('Temos um palíndromo')
else:
    print('Não é palindromo')