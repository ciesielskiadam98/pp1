with open('shoppinglist.txt', 'a') as file:
        y = input("Dodaj produkt: ")
        while len(y)!=0:
            file.write(y + '\n')
            y = input("Dodaj produkt: ")