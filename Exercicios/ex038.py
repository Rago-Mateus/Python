print('Jogo do maior, menor ou igual!')
print(('==--==')*15)
n1 = int(input('Diga um número inteiro:'))
n2 = int(input('Diga outro número inteiro:'))
numeros = [n1,n2]

if n1 == n2:
    print('o número {} e {} são iguais. Ou seja {}={}'.format(n1,n2,n1,n2))
elif n1 > n2:
    print('O n1 igual a {} é maior do que n2, que é igual a {}. Ou seja {} > {}'.format(n1,n2,n1,n2))
else:
    print('O n2 igual a {} é maior do que n1, que é igual a {}. Ou seja {} > {}'.format(n2,n1,n2,n1))
print('++FIM++')
