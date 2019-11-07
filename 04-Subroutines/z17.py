import random
def rzucKostka():
    return(random.randrange(1,7))
suma = 0

for i in range(3):
    suma += rzucKostka()
print(suma)