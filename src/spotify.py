import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyInit:
    """
    Class to initialize Spotify Developer Object. Contains OAuth and User Set
    """
    def __init__(self, client_id, client_secret, redirect_uri, username):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.username = username
        self.auth = None
        self.user_id = None

    def spotify_auth(self):
        """
        What this function does?

        Argument:

        Returns:
        """
        auth = SpotifyOAuth(client_id= self.client_id, 
                            client_secret= self.client_secret,
                            redirect_uri= self.redirect_uri,
                            scope= "playlist-modify-private",
                            show_dialog= True,
                            # cache_path = "token.txt",
                            username= self.username)
        
        self.auth=auth

    def set_user(self):
        """
        What this function does?

        Argument:

        Returns:
        """
        if self.auth is not None:
            sp = spotipy.Spotify(auth_manager = self.auth)
            self.sp = sp
            self.user_id = sp.current_user()['id']
        else:
            raise AttributeError("Authorisation Object not set! Please complete Spotify OAuth")

