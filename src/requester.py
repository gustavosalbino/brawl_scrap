from typing import Optional

import requests
import os

API_ADDRESS = "https://api.brawlstars.com/v1"

API_KEY = os.getenv('API_KEY')

API_PROXY_ADDRESS = "https://bsproxy.royaleapi.dev/v1"


def request_player_recent_battle_log(player_tag: str, params: Optional[str]=None):
    return requests.get(f'{API_PROXY_ADDRESS}/players/{player_tag}/battlelog',
                        headers={'Authorization': f'Bearer {API_KEY}'},
                        params=params)
