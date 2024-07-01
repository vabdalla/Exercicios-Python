primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira+segunda)/2
print(f'Tirando {primeira} e {segunda}, a média do aluno é {media:.1f}')
if media<5:
    print('O aluno está REPROVADO')
elif media >=5 and media<=6.9:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')