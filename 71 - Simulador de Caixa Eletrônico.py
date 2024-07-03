print('='*30, '\n     BANCO CEV     \n','='*30 )
valor_saque = int(input('Que valor voce quer sacar? R$'))
total_cedulas_cinquenta = valor_saque // 50
valor_saque = valor_saque - (total_cedulas_cinquenta*50)
total_cedulas_vinte = valor_saque // 20
valor_saque = valor_saque - (total_cedulas_vinte*20)
total_cedulas_dez = valor_saque // 10
valor_saque = valor_saque - (total_cedulas_dez*10)
total_cedulas_um = valor_saque // 1
valor_saque = valor_saque - (total_cedulas_um*1)
print(f'Total de {total_cedulas_cinquenta} cedulas de R$50')
print(f'Total de {total_cedulas_vinte} cedulas de R$20')
print(f'Total de {total_cedulas_dez} cedulas de R$10')
print(f'Total de {total_cedulas_um} cedulas de 1')

