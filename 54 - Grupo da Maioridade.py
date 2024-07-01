import datetime
c = 0
cont = 0
d = 0
hoje = datetime.date.today().year
print(hoje)
for pessoas in range(1,8):
    c +=1
    pessoas = int(input(f'Em que ano a {c} pessoa nasceu? '))
    print(pessoas)

    if pessoas < hoje-18:
        cont+=1
    else:
        d+=1
print(f'Ao todo tivemos {cont} pessoas maiores de idade')
print(f'E também tivemos {d} pessoas menores de idade')