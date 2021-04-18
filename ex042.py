print('CALCULADORA DE TRIANGULOS')
print(('==--==')*15)
a = int(input('Diga o tamanho da primeira reta a:'))
b = int(input('Diga o tamanho da segunda reta b:'))
c = int(input('Diga o tamanho da terceira reta c:'))

if  a==b==c:
    t= ('equilátero pois tem 3 lados iguais')
elif a==b or a==c or b==c:
    t= ('isósceles pois tem 2 lados iguais')
else:
    t= ('escaleno pois todos os lados são diferentes')

print('Será que a= {}cm, b= {}cm e c= {}cm formam um triângulo? VOU CALCULAR!'.format(a,b,c))
from time import sleep
sleep(3)

if  abs(b-c)<a and a<b+c and abs((a-c))<b and b<a+c and abs(a-b)<c and c<a+b:
    print('As retas {}, {} e {} formam um triângulo!!!'.format(a,b,c))
    print('Será que este triangulo é equilátero, isósceles ou escaleno? VOU CALCULAR!')
    from time import sleep
    sleep(3)
    print('Este triângulo é {}'.format(t))
    print('===FIM===')
else:
    print('As retas {}, {} e {} não formam um triângulo!!!'.format(a,b,c))
    print('===FIM===')

