EN:
- Create a class `Price`
    ```python
        class Price:
            def __init__(self, amount: int, currency: str) -> None:
                self.amount: int = amount
                self.currency: str = currency
    ```
- Acceptance criterias:
    - If I create 2 instances of a `Price` class I want to do operations between them:
        - add prices with same currency
        - do a subtricttion of prices with same currency

- *Additional: operations between prices with different currencies:
    - If price instances currencies are different I want to do a convertion
        - USD is a middle currency
        - If any prices currency is USD convertion is not happening
        - Result currency after the operation is a currency of the price that is on the left or USD (for your decision)

UA:
- Ставоріть клас `Price`
    ```python
        class Price:
            def __init__(self, amount: int, currency: str) -> None:
                self.amount: int = amount
                self.currency: str = currency
    ```
- Вимоги:
    - Якщо я створюю 2 екземпляри класу `Price` я хочу мати можливість виконувати між ними наступні операції:
        - Додавати ціни з однаковими валютами
        - Віднімати ціни з однаковими валютами

- *Додатково: операції з цінаи, у яких різні валюти:
    - Якщо у двох цін відрізняються валюти повинна відбуватись повдійня конвертація
        - USD використовується для проміжуточної конвертації
        - Якщо у цін однакові валюти - конвертація не відбувається
        - Після операції над цінами - кінцева валюта - така ж як і лівого операнда, або USD (на Ваш вибір)