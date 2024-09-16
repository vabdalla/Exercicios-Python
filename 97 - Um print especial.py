#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(mensagem):
    tamanho = len(mensagem)+4
    print('~'*tamanho)
    print(mensagem.center(tamanho))
    print('~'*tamanho)


mensagem = 'Victor Abdalla'
escreva(mensagem)
mensagem = 'Curso de Python no Youtube'
escreva(mensagem)
mensagem = 'CeV'
escreva(mensagem)
