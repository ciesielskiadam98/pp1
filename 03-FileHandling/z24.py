import re
tablica =[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('tekst.csv', 'w') as file:
    file.write('Imie,Nazwisko,Email\n')
    for i in tablica:
        for k in range(len(i)):
            if k != (len(i)-1):
                file.write('{},'.format(i[k]))
            else:
                file.write('{}\n'.format(i[k]))
        
            