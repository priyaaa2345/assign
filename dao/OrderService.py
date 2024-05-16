from exception.database_exception import DatabaseException
from exception.payment_exception import PaymentException
from util.DBConn import DBConnection


class OrderService(DBConnection):
    # def __init__(self, conn):
    #     self.conn = conn
    #     self.cursor = conn.cursor()

    def CalculateTotalAmount(self, to_cal_total):
        try:
            self.cursor.execute(
                """
                    select sum(totalamount) from orders
                    where orderid= ?
                       """,
                (to_cal_total),
            )
            result = self.cursor.fetchone()
            if result[0] is None:
                raise PaymentException()
            return result[0]
        except Exception as e:
            print(e)

        # return result[0] if result else 0

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
        try:
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
            result = self.cursor.fetchone()
            if result:
                return result[0]
            raise DatabaseException()
        except Exception as e:
            print(e)

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

    def CancelOrder(self, order_id, ord_id):
        try:
            self.cursor.execute(
                """
            delete from OrderDetails where orderid=?;
            delete from Orders where orderid=?
                                        """,
                (order_id, ord_id),
            )
            self.conn.commit()

        except Exception as e:
            print(e)


# task 6 : collections


def sort_orders_by_date(self) -> list:
    try:
        orders = self.cursor.execute("select orderdate from orders")
        output = [sorted(orders, key=lambda order: order.date)]
        return output
    except Exception as e:
        print(e)
