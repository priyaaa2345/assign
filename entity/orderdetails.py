class OrderDetails:
    def __init__(self, OrderDetailID, OrderID, ProductID, Quantity, order, product):
        self.__OrderDetailID = OrderDetailID
        self.__OrderID = OrderID
        self.__ProductID = ProductID
        self.__Quantity = Quantity
        self.__order = order
        self.__product = product

    def get_orderid(self):
        return self.__OrderID

    def set_orderid(self, OrderID):
        self.__OrderID = OrderID

    def set_productid(self, ProductID):
        self.__ProductID = ProductID

    def get_productid(self):
        return self.__ProductID

    def set_quantity(self, Quantity):
        if Quantity >= 0:
            self.__Quantity = Quantity
        else:
            raise ValueError("Price must be positive integers")

    def get_quantity(self):
        return self.__Quantity

    def get_orderdetailid(self):
        return self.__OrderDetailID

    def set_orderdetailid(self, OrderDetailID):
        self.__OrderDetailID = OrderDetailID

    # task 4 composition
    def order(self):
        return self.__order

    def product(self):
        return self.__product

    # eg : print("Product Name:", order_detail.product.ProductName)
