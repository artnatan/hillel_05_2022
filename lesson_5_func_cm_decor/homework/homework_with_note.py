# from pprint import pprint as print
from __future__ import annotations

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 12},
    {"name": "Cavin", "age": 17, "number": 3},
]


def repr_players(
    players: list[dict], sorted_: bool = False, keyword: str | None = "number"
) -> None:
    print("TEAM:")
    if sorted_:
        # NOTE: Here we don't wan't to change the source `team` variable.
        #       Better is create a deepcopy variable or think about another approach
        players.sort(key=lambda x: x[keyword])
    for pl in players:
        print(f"\t{pl['number']} Name:{pl['name']} Age:{pl['age']}")
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
            # NOTE: No need continue iteration
            break


def update_player(players: list[dict], num: int, name: str, age: int) -> None:
    index = 0
    while True:
        if index == len(players):
            log(message=f"There is no a player with #{num} to update")
            break

        elif num == players[index]["number"]:
            players[index]["name"] = name
            players[index]["age"] = age
            log(message=f"Update player with #{num}")
            break

        # NOTE: No need creating an additional `else` block here.
        index += 1
        continue


def main():
    repr_players(team)

    add_player(team, num=10, name="Cris", age=31)
    add_player(team, num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    repr_players(team, True)

    add_player(team, num=17, name="Bo", age=3)
    add_player(team, num=10, name="Borja", age=36)
    update_player(team, num=100, name="Alex", age=60)
    update_player(team, num=12, name="Alex", age=60)

    repr_players(team, True, "name")


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
