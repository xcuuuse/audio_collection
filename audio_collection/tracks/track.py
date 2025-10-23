from audio.base import AudioFile
from audio.formats import AudioFormat
from artists.artist import Artist
from artists.album import Album
from audio.metadata import Genre, Tag


class Track(AudioFile):
    def __init__(self, path: str, duration: int, audio_format: AudioFormat, size: int,
                 title: str, artist: Artist, album: Album):
        super().__init__(path, duration, audio_format, size)
        self.title = title
        self.artist = artist
        self.album = album
        self.year = album.year
        self.genre = album.genre
        self.tag = None

    def get_info(self):
        return \
            (f"{self.title}({self.artist.name}) | {self.album.title} | {self.year} | {self.genre.name} |"
             f" {self.tag.name if self.tag else ""}")

    def add_tag(self, tag: Tag):
        self.tag = tag


class Podcast(AudioFile):
    def __init__(self, path: str, duration: int, audio_format: AudioFormat, size: int,
                 podcaster: str, episode: int, title: str):
        super().__init__(path, duration, audio_format, size)
        self.podcaster = podcaster
        self.episode = episode
        self.title = title

    def get_info(self):
        return f"{self.podcaster}: Episode {self.episode}. {self.title}"


class LiveRecording(AudioFile):
    def __init__(self, path: str, duration: int, audio_format: AudioFormat, size: int,
                 artist: Artist, track: Track, year: int):
        super().__init__(path, duration, audio_format, size)
        self.artist = artist
        self.track = track
        self.year = year

    def get_info(self):
        return f"{self.artist.name} - {self.track.title}(Live {self.year})"



