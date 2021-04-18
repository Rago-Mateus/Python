nome = input('Qual o seu nome completo?').strip()

maiuscula = nome.upper()
minuscula = nome.lower()
print(maiuscula)

print(minuscula)

semespaco = nome.replace(" ", '')

print(len(semespaco))

print(len(nome.split()[0]))
