num = int(input('Digite um numero: '))
cont = 0
lista = []
lista2 = []
lista_nova = []
#1 a ate onde eu digitar
for c in range(1,num+1):
    lista2.append(c)
    print(c, end=' ')

for match in lista2:
    lista_nova.append(lista)

for d in range(1,num+1):
    if num % d == 0:
        cont+=1
        lista.insert(d,d)
print(' ')
print(f'O numero {num} foi divisível {len(lista)} vezes')
if len(lista)>2:
    print('E por isso ele NÃO É PRIMO')
else:
    print('E por isso ele É PRIMO')

