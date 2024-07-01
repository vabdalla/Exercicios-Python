n = 1
cont_par = 0
cont_impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            cont_par+=1
        else:
            cont_impar+=1
print(f'Sao {cont_par} numeros pares e {cont_impar} numeros ímpares')
print('FIM')
