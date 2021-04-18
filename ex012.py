preco = float(input('Qual o preço do produto?'))
desconto = float(input('Qual o desconto a ser aplicado (em decimais separado por ponto):'))
preco_desconto = preco * (1-desconto)
print('O preço original do produto é {} e com desconto de {} fica {}.'.format(preco,desconto,preco_desconto))
