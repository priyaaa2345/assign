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

            total = customer_service.CalculateTotalOrders(CustomerId)
            # customer = Customer(CustomerId, None, None, None, None, None)
            # total_orders = customer.CalculateTotalOrders()
            print("the total order for the given customer is : ", total)
        elif choice == 3:
            FirstName = input("enter the name of the customer to display: ")
            # cust = Customer(None, FirstName, None, None, None, None)
            # cust = Customer(FirstName)
            details = customer_service.GetCustomerDetails(FirstName)
            for detail in details:
                print(detail)

        elif choice == 4:
            updation = int(input("enter the data u want to update: "))
            CustomerId = int(input("enter their customer id: "))
            customer_service.UpdateCustomerInfo(updation, CustomerId)
            # updation = Customer(custt, None, None, None, None, phone)
            # updat = updation.UpdateCustomerInfo()

            print("updated successfully")

        elif choice == 5:
            break


def product_menu():
    product_service = ProductService()
    while True:
        print(
            """
                1. Product details
                2. Update product details
                3. Check stock details
                4. Back to main menu
              """
        )
        choice = int(input("enter a choice"))
        if choice == 1:
            search_with_id = int(input("enter the product id to search: "))
            descriptions = product_service.GetProductDetails(search_with_id)
            for description in descriptions:
                print(description)
        elif choice == 2:
            updated_price = int(input("enter the price to update: "))
            updated_description = input("enter the description to update: ")
            the_id = int(input("enter the product id that needs to be updated"))
            product_service.UpdateProductInfo(
                updated_price, updated_description, the_id
            )

            print("everything is updated successfully")
        elif choice == 3:
            stock_search_with_id = int(
                input("enter the product id to check if it is stock: ")
            )
            stock = product_service.IsProductInStock(stock_search_with_id)
            for i in stock:
                print(i)
        elif choice == 4:
            break


def order_detail_menu():
    pass


def order_menu():
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
        result = cursor.fetchone()
        return result[0] if result else 0
        # conn.commit()

    def GetCustomerDetails(self, FirstName):
        cursor.execute("select * from customers where FirstName like ? ", (FirstName))
        # conn.commit()
        return cursor.fetchall()

    def UpdateCustomerInfo(self, updation, CustomerId):
        cursor.execute(
            "update Customers set Phone=? where CustomerId=?",
            (updation, CustomerId),
        )
        conn.commit()


class ProductService:
    # def __init__(self, ProductID, ProductName, Description, Price):
    #     self.ProductID = ProductID
    #     self.ProductName = ProductName
    #     self.Description = Description
    #     self.Price = Price

    def GetProductDetails(self, search_with_id):
        cursor.execute(
            """
                        select * from Products
                        where ProductID=?
                       """,
            (search_with_id),
        )
        return cursor.fetchall()

    def UpdateProductInfo(self, updated_price, updated_description, the_id):
        cursor.execute(
            """                                   
                            update Products
                            set Price=?
                            description=?
                            where ProductID=?
                            """,
            (updated_price, updated_description, the_id),
        )
        conn.commit()

    def IsProductInStock(self, stock_search_with_id):
        cursor.execute(
            """                                        
                        select * from products
                        left join Inventory on
                        Products.ProductID=Inventory.ProductID
                        where QuantityInStock>0 and Inventory.ProductID=?
                       """,
            (stock_search_with_id),
        )
        conn.commit()


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
