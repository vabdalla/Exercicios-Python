import math
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Cateto Adjascente: '))
hip = math.sqrt((math.pow(catop,2)) + (math.pow(catad,2)))
print(f'A hipotenusa irá medir: {hip}')