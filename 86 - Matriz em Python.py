matriz = [[],[],[]]
d = 0
for d in range (0,3):
    matriz[0].append(int(input(f'Digite um valor para {d,c} ')))
d = 1
for b in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para {d, b} ')))
d = 2
for v in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para {d, v} ')))
print(matriz[0])
print(matriz[1])
print(matriz[2])