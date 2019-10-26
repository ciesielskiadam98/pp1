a1 = 1
r = 3

n = int(input("Podaj ilosc wyrazów ciągu arytmetycznego: "))

print("Ciąg arytmetyczny o różnicy 3:", end=" ")

if n > 1:
    while n > 0:
        print("{},".format(a1), end=" ")
        a1 += r
        n -= 1
else:
    print("{},".format(a1), end=" ")