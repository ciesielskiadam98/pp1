text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
x = input("Podaj szukaną samogłoskę: ")
def findCount(x, text):
    y = 0
    for i in text.lower():
        if i == x:
            y += 1
    return y
print("Liczba samogłosek {}: {}".format(x, findCount(x, text)))
    