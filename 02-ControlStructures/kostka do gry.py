import random
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
#print(random.randint(0,1))

for i in range(100):
    x = random.randint(1,6) #losowanie
    if x == 1:
        a1 += 1
    elif x == 2:
        a2 += 1
    elif x == 3:
        a3 += 1
    elif x == 4:
        a4 += 1
    elif x == 5:
        a5 += 1
    else:
        a6 += 1
        
print("Szóstka: {}".format(a6))
print("Piątka: {}".format(a5))
print("Czwórka: {}".format(a4))
print("Trójka: {}".format(a3))
print("Dwójka: {}".format(a2))
print("Jedynka: {}".format(a1))
    