liczba = int(input("Podaj liczbę: "))
suma = 0
iloscLiczb = 0
srednia = 0
while liczba != 0:
    iloscLiczb += 1
    suma += liczba
    srednia = suma/iloscLiczb
    liczba = int(input("Podaj liczbę: "))
    
print("Liczb = {}, Średnia = {}, Suma = {}".format(iloscLiczb, srednia, suma))