print('=-'*15)
print('SEQUÊNCIA DE FIBONACCI!')
print('=-'*15)
n = int(input('Quantos termos vc quer apresentar da sequência de fibonacci?'))
t1=0
t2=1
print('{} -> {}'.format(t1,t2), end='')
c=3
while c<=n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    c=c+1
    t1=t2
    t2=t3
print('')
print('==FIM==')