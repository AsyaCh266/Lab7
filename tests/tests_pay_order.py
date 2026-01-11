import pytest
from domain.order import Order, OrderLine
from domain.money import Money
from application.pay_order import PayOrderUseCase
from infrastructure.repository import InMemoryOrderRepository
from infrastructure.payment import FakePaymentGateway


def create_order():
    order = Order("1")
    order.add_line(OrderLine("Book", Money(100), 2))
    return order


def test_successful_payment():
    repo = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    order = create_order()
    repo.save(order)

    use_case = PayOrderUseCase(repo, payment)
    result = use_case.execute("1")

    assert result.amount == 200
    assert order.status == "PAID"


def test_empty_order():
    repo = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    order = Order("2")
    repo.save(order)

    use_case = PayOrderUseCase(repo, payment)

    with pytest.raises(ValueError):
        use_case.execute("2")


def test_double_payment():
    repo = InMemoryOrderRepository()
    payment = FakePaymentGateway()
    order = create_order()
    repo.save(order)

    use_case = PayOrderUseCase(repo, payment)
    use_case.execute("1")

    with pytest.raises(ValueError):
        use_case.execute("1")


def test_no_change_after_payment():
    order = create_order()
    order.pay()

    with pytest.raises(ValueError):
        order.add_line(OrderLine("Pen", Money(10), 1))


def test_total_calculation():
    order = Order("3")
    order.add_line(OrderLine("A", Money(50), 2))
    order.add_line(OrderLine("B", Money(30), 1))

    assert order.total().amount == 130
