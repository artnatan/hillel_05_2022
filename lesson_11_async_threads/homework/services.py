# from random import randint
from statistics import mean


class DataWork:
    @staticmethod
    def sum_elem_list(num_list: list[int], number: int) -> None:
        print(f"Thread {number} completed. Sum = {sum(num_list)}")

    @staticmethod
    def mean_elem_list(num_list: list[int], number: int) -> None:
        print(f"Thread {number} completed. Mean = {round(mean(num_list), 2)}")
