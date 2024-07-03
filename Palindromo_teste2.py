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