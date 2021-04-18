i = int(input('Diga o primeiro termo de uma PA (progressão aritmética):'))
r = int(input('Diga qual será a razão da PA:'))
#for c in range(i, 10*r, r):
#    print(c)
c = 0
termo = i
while c != 9:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    c = c + 1
print('FIM')
