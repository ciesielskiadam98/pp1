limit = int(input("Podaj limit prędkości w km/h: "))
predkosc = int(input("Podaj predkosc samochodu w km/h: "))

if predkosc - limit <= 10:
    mandat = (predkosc - limit)*5
    print("Mandat(zł): {}".format(mandat))
else:
    mandat = 50 + (predkosc - limit - 10)*15
    print("Mandat(zł): {}".format(mandat))