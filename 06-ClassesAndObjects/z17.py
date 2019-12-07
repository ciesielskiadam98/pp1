import math
class Fraction():
    def __init__(self, counter, denominator):
        self.counter = counter
        self.denominator = denominator
    def simpl(self):
        x = math.gcd(self.counter,self.denominator)
        self.counter = int(self.counter / x)
        self.denominator = int(self.denominator / x)
    def show(self):
        if self.denominator != 1 and self.denominator != 0 and self.counter != 0:
            print('{}/{}'.format(self.counter, self.denominator))
        elif self.denominator == 1:
            print(self.counter)
        elif self.counter == 0:
            print(0)
        else:
            print("Dzielenie przez zero!")

fraction1 = Fraction(0,3)
fraction1.show()
fraction1.simpl()
fraction1.show()
        