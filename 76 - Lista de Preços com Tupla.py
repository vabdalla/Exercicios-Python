# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.
print('='*30)
print(' '*5,'Listagem de preços', ' '*5)
print('='*30)
tupla = ('Lapis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90','Estojo', '25.00', 'Transferidor', '4.20',
         'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34;90')
tamanho_tupla = len(tupla)
for c in range(0,tamanho_tupla,2):
    print(tupla[c], '.'*10,f'R${tupla[c+1]} ')
#index do lapis +1 (valor)