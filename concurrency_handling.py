from util.DBConn import DBConnection


class ConcurrencyHandler(DBConnection):
    def ReadOrders(self, order_id):
        old_data = self.cursor.execute(
            "select * from Orders where OrderId=?", (order_id)
        )

    def UpdateOrders(self):
        pass
