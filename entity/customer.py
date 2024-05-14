class Customer:
    def __init__(self, CustomerId, FirstName, LastName, Email, Phone, Address):
        self.__CustomerId = CustomerId
        self.__FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.__Phone = Phone
        self.__Address = Address

    def get_customerid(self):
        return self.__CustomerId

    def set_customerid(self, CustomerId):
        self.__CustomerId = CustomerId

    def get_firstname(self):
        return self.__FirstName

    def set_firstname(self, FirstName):
        self.__FirstName = FirstName

    def get_phone(self):
        return self.__Phone

    def set_phone(self, Phone):
        self.__Phone = Phone

    def get_address(self):
        return self.__Address

    def set_address(self, Address):
        self.__Address = Address
