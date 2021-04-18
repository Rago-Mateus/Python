print('Calculadora de aumento de salário.')
print(('==--==')*15)
print('Pessoas com salários até R$1250 terão aumento de 15%, para as demais um aumento de 10%')
s = float(input('Qual o seu salário?'))
if s <= 1250.00:
    i = s*0.15
else:
    i = s*0.1
print('Para seu salário de R${}, seu aumento é de {}.'.format(s,i))

print('==FIM==')