import time
print('Gerador de progressão aritmética!!!')
print(('==--==')*10)
a = int(input('Diga um número para o início da PA:'))
r = int(input('Diga um número para a razão da PA:'))
inicio=a
time.sleep(1)
print('Irei apresentar os 10 primeiros números desta PA em que a1={} e r={}.'.format(a,r))
time.sleep(1)
c=1
termos=0
mais=10
total=0
while mais !=0:
    total=total+mais
    while c<=total:
        print('{} -> '.format(a), end='')
        a=a+r
        c=c+1
        termos=termos+1
    print('')
    print('++PAUSA++')
    mais = int(input('Quantos termos a mais quer apresentar na PA? [Digite 0 para finalizar'))
print('Progressão finalizada com {} termos de uma PA que começou com a1={} e razão={}.'.format(total,inicio,r))
print('==FIM==')
