x = int(input("Podaj liczbe całkowitą x: "))
y = int(input("Podaj liczbe całkowitą y: "))

if ( x < 0 or y < 0 ):
    print("Przynajmniej jedna liczba jest ujemna")
else:
    print("Żadna z liczb nie jest ujemna")