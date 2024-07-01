#"escaleno, quando todos os lados possuem medidas diferentes;
# isósceles, quando existem dois lados que possuem mesma medida;
# equilátero, quando todos os lados são congruentes."

primeiro = int(input('Primeiro segmento: '))
segundo = int(input('Segundo segmento: '))
terceiro = int(input('Terceiro segmento: '))
triangulo = str

if primeiro<segundo+terceiro and segundo<terceiro+primeiro and terceiro<segundo+primeiro:
    print('Os segmentos acima PODEM FORMAR um triangulo')
    if primeiro == segundo and primeiro == terceiro:
        triangulo = 'EQUILATERO'
    elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
        triangulo = 'ESCALENO'
    else:
        triangulo = 'ISÓCELES'
    print(f'Os segmentos acima podem formar um triangulo {triangulo}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')


