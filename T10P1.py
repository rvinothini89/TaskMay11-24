# Audio class file to add rating and finding average rating
class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Rating should be between 1 and 5")
    @property
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
# Playlist class file to add audio, add rating and finding average rating
class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio):
        self.audio_files.append(audio)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Rating should be between 1 and 5")
    @property
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
# User class file to create audio file, playlist, adding audio to playlist, search audio/playlist 
class User:
    def __init__(self, username):
        self.username = username
        self.audio_files = []
        self.playlists = []

    def create_audio(self, name, url):
        audio = Audio(name, url)
        self.audio_files.append(audio)
        return audio

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, audio, playlist):
        if audio in self.audio_files and playlist in self.playlists:
            playlist.add_audio(audio)
        else:
            print("Audio or Playlist not found in user's collection")

    def search_audio_by_name(self, name):
        for audio in self.audio_files:
            if audio.name == name:
                return audio
        return None

    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

# Create a user
user = User("Vinothini")

# Create some audio files
audio1 = user.create_audio("Song1", "http://example.com/song1.mp3")
audio2 = user.create_audio("Song2", "http://example.com/song2.mp3")

# Create playlists
playlist1 = user.create_playlist("Rock Classics", "Rock")
playlist2 = user.create_playlist("Pop Hits", "Pop")

# Add audio files to playlists
user.add_audio_to_playlist(audio1, playlist1)
user.add_audio_to_playlist(audio2, playlist2)

# Search for an audio file by name
searched_audio = user.search_audio_by_name("Song1")
if searched_audio:
    print(f"Found audio: {searched_audio.name}, URL: {searched_audio.url}")

# Search for a playlist by name
searched_playlist = user.search_playlist_by_name("Rock Classics")
if searched_playlist:
    print(f"Found playlist: {searched_playlist.name}, Genre: {searched_playlist.genre}")

# Add ratings to audio files
audio1.add_rating(5)
audio1.add_rating(4)
print(f"Average rating for {audio1.name}: {audio1.average_rating}")

# Add ratings to playlists
playlist1.add_rating(5)
playlist1.add_rating(3)
print(f"Average rating for {playlist1.name}: {playlist1.average_rating}")
