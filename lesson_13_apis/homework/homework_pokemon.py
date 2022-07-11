import asyncio
import random

from aiohttp import ClientSession

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 200
AMOUNT = 100


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_random_pokemon(session: ClientSession) -> str:
    url = BASE_URL + get_random_id()

    async with session.get(url) as response:
        res = await response.json()
        return res["name"]


async def main():
    async with ClientSession() as session:
        tasks = [get_random_pokemon(session) for _ in range(AMOUNT)]
        results = await asyncio.gather(*tasks)
        print(f"Pokemon collection: {results}")


if __name__ == "__main__":
    asyncio.run(main())
