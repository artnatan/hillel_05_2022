from random import choice, randrange

exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.028},
    {"from": "USD", "to": "UAH", "value": 36},
    {"from": "EUR", "to": "USD", "value": 1.06},
    {"from": "USD", "to": "EUR", "value": 0.95},
    {"from": "ARS", "to": "USD", "value": 0.008},
    {"from": "USD", "to": "ARS", "value": 124.26},
]


class Price:
    def __init__(self, amount: int, currency: str, exchange_rates: list[dict]) -> None:
        self.amount: int = amount
        self.currency: str = currency
        self.exchange_rates = exchange_rates

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return self.amount + other.amount

        else:
            converted_price = CurrencyExchange.exchange_currency(
                other, self.currency, self.exchange_rates
            )
            return self.amount + converted_price


class CurrencyExchange:
    @staticmethod
    def exchange_currency(
        variable_price: "Price", base_currency: str, rates: list[dict]
    ) -> float:
        if variable_price.currency == "USD":
            index = 0
            while True:
                if rates[index]["to"] == base_currency:
                    return variable_price.amount * rates[index]["value"]
                index += 1

        else:

            index = 0
            while True:
                if rates[index]["from"] == variable_price.currency:
                    variable_value_usd = variable_price.amount * rates[index]["value"]
                    break
                index += 1

            index = 0
            while True:
                if rates[index]["to"] == base_currency:
                    return variable_value_usd * rates[index]["value"]
                index += 1

    # def calculate_at_rate(rates, key_rate, base_currency, variable_price):
    #     index = 0
    #     while True:
    #         if rates[index][key_rate] == base_currency:
    #             return variable_price.amount * rates[index]["value"]
    #         index += 1


def main():
    currency_list = list(set([value["from"] for value in exchange_rates]))
    # price_value = randrange(1000, 20000, 1000)

    choice(currency_list)

    price_a = Price(randrange(1000, 20000, 1000), choice(currency_list), exchange_rates)
    price_b = Price(randrange(1000, 20000, 1000), choice(currency_list), exchange_rates)

    print(price_a.amount, price_a.currency)
    print(price_b.amount, price_b.currency)

    total_price = price_a + price_b
    print(total_price)


if __name__ == "__main__":
    main()


# class CurrencyExchange:
#     @classmethod
#     def calculate(
#         cls, price_base: Price, price_add: Price, exchange_rates: list[dict]
#     ) -> "Price":
#         cls.amount_base = price_base.amount
#         cls.currency_base = price_base.currency
#         cls.amount_add = price_add.amount
#         cls.currency_add = price_add.currency
#         cls.exchange_rates = exchange_rates

#         if cls.currency_base == cls.currency_add:
#             return Price(((cls.amount_base + cls.amount_add), cls.currency_base))

#         else:
#             converted_price = cls.exchange_currency()
#             return Price(((cls.amount_base + converted_price), cls.currency_base))

#     @classmethod
#     def exchange_currency(cls) -> float:
#         if cls.currency_add == "USD":

#             index = 0
#             while True:
#                 if cls.exchange_rates[index]["to"] == cls.currency_base:
#                     return cls.amount_add * cls.exchange_rates[index]["value"]
#                 index += 1

#         else:

#             index = 0
#             while True:
#                 if cls.exchange_rates[index]["from"] == cls.currency_add:
#                     variable_value = cls.amount_add * cls.exchange_rates[index]["value"]
#                     break
#                 index += 1

#             index = 0
#             while True:
#                 if cls.exchange_rates[index]["to"] == cls.currency_base:
#                     return variable_value * cls.exchange_rates[index]["value"]
#                 index += 1
