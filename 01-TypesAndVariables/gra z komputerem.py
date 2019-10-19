import random

#przypisanie do a randomowej liczby od 1 do 6

a = random.randrange(1, 7)

#wczytanie liczby b wymyslonej przez uzytkownika w celu zgadniecia liczby a

b = int(input("Zgadnij ile oczek wyrzucilem: "))

print("Komputer wyrzucil {} oczek.".format(a))

print("Zgadles... {}".format(a==b))