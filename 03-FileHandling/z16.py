import re
suma = 0
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
for i in cyfry:
    suma += int(i)
    
print('Średnia temperatura: {}'.format(suma / int(len(cyfry))))