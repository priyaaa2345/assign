from util.DBConn import DBConnection
from tabulate import tabulate  # for tabulation in collections


class ProductService(DBConnection):
    # def __init__(self, conn):
    #     self.conn = conn
    #     self.cursor = conn.cursor()

    def GetProductDetails(self, search_with_id):
        try:
            self.cursor.execute(
                """
                        select * from Products
                        where ProductID=?
                       """,
                (search_with_id,),
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    # error
    def UpdateProductInfo(self, updated_price, updated_description, the_id):
        try:
            self.cursor.execute(
                """                                   
                            update Products
                            set Price=?,
                            description=?
                            where ProductID=?
                            """,
                (updated_price, updated_description, the_id),
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def IsProductInStock(self, stock_search_with_id):
        try:
            self.cursor.execute(
                """                                        
                        select * from products
                        left join Inventory on
                        Products.ProductID=Inventory.ProductID
                        where QuantityInStock>0 and Inventory.ProductID=?
                       """,
                (stock_search_with_id,),
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    # task 6 collections::::
    def ViewAll(self):
        try:
            self.cursor.execute("select * from Products")
            rows = self.cursor.fetchall()
            if rows:
                headers = [desc[0] for desc in self.cursor.description]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No products found.")
        except Exception as e:
            print(e)

    def CreateNewProduct(self, product_id, product_name, desc, price, category):
        self.cursor.execute(
            "insert into Products values(?,?,?,?,?)",
            (product_id, product_name, desc, price, category),
        )
        self.conn.commit()

    def DeleteById(self, prod_id):
        self.cursor.execute("delete from Inventory where ProductID=?", (prod_id,))
        self.cursor.execute("delete from OrderDetails where ProductID=?", (prod_id,))
        self.cursor.execute("delete from Products where ProductID=?", (prod_id,))
        self.conn.commit()


class ProductsList:
    def __init__(self):
        self.products = []

    def add(self, product):
        if product in self.products:
            raise ValueError("Product already exists")
        self.products.append(product)

    def update(self, product_id, product_name, description, price, category):
        for product in self.products:
            if product.product_id == product_id:
                product.name = product_name
                product.description = description
                product.price = price
                product.category = category
                return
        raise ValueError("Product not found")

    def remove(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                if self.has_existing_orders(product_id):
                    raise ValueError("You can't remove a product with existing orders")
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    # def has_existing_orders(self, product_id):
    #     if product_id == OrderDetails.productID:
    #         return True
    #     else:
    #         return False

    #  TASK ^ :COLLECTIONS
    def manage_product(self) -> list:
        pass
