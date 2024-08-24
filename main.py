import spotipy
from argparse import ArgumentParser
from dotenv import load_dotenv
import os

# For local developement
load_dotenv()

def connectUser(id: str, secret: str) -> spotipy.Spotify:
    '''Connects the user to the API'''

    scope = "user-library-read"

    auth_manager = spotipy.SpotifyOAuth(client_id=id, 
                                        client_secret=secret, 
                                        redirect_uri="http://localhost:8000", 
                                        scope=scope)

    return spotipy.Spotify(auth_manager=auth_manager)



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('username', help="Username", nargs='?', default="")
    parser.add_argument('api_token', help="API Token", nargs='?', default="")
    args = parser.parse_args()

    print("Hello World!")

    #connectUser(args.username, args.api_token)
    sp = connectUser(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
