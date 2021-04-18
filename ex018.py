import math
angulo = float((input('Diga o valor de um ângulo para eu te dizer o seno dele:')))
angulorad = math.radians(angulo)
seno = math.sin(angulorad)
coseno = math.cos((angulorad))
tangente = math.tan((angulorad))
print( 'Para o ângulo {}: \n o seno vale {:.2f}; \n o coseno vale {:.2f}; \n a tangente vale {:.2f}.'.format(angulo,seno,coseno,tangente))




