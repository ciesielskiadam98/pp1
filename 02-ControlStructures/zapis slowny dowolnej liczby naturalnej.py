tab=['zero', 'jeden','dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
x = int(input("Podaj dowolna liczbe naturalna: "))
a = 0 #pomocnicza zmienna - przechowuje elementy stringa jako int

x = str(x)

print(x + " - ", end="")

for i in range(len(x)):
    a = x[i]
    a = int(a)
    print(tab[a], end=" ")
    