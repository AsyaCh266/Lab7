class FakePaymentGateway:
    def _init(self):
        self.charges = []

    def charge(self, order_id, money):
        self.charges.append((order_id, money.amount))
