reta1 = float(input('Diga o tamanho de uma reta:'))
reta2 = float(input('Diga o tamanho de outra reta:'))
reta3 = float(input('Diga o tamanho de uma última reta:'))
if  reta1 > reta2:
    d1 = reta1-reta2
else:
    d1 = reta2-reta1
if  reta1 > reta3:
    d2 = reta1-reta3
else:
    d2 = reta3-reta1
if  reta2 > reta3:
    d3 = reta2-reta3
else:
    d3 = reta3-reta2
diferenças = [d1,d2,d3]

triangulo = [reta1, reta2, reta3]
if  min(triangulo) < (sum(triangulo) - min(triangulo)):
    if min(triangulo) > max(diferenças):
        print('é triangulo.')
    else:
        print('não é triangulo')
else:
    print('não é triangulo.')