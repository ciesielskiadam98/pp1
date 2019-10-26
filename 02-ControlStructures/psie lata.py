x = int(input("Podaj wiek psa w ludzkich latach: "))

if x <= 2:
    print("Wiek psa w psich latach: {}".format(x*10.5))
else:
    print("Wiek psa w psich latach: {}".format(21+4*(x-2)))