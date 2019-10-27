n = 0 #pomocnicza zmienna pozwalająca rysować coraz mniejszą ilość gwiazdek
for i in range(9):
    if i+1 <= 5:
        for y in range(i+1):
            print("*", end=" ")
    else:
        n += 1 
        for x in range(i+1-2*n):
            print("*", end=" ")    
    print("")