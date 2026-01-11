class PayOrderUseCase:
    def _init(self, order_repo, payment_gateway):
        self.order_repo = order_repo
        self.payment_gateway = payment_gateway

    def execute(self, order_id):
        order = self.order_repo.get_by_id(order_id)
        money = order.total()

        order.pay()
        self.payment_gateway.charge(order.id, money)

        self.order_repo.save(order)
        return money
