import math
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjascente: '))
hip = math.sqrt((math.pow(catop,2)) + (math.pow(catad,2)))
print(f'A hipotenusa irá medir {hip}')