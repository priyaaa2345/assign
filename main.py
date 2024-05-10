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
class Customer:
    def __init__(self, CustomerId, FirstName, LastName, Email, Phone, Address):
        self.CustomerId = CustomerId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Phone = Phone
        self.Address = Address


def customer_menu():
    customer_service = CustomerService()
    while True:
        print(
            """
                             
                             1. Read customer details
                             2.Calculate Total orders
                             3. View specific customer 
                             4. Update details
                             5.Back to main menu
                             """
        )
        choice = int(input("enter a choice: "))
        if choice == 1:
            customer_service.read_customers()
        elif choice == 2:
            CustomerId = int(input("enter the customerid to get total orders: "))
            customer_service.CalculateTotalOrders(CustomerId)
            # customer = Customer(CustomerId, None, None, None, None, None)
            # total_orders = customer.CalculateTotalOrders()
            print("the total order for the given customer is : ")
        elif choice == 3:
            FirstName = input("enter the name of the customer to display: ")
            # cust = Customer(None, FirstName, None, None, None, None)
            # cust = Customer(FirstName)
            customer_service.GetCustomerDetails(FirstName)
            # print(details)
        elif choice == 4:
            phone = int(input("enter the data u want to update: "))
            CustomerId = int(input("enter their customer id: "))
            updation = Customer(phone)
            customer_service.UpdateCustomerInfo(updation, CustomerId)
            # updation = Customer(custt, None, None, None, None, phone)
            # updat = updation.UpdateCustomerInfo()
            print("updated successfully")
        elif choice == 5:
            break


def order_menu():
    pass


def order_detail_menu():
    pass


def product_menu():
    pass


def inventory_menu():
    pass


class CustomerService:
    def read_customers(self):
        cursor.execute("select * from Customers")
        for row in cursor:
            print(row)

    def CalculateTotalOrders(self, total):
        cursor.execute(
            """
                    select count(Customers.CustomerId)  from Customers
                    inner join orders on
                    Customers.CustomerId=Orders.CustomerId
                    where Customers.CustomerId=?
                    group by Customers.CustomerId
                    """,
            (total),
        )
        # conn.commit()
        return 0

    def GetCustomerDetails(self, FirstName):
        cursor.execute("select * from customers where FirstName like ? ", (FirstName))
        conn.commit()

    def UpdateCustomerInfo(self, updation, CustomerId):
        cursor.execute(
            "update Customers set Phone=? where CustomerId=?",
            (updation.Phone, CustomerId),
        )


# customers_instance = Customer(
#     Customer.CustomerId,
#     Customer.FirstName,
#     Customer.LastName,
#     Customer.Email,
#     Customer.Phone,
#     Customer.Address,
# )
# customers_instance.read_customers()


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


if __name__ == "__main__":
    while True:
        print(
            """
                           
                              1.Customer data
                              2.Product data
                              3.Orders data
                              4. Order details 
                              5.Inventory data
                              6.Exit
                              """
        )
        choice = int(input("enter your choice "))
        if choice == 1:
            customer_menu()
        elif choice == 2:
            product_menu()
        elif choice == 3:
            order_menu()
        elif choice == 4:
            order_detail_menu()
        elif choice == 5:
            inventory_menu()
        elif choice == 6:
            break
