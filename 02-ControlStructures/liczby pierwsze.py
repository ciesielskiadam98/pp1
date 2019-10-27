ilosc = int(input("Podaj liczbe liczb pierwszych: "))

i = 0 #liczy liczby pierwsze
x = 3
print("Liczby pierwsze: 2, ", end="")

while (i < ilosc):
    for j in range(2,x):
        if x%j != 0:
            if j == (x-1):
                print("{},".format(x), end=" ")
                i += 1
                x += 1
        else:
            j = x #po to aby wyszedł z pętli
            x += 1
    
        