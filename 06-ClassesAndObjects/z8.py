class University():
    def __init__(self):
        self.name = 'UEK'
        
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name

called = University()
called.set_name('AGH')
called.print_name()