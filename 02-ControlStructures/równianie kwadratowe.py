import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b*b-4*a*c

if delta < 0:
    print("Brak rozwiązań")
elif delta == 0:
    x0 = -1*b/2*a
    print("Rozwiązanie równiania x0 = {}".format(x0))
else:
    x1 = (-1*b - math.sqrt(delta))/2*a
    x2 = (-1*b + math.sqrt(delta))/2*a
    print("Rozwiązania równiania x1 = {} i x2 = {}".format(x1,x2))