suma1 = 0
suma2 = 0

for i in range(1,51):
    if i%2==0:
        suma1 += i
    else:
        suma2 += i
        
print("Suma liczb parzystych z przedziału <1,50> wynosi: {}".format(suma1))
print("Suma liczb nieparzystych z przedziału <1,50> wynosi: {}".format(suma2))
