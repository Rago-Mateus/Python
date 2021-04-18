f = str(input('Diga uma frase e te direi se é um palíndromo:'))
f = f.split()
f = ''.join(f)
t = len(f)
r=0
s=0
w=0
z=0
for c in range(t+1,0,-1):
    r = c-1

    for q in range(w,w+1):
        s = q + 1
        w = w +1

    if f[r-1:r] == f[s-1:s]:
        z = z+1
    else:
        z = z+0
if z-1 == t:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
