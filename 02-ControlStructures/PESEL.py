pesel = input("Podaj PESEL: ")

if (pesel[9] == "0" or pesel[9] == "2" or pesel[9] == "4" or pesel[9] == "6" or pesel[9] == "8"):
    plec = "Kobieta"
else:
    plec = "Mężczyzna"
    
a = pesel[0:2] #zmienna pomocnicza do przechowania elementów str jakos int
b = pesel[2:4] #jak wyżej
a = int(a)
b = int(b)

if b <= 12:
    wiek = 2018 - (1900 + a)
else:
    wiek = 2018 - (2000 + a)

print("Płeć: {}".format(plec))
print("Wiek: {}".format(wiek))