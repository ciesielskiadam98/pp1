import re
with open('numbersinrows.txt', 'r') as file:
    quant = re.split(',|\n', file.read())
    print('Ilość liczb: {}'.format(len(quant)))
    suma = 0
    for i in quant:
        suma += int(i)
    print('Suma liczb: {}'.format(suma))
    
    
    
    
    #Alternative version with re.findall() instead of re.split
    #
    #quant = re.findall('[0-9]+', file.read())
    #print('Ilość liczb: {}'.format(len(quant)))
    #suma = 0
    #  for i in quant:
    #      suma += int(i)
    #print('Suma liczb: {}'.format(suma))
    