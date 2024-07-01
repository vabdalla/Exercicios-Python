l1 = int(input('Digite o lado 1: '))
l2 = int(input('Digite o lado 2: '))
l3 = int(input('Digite o lado 3: '))
lista = [l1,l2,l3]
lista.sort()
print (lista)
if lista[0]+lista[1] > lista[2]:
    print('Esse triangulo existe')
else:
    print('Esse triangulo não existe')