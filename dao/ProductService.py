from util.DBConn import DBConnection

# from entity.products import Product


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
                (search_with_id),
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
                            set Price=?
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
                (stock_search_with_id),
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)


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
                    raise ValueError("You cant remove a product with existing orders")
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    # def has_existing_orders(self, product_id):
    #     if product_id == OrderDetails.productID:
    #         return True
    #     else:
    #         return False
