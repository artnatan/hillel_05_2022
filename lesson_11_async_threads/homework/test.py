import asyncio

NUMBERS = [40000, 400, 100000, 700]


async def get_primes_amount(num: int) -> int:
    results = 0
    for i in range(2, num + 1):
        prime_num = True
        counter = 0
        for j in range(2, i + 1):
            if i % j == 0:
                counter += 1
            if counter > 1:
                prime_num = False
                break
        if prime_num:
            results += 1
    print(f"in sequence of numbers from 2 to {num} - {results} primes")
    return {num: results}


async def async_main():
    tasks = [get_primes_amount(num) for num in NUMBERS]
    results = await asyncio.gather(*tasks)
    print(results)


def main():

    asyncio.run(async_main())

    tasks = []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    # tasks = [get_primes_amount(i) for i in numbers]

    # loop = asyncio.get_event_loop()
    # results = loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()
    # print(results)


if __name__ == "__main__":
    main()
