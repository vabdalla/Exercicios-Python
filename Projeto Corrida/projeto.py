km = int(input('quantos km voce irá correr? '))
blocos = int(input('Quantos blocos voce quer dividir? '))
pace = []
min_seg = 0
for c in range(blocos):
    minutos = int(input(f'Minutos do bloco {c+1} '))*60
    segundos = int(input(f'Segundos do bloco {c+1} '))
    min_seg = minutos+segundos
    pace.append(min_seg)
soma = (sum(pace)/blocos)/60
print(f'Pace: {soma}')
resto = 0
if km%blocos != 0:
    resto = km%blocos
print(f'Resto: {resto}')