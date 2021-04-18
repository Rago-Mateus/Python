#cidade = str(input('Diga o nome de sua cidade:')).strip()
#cidade = cidade.replace(cidade, cidade.lower())
#separado = cidade.split()

#if separado[0] == 'santo':
#    print('A cidade começa com a palavra -santo-')
#else:
#    print('A cidade não começa com a palavra -santo-')

city = str(input('Diga sua cidade:')).strip()
city = city.replace(city, city.lower())
print(city[:5] == 'santo')