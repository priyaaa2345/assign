import pyodbc

server_name = "MSI\SQLEXPRESS"
database_name = "TechShop"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("select 1")
print("database is connected")
print("Welcome to TECHSHOP 📲🎧⚡")


# TASK 1: CREATING CLASSES: ✅
# Task 2: Class Creation: ✅
# • Create the classes (Customers, Products, Orders, OrderDetails and Inventory) with the specified
# attributes.
# • Implement the constructor for each class to initialize its attributes.
# • Implement methods as specified
class Customers:
    def read_customers(self):
        cursor.execute("select * from Customers")
        for row in cursor:
            print(row)

    def __init__(self, CustomerId, FirstName, LastName, Email, Phone, Address):
        self.CustomerId = CustomerId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Phone = Phone
        self.Address = Address

    def CalculateTotalOrders(self, CustomerId):
        cursor.execute(
            """
                    select count(Customers.CustomerId) from Customers
                    inner join orders on
                    Customers.CustomerId=Orders.CustomerId
                    where Customers.CustomerId=?
                    group by Customers.CustomerId
                    """,
            (CustomerId),
        )
        conn.commit()

    def GetCustomerDetails():
        pass

    def UpdateCustomerInfo():
        pass


# customers_instance = Customers(None, None, None, None, None, None)
# customers_instance.read_customers()
total = Customers(Customers.CustomerId)
total_orders = total.CalculateTotalOrders(Customers.CustomerId)
print("the total order for the given customer is : ", total_orders)


class Products:
    def __init__(self, ProductID, ProductName, Description, Price):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Description = Description
        self.Price = Price

    def GetProductDetails():
        pass

    def UpdateProductInfo():
        pass

    def IsProductInStock():
        pass


class Orders:
    def __init__(self, OrderID, CustomerID, OrderDate, TotalAmount):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.OrderDate = OrderDate
        self.TotalAmount = TotalAmount

    def CalculateTotalAmount():
        pass

    def GetOrderDetails():
        pass

    def UpdateOrderStatus():
        pass

    def CancelOrder():
        pass

    class OrderDetails:
        def __init__(self, OrderDetailID, OrderID, ProductID, Quantity):
            self.OrderDetailID = OrderDetailID
            self.OrderID = OrderID
            self.ProductID = ProductID
            self.Quantity = Quantity

        def CalculateSubTotal():
            pass

        def GetOrderDetailInfo():
            pass

        def UpdateQuantity():
            pass

        def AddDiscount():
            pass


class Inventory:
    def __init__(self, InventoryID, ProductID, QuantityInStock, LastStockUpdate):
        self.InventoryID = InventoryID
        self.ProductID = ProductID
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    def GetProduct():
        pass

    def GetQuantityInStock():
        pass

    def AddToInventory():
        pass

    def RemoveFromInventory():
        pass

    def UpdateStockQuantity():
        pass

    def IsProductAvailable():
        pass

    def GetInventoryValue():
        pass

    def ListLowStockProducts():
        pass

    def ListOutOfStockProducts():
        pass

    def ListAllProducts():
        pass
