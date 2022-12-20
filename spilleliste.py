from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        file = open(filnavn, "r")
        liste = []
        for line in file:
            alleData = line.strip().split(";")
            alleSanger = Sang(alleData[1], alleData[0])
            self._sanger.append(alleSanger)
        return self._sanger

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:

            sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel) == True:
                funnetSang = sang
                return funnetSang

    def hentArtistUtvalg(self, artistnavn):
        queenListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn) == True:
                queenListe.append(sang)
        return queenListe
