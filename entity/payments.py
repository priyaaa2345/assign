# created for handling payment processing exception


class Payments:
    def __init__(self, payment_id, order_id, amount, status, payment_date):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.status = status
        self.payment_date = payment_date
