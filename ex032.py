print('Bem vindo a calculadora de ano bisexto!')
print('A calculadora funciona para anos posteriores ao ano 2000.')

print(str('--==--')*15)
ano = input(print('Diga um ano que queira saber se é bisexto:'))
if int(ano)%4==0 :
    print('O ano {} é bisexto!'.format(ano))
else:
    print('O ano {} NÃO é bisexto!'.format(ano))

print('==FIM==')