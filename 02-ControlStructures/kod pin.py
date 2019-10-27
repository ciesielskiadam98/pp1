pin = "0805"

x = input("Podaj PIN: " )
i = 1

while i <= 3:       
     if x == pin:
         print("Kod pin prawidłowy")
         i = 4
     elif i == 3:
         print("Karta płatnicza zostaje zablokowana")
         i = 4
     else:
         print("Kod PIN nieprawidłowy")
         x = input("Podaj PIN: ")
         i += 1