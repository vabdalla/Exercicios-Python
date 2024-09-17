import random

def maior(* num):
    maior_num = 0
    #   Gera 6 linhas
    for c in range (0,6):
    #   Gera de 0 a 6 numeros aleatorios
        for d in range(0,random.randint(0,7)):
            aleatorio = random.randint(0, 10)
    #       Encontra o maior
            if aleatorio > maior_num:
                maior_num=aleatorio

            print(aleatorio, end= ' ')
        print(f'Foram informados {d+1} valores ao todo')
        print(f'O maior valor foi {maior_num}')
        maior_num = 0
maior()
