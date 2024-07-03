#for c in range(1,10):
#    passo
#pega

#COMANDO PARA PULAR
#   for c in range(1,3):
#       passo
#       pula
#   passo
#   pega
#SE DENTRO DO FOR
#   for c in range(0,3):
#        if moeda
#           pega
#        passo
#        pula
#   passo
#   pega

#for c in range(0,6):
#    print('Oi')
#print('FIM')

#CONTANDO PRA TRAS - esse -1 é a iteração
#    for c in range(7,-1,-1):
#       print(c)

#i = int(input('Digite o inicio: '))
#f = int(input('Digite o final: '))
#p = int(input('Digite o passo: '))
#for c in range(i,f,p):
#    print(c)
#print('FIM')
s = 0
for c in range(0,3):
    n = int(input('Digite um numero: '))
    s += n
print(f'O somatório de todos os valores é igual a {s}')