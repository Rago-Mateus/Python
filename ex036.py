print('Bem vindo ao programa MEU FINANCIAMENTO, MINHA VIDA!')

print(('==--==')*15)

f = int(input('Qual o valor do financiamento da casa?'))
s = int(input('Qual o valor do sau salário?'))
t = int(input('Em quantos meses vc pretende pagar este finaciamento?'))
p = f / t
c = p / s

if c > 0.3:
    print('Infelizmente não podemos conceder este financiamento devido ao seu nível de renda. A parcela pretendia é de {}, que é maior do que 30% do seu salário.'. format(p))
else:
    print('Seu financiamento foi aprovado e o valor de sua parcela é de {}.'.format(p))

print('++FIM++')

