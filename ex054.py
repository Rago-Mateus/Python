import datetime
atual = datetime.date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade>=21:
        totalmaior=totalmaior+1
    else:
        totalmenor=totalmenor+1

print('Nós tivemos {} maiores de idade e {} pessoas menores de idade.'.format(totalmaior,totalmenor))
