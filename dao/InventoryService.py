from exception.insufficent_stock_exception import InsufficientStockException
from util.DBConn import DBConnection


class InventoryService(DBConnection):

    def quantity_in_inventory(self, quant, proid):
        try:
            self.cursor.execute(
                """
                                select quantity_in_stock from inventory
                                where productID=?
                           """,
                (proid),
            )
            quantity_in_stock = self.cursor.fetchone()[0]
            return quant <= quantity_in_stock

        except Exception as e:
            print("The quantity u have mentioned is not available in the inventory")
            return False
        # result=cursor.fetchone()
        # return result[0] if result else 0

    def GetProduct(self, inv_id):
        try:
            self.cursor.execute(
                """
                    select productname from inventory
                    inner join Products on
                    Inventory.ProductID=Products.ProductID
                    where InventoryId=?;
                       """,
                (inv_id),
            )
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(e)

    def GetQuantityInStock(self, prod_id):
        try:
            self.cursor.execute(
                """
                        select quantityinstock from Inventory
                        where ProductID=?
                        """,
                (prod_id),
            )

            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(e)

    def AddToInventory(self, quan, prid):
        try:
            self.cursor.execute(
                """
                        update Inventory
                        set quantityinstock = QuantityInStock+?
                        where ProductID=?;
                        """,
                (quan, prid),
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def RemoveFromInventory(self, quant, proid):
        try:
            self.cursor.execute(
                """
                        update Inventory
                        set QuantityInStock=QuantityInStock-?
                        where ProductID=?
                        """,
                (quant, proid),
            )
            if quant < 0:
                raise InsufficientStockException()
        except Exception as e:
            print(e)

        finally:
            self.conn.commit()

    def UpdateStockQuantity(self, new_val, pro_id):
        try:
            self.cursor.execute(
                """
                        update Inventory
                        set QuantityInStock=?
                        where ProductID=?;
                       """,
                (new_val, pro_id),
            )
            self.cursor.execute(
                "select QuantityInStock from Inventory where productID=?", (pro_id)
            )
            row = self.cursor.fetchone()
            if row:
                curr_val = row[0]
            if new_val > curr_val:
                raise InsufficientStockException()
        except Exception as e:
            print(e)

        self.conn.commit()

    def IsProductAvailable(self, proddid):
        self.cursor.execute(
            """
                        select quantityinstock from inventory
                        where QuantityInStock>0 and ProductID=?;
                       """,
            (proddid),
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def GetInventoryValue(self, prod_id_invvalue):
        self.cursor.execute(
            """
                        select price*quantityinstock from inventory
                        inner join products on
                        inventory.ProductID=Products.ProductID
                        where inventory.ProductID=?;
                       """,
            (prod_id_invvalue),
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def ListLowStockProducts(self, low_stock):
        self.cursor.execute(
            """
                            select * from inventory
                            where QuantityInStock<?;
                       """,
            (low_stock),
        )
        return self.cursor.fetchall()

    def ListOutOfStockProducts(self):
        self.cursor.execute(
            """                                         
                        select * from inventory
                        where QuantityInStock<0;
                       """
        )
        return self.cursor.fetchall()

    def ListAllProducts(self):
        self.cursor.execute(
            """
                       select * from Inventory;
                       """
        )
        return self.cursor.fetchall()

    # task collection:

    def sort_inventory(self) -> list:
        try:
            inventory = self.cursor.execute("select InventoryID from Inventory")
            output = [sorted(inventory, key=lambda i: i.InventoryID)]
            return output

        except Exception as e:
            print(e)
