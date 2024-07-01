import math

angulo = int(input('Digite o angulo: '))
seno = round(math.sin(math.radians(angulo)),2)
coss = round(math.cos(math.radians(angulo)),2)
tang = round(math.tan(math.radians(angulo)),2)
print(f'O angulo de {angulo} tem o SENO de {seno}')
print(f'O angulo de {angulo} tem o COSSENO de {coss}')
print(f'O angulo de {angulo} tem a TANGENTE de {tang}')