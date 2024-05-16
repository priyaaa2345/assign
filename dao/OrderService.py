from exception.database_exception import DatabaseException
from exception.payment_exception import PaymentException
from util.DBConn import DBConnection
from tabulate import tabulate


class OrderService(DBConnection):
    def CalculateTotalAmount(self, to_cal_total):
        try:
            self.cursor.execute(
                """
                SELECT SUM(TotalAmount) FROM Orders
                WHERE OrderID = ?
                """,
                (to_cal_total,),
            )
            result = self.cursor.fetchone()
            if result[0] is None:
                raise PaymentException("No total amount found for the order.")
            return result[0]
        except Exception as e:
            print(f"Error calculating total amount: {e}")
            raise PaymentException("Error occurred while calculating total amount.")

    def detail_check(self, getu):
        try:
            self.cursor.execute(
                """
                SELECT OrderID FROM Orders
                WHERE OrderID = ?
                """,
                (getu,),
            )
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                raise DatabaseException("No such order ID found.")
        except DatabaseException as e:
            print(e)
            return False
        except Exception as e:
            print(f"Incomplete Order Exception: {e}")
            return False

    # data collection done here
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
                (getu,),
            )
            result = self.cursor.fetchall()
            if result:
                headers = [
                    "OrderID",
                    "OrderDate",
                    "ProductName",
                    "Description",
                    "Quantity",
                ]
                table = tabulate(result, headers=headers, tablefmt="pretty")
                print(table)
                return table
            else:
                raise DatabaseException("No details found for the order.")
        except Exception as e:
            print(f"Error fetching order details: {e}")
            raise DatabaseException("Error occurred while fetching order details.")

    def UpdateOrderStatus(self, status, idu):
        try:
            self.cursor.execute(
                """
                UPDATE Orders
                SET Status = ?
                WHERE OrderID = ?
                """,
                (status, idu),
            )
            self.conn.commit()
            print("Order status updated successfully.")
        except Exception as e:
            print(f"Error updating order status: {e}")
            raise DatabaseException("Error occurred while updating order status.")

    def CancelOrder(self, order_id):
        try:
            self.cursor.execute(
                "DELETE FROM OrderDetails WHERE OrderID = ?", (order_id,)
            )
            self.cursor.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
            self.conn.commit()
            print("Order cancelled successfully.")
        except Exception as e:
            print(f"Error cancelling order: {e}")
            raise DatabaseException("Error occurred while cancelling order.")

    def sort_orders_by_date(self) -> list:
        try:
            self.cursor.execute("SELECT OrderDate FROM Orders")
            orders = self.cursor.fetchall()
            sorted_orders = sorted(orders, key=lambda order: order[0])
            return sorted_orders
        except Exception as e:
            print(f"Error sorting orders by date: {e}")
            raise DatabaseException("Error occurred while sorting orders by date.")


if __name__ == "__main__":
    order_service = OrderService()
    order_service.CalculateTotalAmount(1)
    order_service.GetOrderDetails(1)
