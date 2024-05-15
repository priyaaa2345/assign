class Orders:
    def __init__(self, OrderID, CustomerID, OrderDate, TotalAmount, customer):
        self.__OrderID = OrderID
        self.__CustomerID = CustomerID
        self.__OrderDate = OrderDate
        self.__TotalAmount = TotalAmount
        self.__customer = customer

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

    def set_sort_orders_by_date(self, OrderDate):
        self.__OrderDate = OrderDate

    # task 4 composition
    # creating a private obj from custmers clas
    def get_customer(self):
        self.__customer


# example usage
# Creating an order object with composition relationship
# order = Orders("O001", customer.customer_id, "2024-05-15", 100.0, customer)
