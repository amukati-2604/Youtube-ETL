import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

YOUR_API_KEY = os.getenv("YOUR_API_KEY")
CHANNEL_NAME = "MrBeast"

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_NAME}&key={YOUR_API_KEY}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistId)
        return channel_playlistId
    except requests.exceptions.Requestxception as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()

