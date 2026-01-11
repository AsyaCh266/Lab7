class Money:
    def _init(self, amount: int):
        if amount < 0:
            raise ValueError("Деньги не могут быть отрицательными")
        self.amount = amount

    def add(self, other):
        return Money(self.amount + other.amount)
