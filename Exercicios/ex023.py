numero = str(input('Digite um numero entre 0 e 9999',))
qnt = len(numero)
if qnt == 1:
    numero = str('000')+numero

    print('A unidade vale: {}'.format(numero[3]))
    print('A dezena vale: {}'.format(numero[2]))
    print('A centena vale: {}'.format(numero[1]))
    print('O milhar vale: {}'.format(numero[0]))

elif qnt == 2:
    numero = str('00')+numero
    print('A unidade vale: {}'.format(numero[3]))
    print('A dezena vale: {}'.format(numero[2]))
    print('A centena vale: {}'.format(numero[1]))
    print('O milhar vale: {}'.format(numero[0]))
elif qnt == 3:
    numero = str('0')+numero

    print('A unidade vale: {}'.format(numero[3]))
    print('A dezena vale: {}'.format(numero[2]))
    print('A centena vale: {}'.format(numero[1]))
    print('O milhar vale: {}'.format(numero[0]))

else:
    print('A unidade vale: {}'.format(numero[3]))
    print('A dezena vale: {}'.format(numero[2]))
    print('A centena vale: {}'.format(numero[1]))
    print('O milhar vale: {}'.format(numero[0]))


num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print(('Dezena: {}'.format(d)))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
