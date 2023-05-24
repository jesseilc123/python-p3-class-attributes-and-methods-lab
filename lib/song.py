class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre)
        cls.genre_count[song.genre] = 0

    @classmethod
    def add_to_artists(cls, song):
        cls.artists.append(song.artist)
        cls.artist_count[song.artist] = 0

    @classmethod
    def add_to_genre_count(cls, song):
        for g in cls.genres:
            if song.genre == g:
                cls.genre_count[song.genre] += 1

    @classmethod
    def add_to_artist_count(cls, song):
        for a in cls.artists:
            if song.artist == a:
                cls.artist_count[song.artist] += 1
