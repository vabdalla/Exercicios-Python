n = 0
cont = 0
for c in range(1,500):
    if c%2 != 0:
        if c%3 == 0:
            n=n+c
            cont+=1
print(f'A soma de todos os {cont} é igual a {n}')