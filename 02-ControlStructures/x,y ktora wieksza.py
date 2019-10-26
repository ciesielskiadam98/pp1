x = int(input("Podaj liczbe całkowitą: "))
y = int(input("Podaj liczbe całkowitą: "))

if x > y:
    print(x)
else:
    if x < y:
        print(y)
    else:
        print("Liczby są takie same i wynoszą {}".format(x))