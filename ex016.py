numero = float(input(('Diga um número real (de preferência com casas decimais):')))
inteira = int(numero)
print('Você disse o número {}, sendo que sua parte inteira é {}.'.format(numero,inteira))


import math
print('O valor digitado é {}, sendo que sua porção inteira é {}.'.format(numero,math.trunc(numero)))
