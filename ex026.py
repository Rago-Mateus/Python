frase = str(input('Diga uma frase')).lower().strip()
qnt = frase.count('a')

print('Em sua frase -{}-, aparece a letra -a- {} vezes.'.format(frase,qnt))

print(frase.find('a'))
print(frase.rfind('a'))


