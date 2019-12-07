import statistics
class Statystyka():
    def __init__(self, coll):
        self.coll = coll
    def add_number(self):
        self.coll.append(int(input('Dodaj liczbę do zbioru: ')))
    def show(self):
        for i in self.coll:
            print(i, end = ' ')
    def maxx(self):
        self.max1 = max(self.coll)
    def minn(self):
        self.min1 = min(self.coll)
    def avg(self):
        suma = 0
        for i in self.coll:
            suma += i
        self.avgg = suma / len(self.coll)
    def display(self):
        print(self.max1)
        print(self.min1)
        print(self.avgg)
        print(self.median1)
    def median(self):
        x = sorted(self.coll)
        self.median1 = statistics.median(x)
        
num1 = Statystyka([12, 37, 6, 9, 17])
num1.maxx()
num1.minn()
num1.avg()
num1.median()
num1.display()

