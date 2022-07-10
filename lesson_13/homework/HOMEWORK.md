## <span style="color:green">Homework</span>

```python
import httpx

def get_random_id() -> str:
    ...

async def get_random_pokemon() -> str:
    url = BASE_URL + get_random_id()

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.["name"]

async def main():
    tasks = [get_random_pokemon() for _ in range(100)]
    results = asyncio.gather(tasks)
    print(results)

asyncio.run(main())
```

EN:
    - Repeat classwork async pokemon example with `aiohttp` library rather than `httpx`
    - You should base on the example above
    - There are mistakes in the code sample
UA:
    - Повторити приклад з уроку з асинхронним отриманням покемонів з використанням бібліотеки `aiohttp` замість `httpx`
    - За сонову взяти приклад вище
    - У прикладі коду є помилки