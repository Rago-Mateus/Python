import cmath
import math
cateto1 = float(input(('Diga o comprimento do primeito cateto de um triângulo:')))
cateto2 = float(input('Agora o comprimento do segundo cateto:'))
hipotenusa = math.hypot(cateto1,cateto2)
print( 'Sendo um cateto {} e o outro {}, o valor de sua hipotenusa é {}'.format(cateto1,cateto2,hipotenusa))

catetoq1 = float(cateto1**2)
catetoq2 = float(cateto2**2)
soma_raiz = catetoq1 + catetoq2
hipotenusa = math.sqrt(soma_raiz)
print (hipotenusa)

