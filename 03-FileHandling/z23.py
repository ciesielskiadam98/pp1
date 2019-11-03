import re
with open('land.txt', 'r') as file:
    x = re.findall('[0-9]', file.read())
    suma = 0
    for i in x:
        suma += int(i)
    print('Suma: {}'.format(suma))