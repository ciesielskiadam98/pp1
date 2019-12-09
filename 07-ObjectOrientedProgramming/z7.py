class Student():
    
    album = 100000
    
    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.uczelnia = 'UEK Kraków'
        Student.album += 1
        self.album = Student.album
    
    def __str__(self):
        return "{} {} ({}), {}, {}".format(self.imie, self.nazwisko, self.album, self.kierunek, self.uczelnia)
    
student1 = Student('Wacław','POTOCKI','Informatyka stosowana')
student2 = Student('Jan', 'KOWALSKI', 'Prawo')
student3 = Student('Adam','NOWAK','Finanse i Rachunkowość')
print(student1)
print(student2)
print(student3)