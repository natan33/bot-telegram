import json
import os
from pathlib import Path

def obter_credencias():
    config = "config"
    path_file = f"{Path(os.getcwd())/ "bot_telegram" / config}.json"
    with open(path_file) as file:
        obtem_credencias = json.load(file) 

    return obtem_credencias

credencias = obter_credencias()

CHAVE_API = str(credencias["BOT_TELEGRAM"]["CHAVE_BOT"])
URL_API = str(credencias["BOT_TELEGRAM"]["LINK_BOT"])