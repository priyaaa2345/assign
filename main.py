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
            if customer_service.cust_data_check(FirstName):
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
            print(" ", stock)
        elif choice == 4:
            break


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
            to_cal_total = int(input("enter the order id to calculate total amount: "))
            totu = order_service.CalculateTotalAmount(to_cal_total)
            print("the total amount for the given orderid is: ", totu)
        elif choice == 2:
            get_details = int(input("enter order id to get total details: "))
            if order_service.detail_check:  # exception not throwing properly
                getu = order_service.GetOrderDetails(get_details)
                print("the  order details is: ", getu)
            else:
                print("give the correct details")
        elif choice == 3:  # error
            status = input(
                "enter the status that you want to update(Processing/Shipped): "
            )
            idu = int(input("enter the order id to do changes: "))
            order_service.UpdateOrderStatus(status, idu)
            print("updated successfully")

        elif choice == 4:  # no code
            pass
        elif choice == 5:
            break


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


class Inventory:
    def __init__(self, InventoryID, ProductID, QuantityInStock, LastStockUpdate):
        self.__InventoryID = InventoryID
        self.__ProductID = ProductID
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    def get_inventoryid(self):
        return self.__InventoryID

    def set_inventoryid(self, InventoryID):
        self.__InventoryID = InventoryID

    def get_ProductID(self):
        return self.__ProductID

    def set_ProductID(self, ProductID):
        self.__ProductID = ProductID


def inventory_menu():
    inventory_service = InventoryService()
    while True:
        print(
            """ 
              1. Get product in inventory
              2.Get quantity in stock
              3. Add quantity 
              4. Remove quantity
              5. Update Stock quantity
              6. Check for availability
              7. Get total value 
              8. Low stock product alert
              9. Out of stock product
              10. List all products
              11. Back to main menu
              
              """
        )
        choice = int(input("enter a choice: "))
        if choice == 1:
            inv_id = int(input("enter the inventory id to get the product: "))
            product = inventory_service.GetProduct(inv_id)
            print("The product for the given id is: ", product)
        elif choice == 2:
            prod_id = int(input("enter the product id to know the quantity in stock: "))
            pros = inventory_service.GetQuantityInStock(prod_id)
            print("the quantity in stock is : ", pros)
        elif choice == 3:
            quan = int(input("enter the quantity to add to a product: "))
            prid = int(input("enter the product id to add the quantity: "))
            inventory_service.AddToInventory(quan, prid)
            print("Added successfuly..!")
        elif choice == 4:
            quant = int(input("enter a quantity to remove from inventory: "))
            proid = int(input("enter the productid to remove quantity from: "))
            if inventory_service.quantity_in_inventory(quant, proid):
                inventory_service.RemoveFromInventory(quant, proid)
                print("Removed successfully..")
            else:
                print("insufficent Quantity in inventory ")
        elif choice == 5:
            new_val = int(input("enter a new value to update: "))
            pro_id = int(input("enter the product id: "))
            inventory_service.UpdateStockQuantity(new_val, pro_id)
            print("new value updated!!")
        elif choice == 6:
            proddid = int(input("enter the product id to check for availability: "))
            is_avail = inventory_service.IsProductAvailable(proddid)
            print(f"the product mentioned has {is_avail} quantity ")
        elif choice == 7:
            prod_id_invvalue = int(
                input(
                    "enter the product id to get the total value for the product in inventory: "
                )
            )
            total_inv_value = inventory_service.GetInventoryValue(prod_id_invvalue)
            print(
                f"Total value of {prod_id_invvalue} in inventory is {total_inv_value} "
            )
        elif choice == 8:
            low_stock = int(input("enter the quantity indicating low stock: "))
            threshold_val = inventory_service.ListLowStockProducts(low_stock)
            print("the products are: ", threshold_val)
        elif choice == 9:
            out_stock = inventory_service.ListOutOfStockProducts()
            print("the products that are out of stock are: ", out_stock)
        elif choice == 10:
            all_products = inventory_service.ListAllProducts()
            print("the inventory list are: ", all_products)
        elif choice == 11:
            break


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
        return cursor.fetchall()

    def cust_data_check(self, FirstName):
        try:
            cursor.execute(
                "select * from customers where FirstName like ? ", (FirstName)
            )
            rows = cursor.fetchall()
            if not rows:
                raise Exception("No customer found with the given name.")

            return True

        except Exception as e:
            print("Invalid DataException: Invalid credentials..")
            return False

    def UpdateCustomerInfo(self, updation, CustomerId):
        cursor.execute(
            "update Customers set Phone=? where CustomerId=?",
            (updation, CustomerId),
        )
        conn.commit()

        # for getters and setters:


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

    # error
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
        return cursor.fetchall()


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
        result = cursor.fetchone()
        return result[0] if result else 0

    def detail_check(self, getu):
        try:
            if getu in cursor.execute(
                """
                       select orderid from orders
                       where orderid=?
                       """,
                (getu),
            ):
                return True
        except Exception as e:
            print("InComplete Order Exception")
            print("Theres no such orderid")
            return False

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
            )
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
        result = cursor.fetchone()
        return result[0] if result else 0

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
        result = cursor.fetchone()
        return result[0] if result else 0


class InventoryService:

    def quantity_in_inventory(self, quant, proid):
        try:
            cursor.execute(
                """
                                select quantity_in_stock from inventory
                                where productID=?
                           """,
                (proid),
            )
            quantity_in_stock = cursor.fetchone()[0]
            return quant <= quantity_in_stock
        #     else:
        #         raise InSufficientStockException( # type: ignore
        #             "Insufficient Stock to proceed the order "
        #         )

        except Exception as e:
            print("The quantity u have mentioned is not available in the inventory")
            return False
        # result=cursor.fetchone()
        # return result[0] if result else 0

    def GetProduct(self, inv_id):
        cursor.execute(
            """
                    select productname from inventory
                    inner join Products on
                    Inventory.ProductID=Products.ProductID
                    where InventoryId=?;
                       """,
            (inv_id),
        )
        result = cursor.fetchone()
        return result[0] if result else 0

    def GetQuantityInStock(self, prod_id):
        cursor.execute(
            """
                        select quantityinstock from Inventory
                        where ProductID=?
                       """,
            (prod_id),
        )

        result = cursor.fetchone()
        return result[0] if result else 0

    def AddToInventory(self, quan, prid):
        cursor.execute(
            """
                        update Inventory
                        set quantityinstock = QuantityInStock+?
                        where ProductID=?;
                       """,
            (quan, prid),
        )
        conn.commit()

    def RemoveFromInventory(self, quant, proid):
        cursor.execute(
            """
                        update Inventory
                        set QuantityInStock=QuantityInStock-?
                        where ProductID=?
                       """,
            (quant, proid),
        )
        conn.commit()

    def UpdateStockQuantity(self, new_val, pro_id):
        cursor.execute(
            """
                        update Inventory
                        set QuantityInStock=?
                        where ProductID=?;
                       """,
            (new_val, pro_id),
        )
        conn.commit()

    def IsProductAvailable(self, proddid):
        cursor.execute(
            """
                        select quantityinstock from inventory
                        where QuantityInStock>0 and ProductID=?;
                       """,
            (proddid),
        )
        result = cursor.fetchone()
        return result[0] if result else 0

    def GetInventoryValue(self, prod_id_invvalue):
        cursor.execute(
            """
                        select price*quantityinstock from inventory
                        inner join products on
                        inventory.ProductID=Products.ProductID
                        where inventory.ProductID=?;
                       """,
            (prod_id_invvalue),
        )
        result = cursor.fetchone()
        return result[0] if result else 0

    def ListLowStockProducts(self, low_stock):
        cursor.execute(
            """
                            select * from inventory
                            where QuantityInStock<?;
                       """,
            (low_stock),
        )
        return cursor.fetchall()

    def ListOutOfStockProducts(self):
        cursor.execute(
            """                                         
                        select * from inventory
                        where QuantityInStock<0;
                       """
        )
        return cursor.fetchall()

    def ListAllProducts(self):
        cursor.execute(
            """
                       select productid,quantityinstock from Inventory;
                       """
        )
        return cursor.fetchall()


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
