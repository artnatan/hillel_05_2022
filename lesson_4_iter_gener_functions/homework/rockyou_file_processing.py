from pprint import pprint as print
from typing import Generator

FILENAME = "./lesson_4_iter_gener_functions/homework/rockyou.txt"
SWARCH_KEYWORD = "user"


def read_file(FILENAME: str, SWARCH_KEYWORD: str) -> Generator:
    with open(FILENAME, encoding="ISO-8859-1") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SWARCH_KEYWORD in line:
                yield line.replace("\n", "")


def add_value(FILENAME: str, SWARCH_KEYWORD: str) -> tuple:
    results = []
    for line in read_file(FILENAME, SWARCH_KEYWORD):
        check = True
        while check:
            response = input(
                f"Add keyword '{line}' to list? 'Enter' to add or 'n' - no: "
            )
            if response == "":
                results.append(line)
                check = False
            elif response == "n":
                check = False
    return results, len(results)


result_list, result_len = add_value(FILENAME, SWARCH_KEYWORD)

print(f"list of keywords: {result_list}")
print(f"amount of added lines: {result_len}")
