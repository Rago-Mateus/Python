from time import sleep

print('CALCULADORA DE IMC (índice de massa corporal)')
print('IMC<18.5 significa que vc está abaixo do peso.')
sleep(1)
print(' 18.5 <IMC< 25 significa que vc está no peso ideal!')
sleep(1)
print(' 25 <IMC< 30 significa que vc está com sobrepeso.')
sleep(1)
print(' 30 <IMC< 40 significa que vc está com obsesidade!')
sleep(1)
print('IMC > 40 significa que vc está com obsesidade morbida!')
sleep(1)
print(('==--==')*15)

a = float(input('Escreva a sua altura em metros:'))
m = float(input('Escreva o seu peso em kg:'))
imc = round(m / (a*a),1)
mi = round(18.5 * (a*a),1)
ma = round(25 * (a*a),1)
if  imc<18.5:
    print('Você está abaixo do peso!')
    print('Seu peso ideal é entre {} e {}'.format(mi,ma))
elif imc<25:
    print('Você está no peso ideal!!')
elif imc<30:
    print('Você está com sobrepeso.')
    print('Seu peso ideal é entre {} e {}'.format(mi,ma))
elif imc<40:
    print('Você está com obesidade grau 1')
    print('Seu peso ideal é entre {} e {}'.format(mi, ma))
else:
    print('Você está com obesidade mórbida')
    print('Seu peso ideal é entre {} e {}. CUIDE DE SUA SAUDE!'.format(mi, ma))

print('===FIM===')
