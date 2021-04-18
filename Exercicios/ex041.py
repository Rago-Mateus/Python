print('CALCULADORA DE CATEGORIA DE ATLETAS')
print(('==--==')*15)
import datetime
t = datetime.datetime.strptime((input('Diga a data de hoje no formato xxx-xx-xx:')),'%Y-%m-%d')
n = datetime.datetime.strptime((input('Diga sua data de nascimento, no formato xxxx-xx-xx:')),'%Y-%m-%d')
d = (t - n).days
mi = 9*365
i = 14*365
j = 19*365
s = 20*365
ma = 21*365

if d<=mi:
    print('Você tem menos de 9 anos, então sua categoria é MIRIM.')
elif d<=i:
    print('Você tem entre 14 e 9 anos, então sua categoria é INFANTIL.')
elif d<=j:
    print('Você tem entre 14 e 19 anos, então sua categoria é JUNIOR.')
elif d==s:
    print('Você tem 20 anos, portanto sua categoria é SÊNIOR.')
else:
    print('Você tem mais de 20 anos, portanto sua categoria é MASTER.')

print('==FIM==')
