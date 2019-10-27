a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbe: "))

if (a > b and a < c) or (a < b and a > c):
    print("Mediana: {}".format(a))
elif (b > a and b < c) or (b < a and b > c):
    print("Mediana: {}".format(b))
else:
    print("Mediana: {}".format(c))
