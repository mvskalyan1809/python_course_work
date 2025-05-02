# prompt: i want soptify music songs play list with using of def yield 

import random

def generate_playlist(num_songs):
  """Generates a playlist of Spotify song titles using a generator."""

  song_titles = [
    
  ]

  for _ in range(num_songs):
    yield random.choice(song_titles)


# Example usage
playlist_length = 5
my_playlist = generate_playlist(playlist_length)

print("My Spotify Playlist:")
for song in my_playlist:
  song1
  song2
  song3

