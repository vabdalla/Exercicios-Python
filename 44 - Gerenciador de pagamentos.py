print('==========LOJAS ABDALLA==========')
preco = float(input('Preço das Compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista no dinheiro/pix')
print('[ 2 ] a vista no CARTAO')
print('[ 3 ] 2x no CARTAO')
print('[ 4 ] 3x ou mais no CARTAO')
opcao = int(input('Qual é a opção? '))
novo = float
if opcao==1:
    novo = preco - (preco*10/100)
elif opcao==2:
    novo = preco - (preco*5/100)
elif opcao==3:
    novo = preco
elif opcao==4:
    novo = preco + (preco*20/100)
else:
    print('OPÇÃO INVÁLIDA')
print(f'Sua compra de {preco} vai custar {novo} no final')