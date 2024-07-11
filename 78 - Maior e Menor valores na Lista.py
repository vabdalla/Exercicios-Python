# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
numero = str
maior_valor = 0
posicao_maior_valor = []
posicao_menor_valor = []
d = 1
for c in range(0,5):
    numero = int(input(f'Digite um numero para a posição {c}: '))
#insere na lista
    lista.append(numero)
#verifica maior valor
    if numero >= maior_valor:
        maior_valor=numero
    
menor_valor = min(lista)
#varre lista procurando a posição do maior valor
#contador vai de 0 a 4 e "v" é itens da lista[contador]
for contador, v in enumerate(lista):
    if v==maior_valor:
        posicao_maior_valor.append(contador)
    if v==menor_valor:
        posicao_menor_valor.append(contador)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior_valor} nas posições {posicao_maior_valor}')
print(f'O menor valor digitado foi {menor_valor} nas posições {posicao_menor_valor}')
