class InsufficientStockException(Exception):
    def __init__(self):
        super().__init__("The quantity mentioned is not available in the inventory")
