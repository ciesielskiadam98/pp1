a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbe: "))

if a < b and a < c:
    print("Rosnąco: {},".format(a), end=" ")
    if b < c:
        print("{}, {}".format(b,c))
    else:
        print("{}, {}".format(c,b))
elif b < a and b < c:
    print("Rosnąco: {},".format(b), end=" ")
    if a < c:
        print("{}, {}".format(a,c))
    else:
        print("{}, {}".format(c,a))
if c < a and c < b:
    print("Rosnąco: {},".format(c), end=" ")
    if b < a:
        print("{}, {}".format(b,a))
    else:
        print("{}, {}".format(a,b))        