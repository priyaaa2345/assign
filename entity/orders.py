class Orders:
    def __init__(self, OrderID, CustomerID, OrderDate, TotalAmount):
        self.__OrderID = OrderID
        self.__CustomerID = CustomerID
        self.__OrderDate = OrderDate
        self.__TotalAmount = TotalAmount

    def get_orderid(self):
        return self.__OrderID

    def set_orderid(self, OrderID):
        self.__OrderID = OrderID

    def get_customerid(self):
        return self.__CustomerID

    def set_customerid(self, CustomerID):
        self.__CustomerID = CustomerID

    def get_orderdate(self):
        return self.__OrderDate

    def set_OrderDate(self, OrderDate):
        self.__OrderDate = OrderDate

    def get_TotalAmount(self):
        return self.__TotalAmount

    def set_totalamount(self, TotalAmount):
        self.__TotalAmount = TotalAmount
