imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
imie = input("Podaj imie: ")
def jestImie(imie,imiona):
    if imie in imiona:
        return "Imię znajduje się w wykazie imion"
    else:
        return "Imie nie znajduje się w wykazie imion"
        
print(jestImie(imie, imiona))