class Products:
    def __init__(self, ProductID, ProductName, Description, Price):
        self.__ProductID = ProductID
        self.ProductName = ProductName
        self.Description = Description
        self.__Price = Price

    def set_productid(self, ProductID):
        self.__ProductID = ProductID

    def get_productid(self):
        return self.__ProductID

    def get_price(self):
        return self.__Price

    def set_price(self, Price):
        self.__Price = Price
