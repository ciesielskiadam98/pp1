liczba = int(input("Podaj liczbe: "))
binarna = []
x = liczba
while liczba > 0:
        binarna.append(liczba%2)
        liczba = liczba//2
    
print("{} = {}".format(x, binarna[-1*len(binarna):-1]))
    