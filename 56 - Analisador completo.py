nome_lista = []
idade_lista = []
idade_lista_homens = []
#usar o count
sexoM=0
sexoF=0
sexo_lista = []
lista_mulheres_menosvinte = []
contador = 0

#adicionando nome,idade,em uma lista, contagem de M e F
for c in range(1,5):
    print(f'-----{c}ª PESSOA -----')
    nome = input('Nome: ')
    nome_lista.append(nome)

    idade = int(input('Idade: '))
    idade_lista.append(idade)
    sexo = input('Sexo [M/F]: ').upper()
    sexo_lista.append(sexo)
    if sexo=='M':
        sexoM+=1
        idade_lista_homens.append(idade)

    else:
        sexoF=+1
        idade_lista_homens.append(0)

    if sexo == 'F' and idade < 20:
        lista_mulheres_menosvinte.append(idade)
    else:
        lista_mulheres_menosvinte.append(0)

#media de idade
media = sum(idade_lista)/4

#pegando maior idade de homem
maior_idade_homem = idade_lista_homens.index(max(idade_lista_homens))

#linkando com a posição do nome
nome_do_homem_mais_velho = nome_lista[maior_idade_homem]

#pegando quantas mulheres tem menos de 20 anos
for d in range(0,len(lista_mulheres_menosvinte)):
    if lista_mulheres_menosvinte[d] == 0:
        contador+=1
print(f'A media de idade do grupo é de {media}')
print(f'Nome do homem mais velho: {nome_do_homem_mais_velho} ')
print(f'Ao todo são {contador} mulheres com menos de 20 anos')