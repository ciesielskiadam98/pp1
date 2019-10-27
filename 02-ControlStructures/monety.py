kwota = int(input("Podaj kwote: "))

print("5zł - {} szt".format(kwota//5))
print("2zł - {} szt".format((kwota - (kwota//5)*5) // 2))
print("1zł - {} szt".format(kwota - ((kwota//5)*5)-(((kwota - (((kwota//5)*5))) // 2 )*2)))


