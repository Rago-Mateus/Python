salario = float(input('Qual o salário do funcionário?'))
dissidio = float(input('Qual foi o dissídio deste ano (em decimais separado por ponto):'))
salario_aumento = salario * (1+dissidio)
print('O salário original do funcionário era {} e com dissídio de {} ficou {}.'.format(salario,dissidio,salario_aumento))

