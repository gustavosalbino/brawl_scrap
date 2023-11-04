from datetime import datetime

from reader import get_last_log_path, read_battle_log_items
from scrapper import scrap_selected_player_recent_battle_log
from writer import write_battle_log

# PLAYERS_TAG_LIST = ["GUSTAVO", "PRUDENTE" "JESSE"]
PLAYERS_TAG_LIST = ["%232LCR8UUGP", "%2328PYC9PVC", "%239LCPUQ8U"]


for player in PLAYERS_TAG_LIST:

    # Create player folder if it does not exist
    folder = f"data/{player}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Get most recent 25 battles
    battle_log, request_time = scrap_selected_player_recent_battle_log(player)

    # Get last battle in history
    most_recent_log_path = get_last_log_path(player)
    if most_recent_log_path is not None:
        most_recent_battle = read_battle_log_items(most_recent_log_path)[0]
    else:
        most_recent_battle = {"battleTime": "19000101T000000.000Z"}

    # Filter out battles already logged
    battle_time_format = "%Y%m%dT%H%M%S.000Z"
    last_battle_time_logged = datetime.strptime(most_recent_battle.get('battleTime'), battle_time_format)
    battle_log["items"] = list(map(lambda x: x if datetime.strptime(x.get('battleTime'), battle_time_format)
                                   > last_battle_time_logged else None, battle_log["items"]))
    battle_log["items"] = list(filter(lambda x: x is not None, battle_log["items"]))

    # Save battles in player's history
    if battle_log["items"]:
        write_battle_log(battle_log=battle_log, player_tag=player, request_time=request_time)
