class TV():
    
    def __init__(self):
        self.is_on = False
    
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on == True:
            print("Telewizor jest załączony")
        else:
            print("Telewizor jest wyłączony")
    

tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.off()
tv1.show_status()
        