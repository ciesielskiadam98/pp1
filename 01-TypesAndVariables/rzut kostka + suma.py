import random

#przypisanie losowych liczb do a,b,c za pomocą modułu random

a = random.randrange(1, 7)
b = random.randrange(1, 7)
c = random.randrange(1, 7)

suma = a + b + c

print("{} {} {}   {}".format(a, b, c, suma))