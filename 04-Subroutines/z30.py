import random
def r():
    x = random.randrange(1,51)
    return x
odd = 0
even = 0
for i in range(1000):
    if r() % 2 == 0:
        even += 1
    else:
        odd += 1
print("Parzyste: {} %\nNieparzyste: {} %".format(even/10, odd/10))
