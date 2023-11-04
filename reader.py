import json
import os
from datetime import datetime
from functools import reduce
from typing import List, Optional


def read_battle_log_items(path: str) -> List[dict]:
    with open(path, "r") as file:
        return json.load(file)["items"]


def get_last_log_path(player_tag: str) -> Optional[str]:
    files = os.listdir(f"data/{player_tag}")
    if files:
        return f"data/{player_tag}/{reduce(_compare_log_names, files)}"
    return None


def _compare_log_names(log_1, log_2, str_format: str = "%Y-%m-%d %H:%M:%S.json"):
    if datetime.strptime(log_1, str_format) > datetime.strptime(log_2, str_format):
        return log_1
    elif datetime.strptime(log_2, str_format) > datetime.strptime(log_1, str_format):
        return log_2
    else:
        raise Exception(f"Log files containing same request time. Log 1: {log_1}. Log 2: {log_2}")
