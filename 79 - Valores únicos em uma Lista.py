lista_unica = []
sim_ou_nao = str
c = 0
while True:
    valor_digitado = int(input('Digite um número: '))
    print('Valor adicionado com sucesso...')
    if valor_digitado not in lista_unica:
        lista_unica.append(valor_digitado)
    else:
        print('Valor duplicado! Não vou adicionar')
    sim_ou_nao = input('Quer continuar? [ S / N ]').upper()
    c+=1
    if sim_ou_nao == 'N':
        break
print(sorted(lista_unica))