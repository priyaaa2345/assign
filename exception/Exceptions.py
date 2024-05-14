class InvalidDataException(Exception):
    def __init__(self):
        super().__init__("No customer found with the given name.")


class InsufficientStockException(Exception):
    def __init__(self):
        super().__init__("The quantity mentioned is not available in the inventory")


class IncompleteOrderException(Exception):
    def __init__(self):
        super().__init__(" The product id mentioned is not in the orderdetails")


class PaymentException(Exception):
    def __init__(self):
        super().__init__("Exception:Payment not processed")


class AuthenticationException(Exception):
    def __init__(self):
        super().__init__(" Exception: Only Authorized User can enter")
