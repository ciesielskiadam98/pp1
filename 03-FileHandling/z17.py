import re
suma = 0
tekst = 'To be, or not to be, that is the question'
samogloski = re.findall('a|e|y|i|o|u', tekst)

for i in samogloski:
    suma += 1
print('Liczba samogłosek w tekście: {}'.format(suma))