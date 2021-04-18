nome = input('Diga o seu nome:').strip()
minusculo = nome.lower()
teste = 'silva' in minusculo

if teste == True:
    print('Você tem a palavra silva no nome')

else:
    print('Você não tem a palavra silva no nome')