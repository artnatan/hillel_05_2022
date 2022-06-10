from typing import Generator

FILENAME = "./lesson_4_iter_gener_functions/generators/rockyou.txt"
SEARCH_KEYWORD = "admin"


def read_lines_find_admin() -> list:
    # results = []
    # with open(FILENAME, encoding="utf-8") as file:
    #     for word in file.readlines():
    #         if SEARCH_KEYWORD in word:
    #             results.append(word)

    # return results
    with open(FILENAME, encoding="utf-8") as file:
        return [word for word in file.readlines() if SEARCH_KEYWORD in word]


def bad_generator() -> Generator:
    with open(FILENAME, encoding="utf-8") as file:
        for line in file.readlines():
            yield line


def read_lines_find_admin_generator() -> Generator:
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                continue


# print("Lines 1: ", len(read_lines_find_admin()))
# print("Lines 2: ", read_lines_find_admin_generator())

# for line in read_lines_find_admin():
#     print(line)

for line in read_lines_find_admin_generator():
    print(line)
