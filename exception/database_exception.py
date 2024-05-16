class DatabaseException(Exception):
    def __init__(self):
        super().__init__("Sql Exception..checking credentials")
