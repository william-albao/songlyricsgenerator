# Import libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius as lg

# Replace with your own Spotify credentials
CLIENT_ID = '###########################'
CLIENT_SECRET = '############################'
REDIRECT_URI = 'http://localhost:3000'

# Replace with your own Genius credentials
GENIUS_ACCESS_TOKEN = "#############################"

# Create the SpotifyOAuth instance
sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope='user-read-playback-state')

# Get the access token
access_token = sp_oauth.get_cached_token()['access_token']

# Create a Spotipy and Genius instance with the access token
sp = spotipy.Spotify(auth=access_token)
genius = lg.Genius(GENIUS_ACCESS_TOKEN)

# Function to get the lyrics using Genius API and LyricsGenius library
def get_lyrics(song_title, artist_name):
    song = genius.search_song(artist_name, song_title)
    return song.lyrics

# Get the current playback
curr_playback = sp.current_playback()
if curr_playback and curr_playback['is_playing']:
    track = curr_playback['item']
    print("Song Title: ", track['name'])
    song_title = track['name']
    for artist in track['artists']:
        print("Artist Name: ", artist['name'])  
        artist_name = artist['name']

    lyrics = get_lyrics(song_title, artist_name)
    if lyrics:
        print(lyrics)
    else:
        print("Lyrics not found")
else:
    print("No music currently playing")


