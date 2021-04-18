h = float(input('Diga qual a altura da parede:'))
l = float(input('Agora, qual a largura de sua parede:'))
Area = h*l
print('Isso significa que a área da parede é de {} metros quadrados.'.format(Area))
litros = (Area//2)
print('Para pintar toda esta parede, vc precisaria de {} litros de tinta'.format(litros))