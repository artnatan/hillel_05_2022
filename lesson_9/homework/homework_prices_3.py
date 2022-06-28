from random import choice, randrange
from typing import Union

# list with dicts of exchange rates
exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.028},
    {"from": "USD", "to": "UAH", "value": 36},
    {"from": "EUR", "to": "USD", "value": 1.06},
    {"from": "USD", "to": "EUR", "value": 0.95},
    {"from": "ARS", "to": "USD", "value": 0.008},
    {"from": "USD", "to": "ARS", "value": 124.26},
]


# data generation for Price
class CreateData:
    @staticmethod
    def start(currency_list: list[str]) -> tuple:
        return randrange(1000, 20000, 1000), choice(currency_list)


# addition and subtraction operations
class Price:
    def __init__(self, amount: Union(int, float), currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __add__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount + other.amount), currency=self.currency)
        return instance

    def __sub__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount - other.amount), currency=self.currency)
        return instance


# currency conversion
class CurrencyExchange:
    def __init__(
        self, currency_base: str, price_add: "Price", exchange_rates: list[dict]
    ) -> None:
        self.currency_base = currency_base
        self.amount_add = price_add.amount
        self.currency_add = price_add.currency
        self.exchange_rates = exchange_rates

    def calculate(self) -> "Price":

        # if currencies are same
        if self.currency_base == self.currency_add:
            print(
                f"Currencies are the same, no conversion required \nPrice_B: {self.amount_add} {self.currency_add}"
            )
            return Price(self.amount_add, self.currency_add)

        # if Price B currency = USD
        elif self.currency_add == "USD":

            converted_price = self.exchange("to", self.amount_add, self.currency_base)
            print(
                f"Currency Price_B exchange done \nPrice_B: {converted_price} {self.currency_base}"
            )
            return Price(converted_price, self.currency_base)

        # if Price A currency = USD, but Price B currency is not
        elif self.currency_base == "USD":

            converted_price = self.exchange("from", self.amount_add, self.currency_add)
            print(
                f"Currency Price_B exchange done \nPrice_B: {converted_price} {self.currency_base}"
            )
            return Price(converted_price, self.currency_base)

        # double currency conversion
        else:

            variable_value = self.exchange("from", self.amount_add, self.currency_add)

            converted_price = self.exchange("to", variable_value, self.currency_base)
            print(
                f"Currency Price_B exchange done \nPrice_B: {converted_price} {self.currency_base}"
            )
            return Price(converted_price, self.currency_base)

    # calculation outside brackets
    def exchange(
        self, key_rate: str, amount: Union[float, int], currency: str
    ) -> float:
        index = 0
        while True:
            if exchange_rates[index][key_rate] == currency:
                return round(amount * exchange_rates[index]["value"], 2)
            index += 1


def main():

    # data generation for Price
    currency_list = list(set([value["from"] for value in exchange_rates]))
    data_a: tuple[int, str] = CreateData.start(currency_list)
    data_b: tuple[int, str] = CreateData.start(currency_list)

    # creat objects of class Price
    price_a = Price(data_a[0], data_a[1])
    price_b = Price(data_b[0], data_b[1])

    print(f"Price_A: {price_a.amount} {price_a.currency}")
    print(f"Price_B: {price_b.amount} {price_b.currency}")

    # conversion currency Price_B to currency Price_A
    price_b = CurrencyExchange(price_a.currency, price_b, exchange_rates).calculate()

    # operations on objects
    price_c = price_a + price_b
    print(f"Price_C = Price_A + Price_B: {price_c.amount} {price_c.currency}")

    price_c = price_a - price_b
    print(f"Price_C = Price_A - Price_B: {price_c.amount} {price_c.currency}")


if __name__ == "__main__":
    main()
