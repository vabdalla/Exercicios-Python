import time
resultado = 0
escolha = 0
while escolha != 5:
    primeiro_valor = int(input('Primeiro valor: '))
    segundo_valor = int(input('Segundo valor: '))
    print('=-='*10)
    print ('[ 1 ] SOMAR ')
    print ('[ 2 ] MULTIPLICAR ')
    print('[ 3 ] MAIOR ')
    print('[ 4 ] NOVOS NÚMEROS ')
    print('[ 5 ] SAIR DO PROGRAMA ')
    escolha = int(input('>>>>> Qual é sua opção? '))
    if escolha == 1:
        resultado = primeiro_valor+segundo_valor
        print(f'A soma entre {primeiro_valor} + {segundo_valor} = {resultado}')
    elif escolha == 2:
        resultado = primeiro_valor*segundo_valor
        print(f'A multiplicação entre {primeiro_valor} x {segundo_valor} = {resultado}')
    elif escolha == 3:
        resultado = primeiro_valor>segundo_valor
        if resultado == True:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {primeiro_valor}')
        else:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {segundo_valor}')
    elif escolha == 4:
        print('Informe os números novamente: ')
    elif escolha > 5:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
print('Finalizando...')
time.sleep(1)
print('=-='*10)
print('Fim do programa! Volte sempre!')

