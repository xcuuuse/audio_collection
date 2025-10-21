from tracks.track import Track
from user.user import User


class Playlist:
    def __init__(self, name: str, user: User):
        self.__name = name
        self.__user = user
        self.__tracks = list[Track]

    @property
    def name(self):
        return self.__name

    @property
    def user(self):
        return self.__user

    @property
    def tracks(self):
        return self.__tracks

    """def add_track(self, path: str, duration: int, audio_format: AudioFormat, size: int,
                 title: str, artist: Artist, album: Album):
        self.__tracks.append(track) """


class SmartPlaylist:
    pass


class PlaylistManager:
    pass

