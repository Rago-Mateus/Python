t = 0
n = int(input('Diga um número e te direi se ele é primo:'))
for c in range(1, (n//2)+1):
    if n % c == 0:
        t=t+1
print(t)
if  t == 1:
    print('Este número é primo, pois é divisel por 1 e por ele mesmo!')
else:
    print('Este número não é primo pois ele tem mais de 2 divisores.')
