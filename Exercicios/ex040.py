print('CALCULADORA DE NOTAS')
print(('==--==')*15)
n1 = int(input('Escreva a nota da sua primeira prova:'))
n2 = int(input('Escreva a nota da sua segunda prova:'))
m = (n1+n2)/2
if m<5:
    print('Sua média final foi {}, portanto vc está REPROVADO.'.format(m))
elif m>6.99:
    print('Sua média final foi {}, portanto vc está APROVADO!'.format(m))
else:
    print('Sua média final foi de {}, portanto vc está de RECUPERAÇÃO.'.format(m))

print('==FIM==')
