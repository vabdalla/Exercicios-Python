palavra = str(input('Digite uma palavra: '))
d = len(palavra)-1
for c in range(0,d+1):
    if palavra[c] == palavra[d]:
        c+=1
        d-=1
        if c==d:
            print('É PALINDROMO')
            break
else:
    print('NÃO É PALINDROMO')

################## OUTRO MODO DE FAZER ##################

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