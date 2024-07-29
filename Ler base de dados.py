with open("id_venda e valor.txt","r") as arquivo:
    texto = arquivo.read()
valor_separado = []

#transformando cada linha em uma lista
linha_separada = texto.split("\n")
for c in linha_separada:
    valor_separado.append(c.split(";"))
soma = 0

# excluir primeira linha
valor_separado = valor_separado[1:]

# pegando o segundo elemento (valor) e somando na variavel soma
for d in valor_separado:
    valor = int(d[1])
    soma += valor
dicionario = {'ID de venda', 'Valor'}
print(linha_separada)
print(valor_separado)
print(soma)

