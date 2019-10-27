liczba = int(input("Podaj liczbe: "))
binarna = []
while liczba >= 1:
        binarna.append(liczba%2)
        liczba = liczba//2
binarna.reverse()

i = 0 #pomocnicza zmienna

while i<len(binarna):
    print(binarna[i], end="")
    i += 1

    