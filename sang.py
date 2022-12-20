class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print(" artist er", self._artist, "og tittel er", self._tittel)

    def sjekkArtist(self, navn):
        navnene = navn.split(" ")
        lista = self._artist.split(" ")
        for navn in navnene:
            if navn in lista:
                return True

    def sjekkTittel(self, tittel):
        if str(tittel).lower() == str(self._tittel).lower():
            return True

    def sjekkArtistOgTittel(self, artist, tittel):

        if self.sjekkTittel(tittel) == True and self.sjekkArtist(artist) == True:
            return True
        else:
            return False
