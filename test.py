import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from requests import post, get
import json
import base64
# Thực hiện xác thực
client_id='2ed7b10402494723a6f28c396d576e5d'
client_secret='76d5317b083645e4a390eac819063851'
redirect_uri='http://localhost:9009'
scope='user-read-recently-played'

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    header ={
        "Authorization" : "Basic " + auth_base64,
        "Content-type" : "application/x-www-form-urlencoded"
    }
    data = {
     "grant_type": "client_credentials",
     "scope": scope
}
    result = post(url, headers=header, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token
def get_recently(number: int, token: str):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer " + token,
    }
    params = [
        ("limit", number),
    ]
    try:
        response = get(
            "https://api.spotify.com/v1/me/player/recently-played",
            headers=headers,
            params=params,
            timeout=10,
        )
        return (response.status_code, response.json())
    except:
        return None
    
token = get_token()
print(token)
recently_played_tracks = get_recently(2, token)
print(recently_played_tracks)
