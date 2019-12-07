class University():
    def __init__(self):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
        
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
    
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname

called = University()
called.set_name('AGH')
called.print_name()

called.print_fullname()
called.set_fullname('Akademia Górniczo Hutnicza')
called.print_fullname()
