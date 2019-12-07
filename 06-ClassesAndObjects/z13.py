class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    
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
    
    def set_channels(self, channels_list):
        self.channels = channels_list
    
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        for i in range(len(self.channels)):
            print("{}. {}".format(i+1, self.channels[i]))
    
tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
tv1.show_channels()
tv1.show_status()
tv1.off()
