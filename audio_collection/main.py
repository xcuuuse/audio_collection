from audio.base import AudioFormat, AudioFile, Converter
from artists.artist import Artist
from artists.album import Album
from audio.metadata import Genre, Tag
from tracks.track import Track, LiveRecording
from user.user import User, Authentication
from user.authentication import Password, Username
form = AudioFormat(".wav")
form2 = AudioFormat(".flac")
file = AudioFile("e:/numb.wav", 183, form, 1024)
print(file.get_info())

converter = Converter([form, form2])
converter.convert_file(file, form2)
print(file.get_info())
genres = [Genre("nu metal"), Genre("alt rock")]
artist = Artist("Linkin Park", "linkin park", genres)
album = Album("Meteora", 2003, artist, genres[0])
# maybe do the logic of file size changing
track = Track("e:/numb.wav", 183, form, 1024,
              "Numb", artist, album)
print(track.get_info())
track.add_tag(Tag("metal"))
print(track.get_info())
