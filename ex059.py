print('++==CALCULADORA DE DOIS NÚMEROS==++')
print(('==--==')*10)
operacao = '99'
import time
time.sleep(1)
n1 = float(input('Diga o primeiro número:'))
n2 = float(input('Diga o segundo número:'))
print('Você escolheu os números {} e {}.'.format(n1, n2))
while operacao != '5':
    print('''Digite:
    [1] para somar
    [2] para multiplicar
    [3] para mostrar o maior
    [4] para input de novos números
    [5] para sair do programa''')
    operacao = str(input('Qual a sua opção?'))
    if operacao == '1':
        print('A soma dos números [{}] e [{}] é [{}]'.format(n1, n2, (n1+n2)))
    elif operacao == '2':
        print('A multiplicação dos números [{}] e [{}] é [{}].'.format(n1, n2, n1*n2))
    elif operacao == '3':
        print('O número maior entre [{}] e [{}] é [{}].'.format(n1, n2, max(n1, n2)))
    elif operacao == '4':
        n1 = float(input('Diga o novo primeiro número:'))
        n2 = float(input('Diga o novo segundo número:'))
    elif operacao == '5':
        print('Ok, encerrando o programa em:')
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        print('Programa encerrado!')