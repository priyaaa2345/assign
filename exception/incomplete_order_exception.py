class IncompleteOrderException(Exception):
    def __init__(self):
        super().__init__(" The product id mentioned is not in the orderdetails")
