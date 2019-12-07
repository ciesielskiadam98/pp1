class Statystyka():
    def __init__(self, coll):
        self.coll = coll
        self.max1 = max(self.coll)
        self.min1 = min(self.coll)
    def add_number(self):
        self.coll.append(int(input('Dodaj liczbę do zbioru: ')))
    def show(self):
        for i in self.coll:
            print(i, end = ' ')
    def maxx(self):
        self.max1 = max(self.coll)
        print(self.max1)
    def minn(self):
        self.min1 = min(self.coll)
        print(self.min1)
    def avg(self):
        suma = 0
        for i in self.coll:
            suma += i
        print(suma/len(self.coll))
        
        
        
num1 = Statystyka([12, 37, 6, 9, 17])
num1.maxx()
num1.minn()
num1.avg()


