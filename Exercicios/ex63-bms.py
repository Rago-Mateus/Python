print('SEQUÊNCIA DE FIBONACCI!')
print('=-='*20)
n = int(input('Quantos termos você quer apresentar da sequência de Fibonacci?'))
print('<','^~'*30,'>')
t1 = 0; t2 = 1; t3 = t1 + t2; c = 2; total = 0; m = 0;
print(' {} -> {} ->'.format(t1,t2), end='')
while c < n:
    c = c + 1
    print(' -> {}'.format(t3), end='')
    t1 = t2; t2 = t3; t3 = t1 + t2
print('')
print('<','^~'*30,'>')
print('==FIM==')
