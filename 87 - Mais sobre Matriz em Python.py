# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
lista_pares = []
lista_terceira_coluna = []
cont = 0
lista_segunda_linha = []
for d in range (0,3):
    for c in range(0,3):
        matriz[d][c] = int(input(f'Digite um valor para [{d}, {c}]: '))
for d in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[d][c]}]', end='')
    print()
for d in range(0, 3):
    for c in range(0,3):
        if matriz[d][c] % 2 == 0:
            lista_pares.append(matriz[d][c])
        if c == 2:
            lista_terceira_coluna.append(matriz[d][c])
        if d == 1:
            lista_segunda_linha.append(matriz[d][c])
soma_pares = sum(lista_pares)
soma_terceira_coluna = sum(lista_terceira_coluna)
maximo = max(lista_segunda_linha)
print(f'Lista pares: {lista_pares}')
print(f'A soma dos valores pares: {soma_pares}')
print(f'Lista terceira coluna {lista_terceira_coluna}')
print(f'A soma dos valores da terceira coluna {soma_terceira_coluna}')
print(f'Lista segunda linha: {lista_segunda_linha}')
print(f'O maior valor da segunda linha é: {maximo}')