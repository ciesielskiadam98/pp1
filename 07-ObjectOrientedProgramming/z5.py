class Songs():
    def __init__(self, singer, title, album, year):
        self.singer = singer
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return "Wykonawca: {}\nUtwór:     {}\nAlbum:     {}\nRok:       {}\n".format(self.singer, self.title, self.album, self.year)

singer1 = Songs('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', 2018)
singer2 = Songs('The Black Keys', 'Fever', 'Fever', 2014)
singer3 = Songs('The xx','Intro','xx',2009)
print(singer1)
print(singer2)
print(singer3)


