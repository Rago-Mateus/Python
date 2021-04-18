print('Bem vindo à calculadora de multa de velocidade')
print(str('==--==')*15)
v = input(print('Qual a sua velocidade em km\h?'))
if int(v)>80:
    m=(int(v)-80)*7
    print('O limite de velocidade desta rodovia é 80km\h.')
    print(('Sua velocidade atual é de {}, portanto {} acima do limite.'.format(v,(80-int(v)))))
    print('Você foi multado em R${}.'.format(m))
else:
    print('Siga em frente! Lembre-se que o limite de velocidade desta rodovia é  80km\h!')

print('==FIM==')

