peso = float(input('Qual seu peso? (KG)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso/(altura*altura)
print(f'Seu IMC é de: {imc:.1f}')
if imc<18.5:
    print('Voce está ABAIXO do peso ideal')
elif imc>=18.5 and imc<25:
    print('Voce está no peso ideal PARABÉNS')
elif imc>=25 and imc<30:
    print('Voce está com SOBREPESO')
elif imc>=30 and imc<40:
    print('Voce está com OBESIDADE')
else:
    print('Voce está com OBESIDADE MÓRBIDA')