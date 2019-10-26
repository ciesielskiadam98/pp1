x = int(input("Podaj liczbe: "))

for i in range(10):
    print("{} x {} = {}".format(x, i+1, (i+1)*x))