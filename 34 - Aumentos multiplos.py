sal = int(input('Digite seu salário: R$'))
if sal > 1250:
    aumento = sal+(sal*0.1)
else:
    aumento = sal+(sal*0.15)
print(f'O seu salário de {sal} com aumento passa a ser {aumento}')