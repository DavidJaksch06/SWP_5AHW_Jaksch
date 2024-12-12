class Musik:
    def __init__(self, titel):
        self.titel = titel

    def spielen(self):
        print(f"Spiele '{self.titel}'")


class Instrument(Musik):
    def __init__(self, titel, instrument):
        super().__init__(titel)
        self.instrument = instrument

    def spielen(self):
        print(f"Spiele '{self.titel}' auf {self.instrument}")


class Playlist(Musik):
    def __init__(self, titel, songs):
        super().__init__(titel)
        self.songs = songs

    def spielen(self):
        print(f"Spiele die Playlist '{self.titel}' mit den Songs: {', '.join(self.songs)}")


lied = Musik("Gutes Musikstück")
lied.spielen()

gitarre = Instrument("Gitarrensong", "Gitarre")
gitarre.spielen()

playlist = Playlist("Chill Vibes", ["Chill-Song 1", "Chill-Song 2", "Chill-Song 3"])
playlist.spielen()