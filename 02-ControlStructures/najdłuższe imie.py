tablica = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

i = 0
x = 1
z = 0
while (z == 0): #gwarancja powrotu do pętli
    while ( x <= 5 and len(tablica[i]) > len(tablica[x])):
        x += 1
    
    if x > 5:
        print(tablica[i])
        z = 1 #koniec pętli pierwszej
    else:
        i = x #kolejne imie po nieudanym poprzednim
        x = i+1 #kolejne imie po sprawdzanym od nowej pozycji
        if i == 5:
            print(tablica[i])
            z = 1
        else:
            z = 0