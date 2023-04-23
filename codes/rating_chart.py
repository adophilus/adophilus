from collections import namedtuple
import datetime
import math
import json
import os
import sys
import asciichartpy as ac
import requests
from urllib.parse import urlencode

USERNAME = "adophilus"
NGAMES = 100
GAMES_URL = f"https://lichess.org/api/games/user/{USERNAME}?" + urlencode(
    {"rated": "true", "perfType": "rapid", "moves": "false", "max": NGAMES}
)


def getGames() -> list:
    req = requests.get(GAMES_URL, headers={"Accept": "application/x-ndjson"})
    return map(lambda g: json.loads(g), filter(None, req.text.split("\n")))


def main():
    games = getGames()
    ratings = list(
        map(
            lambda g: g["players"]["white"]["rating"]
            if (g["players"]["white"]["user"]["name"] == USERNAME)
            else g["players"]["black"]["rating"],
            games,
        )
    )
    return ac.plot(ratings, {"height": 15})


if __name__ == "__main__":
    plot = main()
    print(plot)
