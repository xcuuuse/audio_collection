from artists.artist import Artist, Musician
from audio.metadata import Genre


class Album:
    def __init__(self, title: str, year: int, artist: Artist, genre: Genre):
        self.__title = title
        self.__year = year
        self.__artist = artist
        self.__genre = Genre

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def artist(self):
        return self.__artist

    @property
    def genre(self):
        return self.__genre.name


class Band(Artist):
    def __init__(self, name: str, bio: str, genres: list[Genre],
                 members: list[Musician]):
        super().__init__(name, bio, genres)
        self.__members = members

    @property
    def members(self):
        return [i.name for i in self.__members]

    def add_member(self, musician: Musician):
        self.__members.append(musician)
