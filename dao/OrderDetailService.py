from exception.incomplete_order_exception import IncompleteOrderException
from util.DBConn import DBConnection


class OrderDetailService(DBConnection):
    # def __init__(self, conn):
    #     self.conn = conn
    #     self.cursor = conn.cursor()

    def CalculateSubtotal(self, ordid):
        try:
            self.cursor.execute(
                """
                        select quantity*price from OrderDetails
                        left join Products on
                        OrderDetails.ProductID=Products.ProductID
                        where orderid=?
                            """,
                (ordid),
            )
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(e)

    def GetOrderDetailInfo(self, orduid):
        try:
            self.cursor.execute(
                """
                        select * from OrderDetails
                        right join orders on
                        OrderDetails.OrderID=Orders.OrderID
                        where orderdetails.orderid=?
                       """,
                (orduid),
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def UpdateQuantity(self, quan, orddid):
        try:
            self.cursor.execute(
                """
                    update OrderDetails
                    set quantity = ?
                    where ProductID=?
                        """,
                (quan, orddid),
            )
            result = self.cursor.fetchone()
            if not result:
                raise IncompleteOrderException()

            self.conn.commit()
        except Exception as e:
            print(e)

    def AddDiscount(self, ordeid):
        try:
            self.cursor.execute(
                """
                        select (totalamount-100) from OrderDetails
                        left join orders ons
                        OrderDetails.orderid=orders.orderid
                            where OrderDetailid=?;
                        """,
                (ordeid),
            )
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(e)

    def DeleteById(self, orderdetailid):
        try:
            self.cursor.execute(
                "delete from OrderDetails where OrderDetailId= ? ", (orderdetailid)
            )
        except Exception as e:
            print(e)

    def GetDetail(self):
        try:
            self.cursor.execute("select * from OrderDetails")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
