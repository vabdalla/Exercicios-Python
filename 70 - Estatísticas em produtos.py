print('='*30, '\n     LOJA SUPER BARATAO     \n','='*30 )
quer_continuar = 'S'
contador_preco = 0
mais_que_mil = 0
produto_mais_barato = str
preco_produto_mais_barato = 0
while quer_continuar == 'S':
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    preco_produto_mais_barato = preco
    produto_mais_barato = nome_produto
    if preco_produto_mais_barato > preco:
        preco_produto_mais_barato = preco
        produto_mais_barato = nome_produto
    if preco >= 1000:
        mais_que_mil+=1
    contador_preco += preco
    quer_continuar = str(input('Quer continuar? [S / N]')) .upper()

print('='*30, '\n     FIM DO PROGRAMA     \n','='*30 )
print(f'O total da compra foi de R${contador_preco}')
print(f'Temos {mais_que_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produto_mais_barato} que custou {preco_produto_mais_barato}')