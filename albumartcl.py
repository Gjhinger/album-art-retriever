import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import sys


def get_dir():
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Trilogy'
    return name


def get_art(aname, spotify):
    results = spotify.search(q='album:' + aname, type='album')
    items = results['albums']['items']
    if len(items) > 0:
        album = items[0]
        print(album['name'], album['images'][0]['url'])
        webbrowser.open(album['images'][0]['url'])


def main():
    aname = get_dir()
    cid = 'Client ID'
    secret = 'Secret ID'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    get_art(aname, spotify)


if __name__ == '__main__':
    main()
