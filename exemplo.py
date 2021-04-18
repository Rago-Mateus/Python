maximo = 0
minimo = 10000000000000
for c in range(0,6):
    peso = int(input('Qual o peso da pessoa?'))
    if peso > maximo:
        maximo = peso
    if peso < minimo:
        minimo = peso
print('O peso máximo encontrado foi {}'.format(maximo))
print('O peso mínimo encontrato é {}'.format(minimo))