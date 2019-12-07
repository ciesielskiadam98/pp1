import random
class Dice():
    def __init__(self):
        self.number = random.randrange(1,6)
    def throw(self):
        self.number = random.randrange(1,6)
        return self.number
        
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
while True:
    print(dice1.throw())
    print(dice2.throw())
    print(dice3.throw())
    print('Suma: {}'.format(dice1.number + dice2.number + dice3.number))
    x = input()

    