from random import randint
from statistics import mean
from threading import Event, Thread
from typing import Coroutine


class ThreadsWork:
    def __init__(self, amount: int, event: Coroutine) -> None:
        self.num_list = []
        self.amount = amount
        self.event = event

    def sum_elem_list(self, number: int) -> None:

        self.event.wait()
        print(f"Thread {number} completed. Sum = {sum(self.num_list)}")

    def mean_elem_list(self, number: int) -> None:

        self.event.wait()
        print(f"Thread {number} completed. Mean = {round(mean(self.num_list), 2)}")

    def get_random_list_int(self, number: int) -> None:

        self.num_list = [randint(0, 100) for _ in range(self.amount)]
        print(f"Thread {number} completed. List formed.")
        self.event.set()


def main():

    amount = 10000
    event = Event()
    td = ThreadsWork(amount, event)

    threads = [
        Thread(
            target=td.get_random_list_int,
            kwargs={"number": 1},
        ),
        Thread(
            target=td.sum_elem_list,
            kwargs={"number": 2},
        ),
        Thread(
            target=td.mean_elem_list,
            kwargs={"number": 3},
        ),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
