from random import choice, randrange

exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.028},
    {"from": "USD", "to": "UAH", "value": 36},
    {"from": "EUR", "to": "USD", "value": 1.06},
    {"from": "USD", "to": "EUR", "value": 0.95},
    {"from": "ARS", "to": "USD", "value": 0.008},
    {"from": "USD", "to": "ARS", "value": 124.26},
]


class CreateData:
    @staticmethod
    def start(currency_list: list[str]) -> tuple:
        return randrange(1000, 20000, 1000), choice(currency_list)


class Price:
    def __init__(self, data: tuple, exchange_rates: list[dict]) -> None:
        self.amount: int = data[0]
        self.currency: str = data[1]
        self.exchange_rates: list[dict] = exchange_rates

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(amount=(self.amount + other.amount), currency=self.currency)

        else:
            converted_price = CurrencyExchange.exchange_currency(self, other)
            return Price(amount=(self.amount + converted_price), currency=self.currency)


class CurrencyExchange(Price):
    def exchange_currency(self, variable_price: "Price") -> float:
        if variable_price.currency == "USD":

            return self.calculate_at_rate("from", variable_price.amount)

        else:

            variable_value_usd = self.calculate_at_rate("from", variable_price.amount)

            return self.calculate_at_rate("to", variable_value_usd)

    def calculate_at_rate(self, key_rate, variable_price_value: int) -> float:
        index = 0
        while True:
            if self.exchange_rates[index][key_rate] == self.currency:
                return variable_price_value * self.exchange_rates[index]["value"]
            index += 1


def main():
    currency_list = list(set([value["from"] for value in exchange_rates]))

    price_a = Price(CreateData.start(currency_list), exchange_rates)
    price_b = Price(CreateData.start(currency_list), exchange_rates)

    print(price_a.amount, price_a.currency)
    print(price_b.amount, price_b.currency)

    total_price = price_a + price_b
    print(total_price)


if __name__ == "__main__":
    main()
