'''homem = mulher = 0
sexo = W
while sexo =! M:
    sexo = str(input('Qual o seu sexo?'))
    if sexo ==  'M':
        homem = homem +1
    elif sexo == 'F':
        mulher = mulher +1
    else:
        print('Digite ou M ou F! Não são permitidos outras letras')
print("o número de mulheres é {}".format(mulher))
print("o número de homens é {}".format(homem))'''
sexo = str(input('Qual o seu sexo [M/F]?')).lower().strip()[0]
while sexo not in 'mf':
    sexo = str(input('Dados inválidos! Digite seu sexo por favor:')).lower().strip()
print('Sexo {} registrado com sucesso!'.format(sexo))

