resultado = 0
numero = int(input('Digite um número para \ncalcular seu Fatorial: '))
resultado2= numero
print(f'Calculando {numero}! =  ', end='')
for c in range(numero,2, -1):
    resultado = resultado2*(c-1)
    resultado2 = resultado
print(resultado2)
