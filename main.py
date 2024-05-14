import pyodbc
from entity.customer import Customer
from dao.CustomerService import CustomerService
from dao.ProductService import ProductService
from dao.OrderService import OrderService
from dao.OrderDetailService import OrderDetailService
from dao.InventoryService import InventoryService

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
# cursor = conn.cursor()

# cursor.execute("select 1")
print("database is connected")
print("Welcome to TECHSHOP 📲🎧⚡")


# TASK 1: CREATING CLASSES: ✅
# Task 2: Class Creation: ✅
# • Create the classes (Customers, Products, Orders, OrderDetails and Inventory) with the specified
# attributes.
# • Implement the constructor for each class to initialize its attributes.
# • Implement methods as specified


class MainMenu:
    def customer_menu(self):
        customer_service = CustomerService(conn)
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


if __name__ == "__main__":
    main_menu = MainMenu()
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
            main_menu.customer_menu()
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
