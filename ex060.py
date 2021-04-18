contador = 0
fatorial = 1
print('CALCULADORA DE NÚMEROS FATORIAIS')
print('==--=='*15)
numero = int(input('Diga um número para calcularmos o seu fatorial!'))
escolhido = numero
while contador-1 != 0:
    fatorial = fatorial*numero
    contador = numero-1
    numero = numero-1
print('Você escolheu o número {}, em que seu fatorial é igual a {}. [{}!={}]'.format(escolhido,fatorial,escolhido,fatorial))