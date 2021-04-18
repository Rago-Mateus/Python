print('MOSTRADOR DE NÚMEROS PARES!')

i = int(input('Digite um número para começar a contagem dos números pares:'))
f = int(input('Digite até qual número iremos contar:'))
if i%2==0:
    for c in range (i, f+2, 2):
        print(c)
else:
    for c in range (i+1, f, 2):
        print(c)
print('==FIM==')

