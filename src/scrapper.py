from datetime import datetime
from typing import Tuple

from src.requester import request_player_recent_battle_log


def scrap_selected_player_recent_battle_log(player_tag: str) -> Tuple[dict, datetime]:
    battle_log = request_player_recent_battle_log(player_tag)
    if battle_log.status_code == 200:
        return battle_log.json(), datetime.utcnow()
    else:
        raise Exception(f"Error to process request. Response error code: {battle_log.status_code}."
                        f"\n{battle_log.text}")


scrap_selected_player_recent_battle_log("%232LCR8UUGP")
