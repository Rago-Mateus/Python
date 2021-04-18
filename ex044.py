from time import sleep

print('CALCULADORA DE PREÇOS: preço vs condição de pgto')
print('===--==='*15)
p = float(input('Escreva qual o preço do produto que deseja comprar:'))
print('Escolha a sua condição de pagamento. Digite:')
sleep(1)
print('1 para pgto à vista em dinheiro ou cheque: 10% de desconto;')
sleep(1)
print('2 para pgto à vista no cartão: 5% de desconto;')
sleep(1)
print('3 para pgto no cartão até 2x: preço normal;')
sleep(1)
print('4 para pgto no cartão parcelado de 3x ou mais: 20% de acréscimo;')
c = int(input('Digite 1, 2, 3 ou 4:'))
if c==1:
    print('Para pgto à vista em dinheiro ou cheque, o produto que era R${}, sai por R${}'.format(p,round(p*0.9,2)))
elif c==2:
    print('Para pgto à vista no cartão, o produto que era R${}, sai por R${}'.format(p,round(p*0.95,2)))
elif c==3:
    print('Para pgto parcelado cartão até 2x, o produto não tem desconto e sai por R${}'.format(round(p, 2)))
elif c==4:
    print('Para pgto parcelado cartão de 3x ou mais, o produto tem acréscimo de 20% e sai por R${}'.format(round(p*1.2, 2)))
else:
    print('Condição de pagamento inválida! Reinicie a calculadora.')

print('===FIM===')
