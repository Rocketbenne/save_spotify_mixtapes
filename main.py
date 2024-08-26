import spotipy
from argparse import ArgumentParser
from dotenv import load_dotenv
import os

load_dotenv()  # for local developement

def connectUser(id: str, secret: str) -> spotipy.Spotify:
    """ Connects the user to the API
    @param id: Client ID
    @param secret: Client Secret
    @return: Spotify API client"""
    
    sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=id,
                                                                       client_secret=secret))
    return sp


if __name__ == "__main__":
    # Parse console arguments
    parser = ArgumentParser()
    parser.add_argument('client_id', help="Username", nargs='?', default="")
    parser.add_argument('client_secret', help="API Token", nargs='?', default="")
    args = parser.parse_args()

    # Connect user to Spotify API
    sp = connectUser(args.client_id, args.client_secret)
    #sp = connectUser(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))  # for local developement

    #  Search for Weezer songs
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
