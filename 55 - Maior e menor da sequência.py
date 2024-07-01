d = 1
m = 0
maiorpeso = 0
lista = []
for c in range(1,6):
    peso = float(input(f'Peso da {d}ª pessoa: '))
    d+=1
    lista.append(peso)
    if peso>maiorpeso:
        maiorpeso=peso
menorpeso = min(lista)

print(f'O maior peso lido foi de {maiorpeso} ')
print(f'O menor peso lido foi de {menorpeso} ')