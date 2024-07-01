vcasa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
finan = int(input('Quantos anos de financiamento? '))
presmensal = vcasa/(finan*12)
apouneg = presmensal<sal*30/100

print(f'Para pegar uma casa de {vcasa} em {finan} anos a prestação sera de {presmensal}')
print(apouneg)
if apouneg == True:
    print(f'Seu empréstimo foi APROVADO')
else:
    print('Seu empréstimo foi NEGADO')