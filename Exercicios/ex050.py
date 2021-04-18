s = 0
for c in range(1,6,1):
    c = int(input('Diga um número:'))
    if  c % 2 ==0:
        s=s+c
print('a soma dos números pares são: {}'.format(s))
