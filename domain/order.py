from domain.money import Money
from domain.status import OrderStatus


class OrderLine:
    def _init(self, name: str, price: Money, qty: int):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return Money(self.price.amount * self.qty)


class Order:
    def _init(self, order_id: str):
        self.id = order_id
        self.lines = []
        self.status = OrderStatus.CREATED

    def add_line(self, line: OrderLine):
        if self.status == OrderStatus.PAID:
            raise ValueError("Невозможно изменить оплаченный заказ")
        self.lines.append(line)

    def total(self):
        total = Money(0)
        for l in self.lines:
            total = total.add(l.total())
        return total

    def pay(self):
        if not self.lines:
            raise ValueError("Не удается оплатить пустой заказ")
        if self.status == OrderStatus.PAID:
            raise ValueError("Заказ уже оплачен")
        self.status = OrderStatus.PAID
