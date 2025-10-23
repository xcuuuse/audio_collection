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

    def add_track(self, track: Track):
        self.__tracks.append(track)

    def remove_track(self, track: Track):
        self.__tracks.remove(track)


class SmartPlaylist(Playlist):
    def __init__(self, name: str, user: User,
                 criteria: dict):
        super().__init__(name, user)
        self.__criteria = criteria

    @property
    def criteria(self):
        return self.__criteria

    def update_tracks(self):
        pass


class PlaylistManager:
    def __init__(self, name: str, user: User):
        self.__name = name
        self.__user = user

    @property
    def name(self):
        return self.__name

    @property
    def user(self):
        return self.__user

    @staticmethod
    def create_playlist(name: str, user: User):
        return Playlist(name, user)



