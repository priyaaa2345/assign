from util.DBConn import DBConnection


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
