class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on == True:
            print("Telewizor jest załączony, kanał {}".format(int(self.channel_no)))
        else:
            print("Telewizor jest wyłączony")
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.off()
tv1.show_status()