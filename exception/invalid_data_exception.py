class InvalidDataException(Exception):
    def __init__(self):
        super().__init__("No customer found with the given name.")
