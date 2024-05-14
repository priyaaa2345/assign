class OrderService:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def CalculateTotalAmount(self, to_cal_total):
        self.cursor.execute(
            """
                    select sum(totalamount) from orders
                    where orderid= ?
                       """,
            (to_cal_total),
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def detail_check(self, getu):
        try:
            if getu in self.cursor.execute(
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
        self.cursor.execute(
            """
                        SELECT Orders.OrderID, Orders.OrderDate, Products.ProductName, Products.Description, OrderDetails.Quantity
                        FROM Orders
                        INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
                        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE Orders.OrderID = ?

                       """,
            (getu),
        )
        return self.cursor.fetchall()

    def UpdateOrderStatus(self, status, idu):
        self.cursor.execute(
            """
                        update orders
                        set status = '?'
                        where OrderID=?;
                       """(
                status, idu
            )
        )
        self.conn.commit()

    def CancelOrder(self):  # has some sql error
        try:
            self.cursor.execute(
                """
            delete from Orders where orderid=?
                                        """,
                (),
            )
            self.conn.commit()

        except Exception as e:
            print(e)
