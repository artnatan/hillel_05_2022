# from pprint import pprint as print
from __future__ import annotations

LOGGING = True
keyword = "number"
sort_param = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 12},
    {"name": "Cavin", "age": 17, "number": 3},
]


def repr_players(
    players: list[dict], sorted: bool = False, keyword: str | None = "number"
) -> None:
    print("TEAM:")
    if sorted:
        players.sort(key=lambda x: x[keyword])
    for player in players:
        print(f"\t{player['number']} Name:{player['name']}Age:{player['age']}")
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def add_player(players: list[dict], num: int, name: str, age: int) -> None:
    if num not in [player["number"] for player in players]:
        player = {"name": name, "age": age, "number": num}
        team.append(player)
        log(message=f"Adding {player['name']}")
    else:
        log(message=f"There is already a player with #{num}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def update_player(players: list[dict], num: int, name: str, age: int) -> None:

    check_player = True
    for player in players:
        if num == player["number"]:
            player["name"] = name
            player["age"] = age
            log(message=f"Update player with #{num}")
            check_player = False
    if check_player:
        log(message=f"There is no a player with #{num} to update")


def main():
    repr_players(team)

    add_player(team, num=10, name="Cris", age=31)
    add_player(team, num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    repr_players(team, True)

    add_player(team, num=17, name="Bo", age=3)
    add_player(team, num=10, name="Borja", age=36)
    update_player(team, num=100, name="Alex", age=60)
    update_player(team, num=1, name="Alex", age=60)

    repr_players(team, True, "name")


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
