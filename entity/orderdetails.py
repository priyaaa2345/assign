class OrderDetails:
    def __init__(self, OrderDetailID, OrderID, ProductID, Quantity):
        self.__OrderDetailID = OrderDetailID
        self.__OrderID = OrderID
        self.__ProductID = ProductID
        self.__Quantity = Quantity

    def get_orderid(self):
        return self.__OrderID

    def set_orderid(self, OrderID):
        self.__OrderID = OrderID

    def set_productid(self, ProductID):
        self.__ProductID = ProductID

    def get_productid(self):
        return self.__ProductID

    def set_quantity(self, Quantity):
        self.__Quantity = Quantity

    def get_quantity(self):
        return self.__Quantity

    def get_orderdetailid(self):
        return self.__OrderDetailID

    def set_orderdetailid(self, OrderDetailID):
        self.__OrderDetailID = OrderDetailID
