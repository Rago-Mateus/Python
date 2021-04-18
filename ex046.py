import time
print('FOGOS DE ARTIFÍCIO')
print('=--='*10)
print('Pressione qualquer tecla para iniciar os fogos de artifício.')
s = input('          PRESS TO START')
print('Contagem regressiva!!!')
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('BUM! BUM! CHACALACA BUM BUM BUM!!!')
