import json
from datetime import datetime
from typing import Optional


def write_battle_log(player_tag: str, battle_log: dict, request_time: Optional[datetime] = None,
                     str_format: str = "%Y-%m-%d %H:%M:%S"):
    folder = f"data/{player_tag}"

    formatted_time = request_time.strftime(str_format)
    save_relative_path = f"{folder}/{formatted_time}.json"

    json_battle_log = json.dumps(battle_log, indent=4)
    with open(save_relative_path, "w") as output_file:
        output_file.write(json_battle_log)
