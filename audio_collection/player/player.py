from tracks.track import Track

class AudioOutput:
    def __init__(self, name: str):
        self.__name = name
        self.connected_device = None

    @property
    def name(self):
        return self.__name

    def connect_device(self, name):
        self.connected_device = name


class Player:
    def __init__(self, track: Track, device: AudioOutput):
        self.__track = track
        self.__device = device
        self.is_playing = False

    @property
    def track(self):
        return self.__track

    @property
    def device(self):
        return self.__device

    def play(self, track: Track):
        if not self.is_playing:
            print(f"{self.track.title} is now playing")
            self.is_playing = True
        else:
            print(f"{self.track.title} is paused")
            self.is_playing = False

class PlaybackQueue:
    pass

