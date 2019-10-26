tablica = [15, 8, 31, 47, 2, 19]
suma = 0
i = 1
x = len(tablica)
y = 0
while x > 0:
    if tablica[i-1]%2 != 0:
        suma += tablica[i-1]
        y += 1
    i += 1
    x -= 1
    
print("Średnia arytmetyczna nieparzystych liczb: {}".format(suma/y))