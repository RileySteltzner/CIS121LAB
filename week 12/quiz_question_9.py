class Playlist:
    def __init__(self, name = "New Playlist", songs = []):
        self.name = name
        self.songs = songs
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __add__(self, other):
        combined_songs = {self.songs} + {other.songs}
        return combined_songs
    def __str__(self):
        return f"{self.name} has the songs {self.songs} in the playlist"


p1 = Playlist("x", {"SongA", "SongB"})
p2 = Playlist("y", {"SongC"})
combined = p1 + p2
print(combined)