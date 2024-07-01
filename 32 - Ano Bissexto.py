ano = str(input('Digite o ano: '))
#para pegar os dois ultimos numeros da string
ultimosdois = ano[-2:]
#converte string em int para realizar operações
numeros = int(ultimosdois)
if numeros%4==0:
    print('Esse ano é bissexto')
else:
    print('Esse ano NÃO é bissexto')
