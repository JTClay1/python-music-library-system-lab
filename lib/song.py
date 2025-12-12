class Song:
    # Class-level tracking — shared across ALL Song instances
    # These describe the library as a whole, not any single song
    count = 0                 # total number of songs created
    genres = []               # unique list of all genres
    artists = []              # unique list of all artists
    genre_count = {}          # how many songs per genre
    artist_count = {}         # how many songs per artist

    def __init__(self, name, artist, genre):
        # Instance-level data — specific to THIS song only
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every time a Song is created, update shared class state
        # Using class methods keeps this logic centralized and clean
        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment total song count
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Only add genre if it hasn't been seen before
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Only add artist if they aren't already tracked
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment genre count, or initialize if first occurrence
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment artist count, or initialize if first occurrence
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
