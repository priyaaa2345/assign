from exception.payment_exception import PaymentException
from util.DBConn import DBConnection


class PaymentService(DBConnection):
    def DisplayStatus(self, order_id):
        try:
            self.cursor.execute(
                "select status from Payments where order_id = ?", (order_id)
            )
            result = self.cursor.fetchone()
            if result:
                return result[0]
            raise PaymentException()
        except Exception as e:
            print(e)
