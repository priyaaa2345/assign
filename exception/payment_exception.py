class PaymentException(Exception):
    def __init__(self):
        super().__init__("Exception:Payment failed..Initiate retry")
