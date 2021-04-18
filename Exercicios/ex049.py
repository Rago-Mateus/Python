n = float(input('Diga um número e te direi a tabuada correspondente a ele:'))
for c in range(0, 11, 1):
    print('{} x {} = {}'.format(n,c,n*c))
