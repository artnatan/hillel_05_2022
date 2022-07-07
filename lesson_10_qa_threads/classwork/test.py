from typing import Callable

# from dataclasses import dataclass

# @dataclass
# class UserData:
#     username: str = ""
#     password: str = ""


# user_data = UserData(username="", password="")


# def validate_password(user_data: UserData) -> None:
#     if len(user_data.password) < 8:
#         raise ValueError("Password is too less")


def validate_password(user_data: tuple[str, str]) -> None:
    _, password = user_data
    if len(password) < 8:
        raise ValueError("Password is too less")


def validate_username(user_data: tuple[str, str]) -> None:
    username, _ = user_data
    if username.isnumeric():
        raise ValueError("U can't be a num")


def change_me(user_data: tuple[str, str], validators: list[Callable]) -> bool:
    username, _ = user_data
    for validator in validators:
        validator(user_data)

    print(f"{username} updated in database")

    return True


def signup(user_data: tuple[str, str], validators: list[Callable]) -> bool:
    username, _ = user_data
    for validator in validators:
        validator(user_data)

    print(f"{username} saved in database")

    return True


def main():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    user_data = (username, password)

    result = signup(user_data, [validate_username])

    if result is True:
        print("Welcome")
    else:
        print("Bye")

    new_data = ("new_username", "wqeqweqwe")
    user_updated = change_me(
        new_data,
        [
            validate_password,
            validate_username,
        ],
    )

    if user_updated is True:
        print("Done")


if __name__ == "__main__":
    main()
