import math

a = int(input("Podaj pierwszy bok: "))
b = int(input("Podaj drugi bok: "))
c = int(input("Podaj trzeci bok: "))

p = (a+b+c)/2

pole = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Pole trójkąta o podanych bokach wynosi: {}".format(pole))