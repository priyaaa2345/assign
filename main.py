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
            new_one = product_service.UpdateProductInfo(
                updated_price, updated_description, the_id
            )
            for i in new_one:
                print(i)

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


def order_menu():
    order_service = OrderService()
    while True:
        print(
            """
                1. Total amount for order
                2. Display order details
                3. UPdate order status
                4. Cancel order
                5. Bacck to main menu

              """
        )
        choice = int(input("enter a choice: "))
        if choice == 1:
            to_cal_total = int(
                input("enter the customer id to calculate total amount: ")
            )
            totu = order_service.CalculateTotalAmount(to_cal_total)
            print("the total amount for the given orderid is: ", totu)
        elif choice == 2:
            get_details = int(input("enter cust id to get total details: "))
            getu = order_service.GetOrderDetails(get_details)
            print("the total order details is: ", getu)
        elif choice == 3:
            status = input(
                "enter the status that you want to update(Processing/Shipped): "
            )
            idu = int(input("enter the order id to do changes: "))
            order_service.UpdateOrderStatus(status, idu)
            print("updated successfully")

        elif choice == 4:
            pass
        elif choice == 5:
            break


def order_detail_menu():
    order_detail_service = OrderDetailService()
    while True:
        print(
            """
                1. Calculate subtotal
                2. Get order detail information
                3. update quantity
                4. Adding discount
                5. Back to main menu
              """
        )
        choice = int(input("enter a choice: "))
        if choice == 1:
            ordid = int(input("enter the order id to calculate its subtotal: "))
            subtotal = order_detail_service.CalculateSubtotal(ordid)
            print("the amount is: ", subtotal)
        elif choice == 2:
            orduid = int(input("enter the order id to get the complte info: "))
            detail = order_detail_service.GetOrderDetailInfo(orduid)
            print("the details are: ", detail)
        elif choice == 3:
            quan = int(input("enter the quantity to update: "))
            orddid = int(input("enter the ord detail id to update: "))
            order_detail_service.UpdateQuantity(quan, orddid)
            print("updated successfully!! ")
        elif choice == 4:
            ordeid = int(input("enter the orderdetailid to add discount: "))
            disc_amt = order_detail_service.AddDiscount(ordeid)
            print("the amt affter discount is : ", disc_amt)
        elif choice == 5:
            break


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
        return cursor.fetchall()

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
        # conn.commit()
        # return cursor.fetchall()


class OrderService:
    #     def __init__(self, OrderID, CustomerID, OrderDate, TotalAmount):
    #         self.OrderID = OrderID
    #         self.CustomerID = CustomerID
    #         self.OrderDate = OrderDate
    #         self.TotalAmount = TotalAmount

    def CalculateTotalAmount(self, to_cal_total):
        cursor.execute(
            """
                    select sum(totalamount) from orders
                    where orderid= ?
                       """,
            (to_cal_total),
        )
        return cursor.fetchall()

    def GetOrderDetails(self, getu):
        cursor.execute(
            """
                        SELECT Orders.OrderID, Orders.OrderDate, Products.ProductName, Products.Description, OrderDetails.Quantity
                        FROM Orders
                        INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE Orders.OrderID = ?

                       """,
            (getu),
        )
        return cursor.fetchall()

    def UpdateOrderStatus(self, status, idu):
        cursor.execute(
            """
                        update orders
                        set status = '?'
                        where OrderID=?;
                       """(
                status, idu
            ),
        )
        conn.commit()

    def CancelOrder():  # has some sql error
        pass


class OrderDetailService:
    # def __init__(self, OrderDetailID, OrderID, ProductID, Quantity):
    #     self.OrderDetailID = OrderDetailID
    #     self.OrderID = OrderID
    #     self.ProductID = ProductID
    #     self.Quantity = Quantity

    def CalculateSubtotal(self, ordid):
        cursor.execute(
            """
                        select quantity*price from OrderDetails
                        left join Products on
                        OrderDetails.ProductID=Products.ProductID
                        where orderid=?
                        """,
            (ordid),
        )
        return cursor.fetchall()

    def GetOrderDetailInfo(self, orduid):
        cursor.execute(
            """
                        select * from OrderDetails
                        right join orders on
                        OrderDetails.OrderID=Orders.OrderID
                        where orderdetails.orderid=?
                       """,
            (orduid),
        )
        return cursor.fetchall()

    def UpdateQuantity(self, quan, orddid):
        cursor.execute(
            """
                    update OrderDetails
                    set quantity = ?
                    where OrderDetailID=?
                       """,
            (quan, orddid),
        )
        conn.commit()

    def AddDiscount(self, ordeid):
        cursor.execute(
            """
                        select (totalamount-100) from OrderDetails
                        left join orders on
                        OrderDetails.orderid=orders.orderid
                        where OrderDetailid=?;
                       """,
            (ordeid),
        )
        return cursor.fetchall()


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
