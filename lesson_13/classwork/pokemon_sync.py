import random
from time import perf_counter

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 4
SIZE = 4

# import grequests
# urls = [get_random_pokemon_url() for _ in range(SIZE)]
# requests = (grequests.get(url) for url in urls)

# for response in grequests.map(requests):
#     if response:
#         random_pokemons.append(response.json()["name"])


def get_pokemon_sync(id_: str) -> str:
    url = BASE_URL + id_
    response = requests.get(url)

    return response.json()["name"]


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


def get_random_pokemon() -> str:
    random_id = get_random_id()
    return get_pokemon_sync(random_id)


def get_random_pokemon_url() -> str:
    random_id = get_random_id()
    return BASE_URL + str(random_id)


def sync_main():
    random_pokemons = []

    for _ in range(SIZE):
        pokemon = get_random_pokemon()
        random_pokemons.append(pokemon)

    print(f"Pokemons: {random_pokemons}")


def main():
    print("=" * 30)

    # NOTE: Sync run
    start_time = perf_counter()
    sync_main()
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time}")


if __name__ == "__main__":
    main()
