class InMemoryOrderRepository:
    def _init(self):
        self.orders = {}

    def get_by_id(self, order_id):
        return self.orders[order_id]

    def save(self, order):
        self.orders[order.id] = order
