from audio.metadata import Genre


class Artist:
    def __init__(self, name: str, bio: str, genres: list[Genre]):
        self.__name = name
        self.__bio = bio
        self.__genres = genres

    @property
    def name(self):
        return self.__name

    @property
    def bio(self):
        return self.__bio

    @property
    def genres(self):
        return [i.name for i in self.__genres]

    def get_info(self):
        return f"{self.name}: {self.bio}. Genres: {", ".join(self.genres)}"


class Musician(Artist):
    def __init__(self, name: str, bio: str, genres: list[Genre],
                 instruments: list[str]):
        super().__init__(name, bio, genres)
        self.__instruments = instruments

    @property
    def instruments(self):
        return self.__instruments


