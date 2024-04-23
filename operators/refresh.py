"""
Generates a new access token on each run
"""

import base64
import requests
import os

class RefreshToken:
    def __init__(self):
        self.refresh_token = os.getenv("REFRESH_TOKEN")
        self.base_64 = ""
    def get_auth_base64(self):
        auth_string = os.getenv("CLIENT_ID") + ":" + os.getenv("CLIENT_SECRET")
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
        self.base_64 = auth_base64
        return auth_base64
    
    def refresh(self):
        self.get_auth_base64()
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(
            query,
            data={"grant_type": "refresh_token", "refresh_token": self.refresh_token},
            headers={"Authorization": "Basic " + self.base_64},
        )

        response_json = response.json()

        return response_json["access_token"]

if __name__ == "__main__":
    new_token = RefreshToken()
    new_token.refresh()
