from exception.authentication_exception import AuthenticationException
from exception.invalid_data_exception import InvalidDataException
from util.DBConn import DBConnection


class CustomerService(DBConnection):
    # def __init__(self, conn):
    #     self.conn = conn
    #     self.cursor = conn.cursor()

    def read_customers(self):
        try:
            self.cursor.execute("select * from Customers")
            for row in self.cursor:
                print(row)
        except Exception as e:
            print(e)

    def CalculateTotalOrders(self, total):
        try:
            self.cursor.execute(
                """
                    select count(Customers.CustomerId)  from Customers
                    inner join orders on
                    Customers.CustomerId=Orders.CustomerId
                    where Customers.CustomerId=?
                    group by Customers.CustomerId
                        """,
                (total),
            )
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print(e)

        # conn.commit()

    def GetCustomerDetails(self, FirstName):
        try:
            self.cursor.execute(
                "select * from customers where FirstName like ? ", (FirstName)
            )
            result = self.cursor.fetchall()
            if not result:
                raise InvalidDataException()
        except InvalidDataException as e:
            print(e)
        return result

    def UpdateCustomerInfo(self, updation, CustomerId):
        try:
            self.cursor.execute(
                "update Customers set Phone=? where CustomerId=?",
                (updation, CustomerId),
            )
            self.conn.commit()

        except Exception as e:
            print(e)

    # inventory id access
    def invent_access(self, inv_id):
        try:
            result = self.cursor.execute(
                """
                            select orderid from Customers
                            right join orders on
                            Customers.orderID=orders.orderID
                            where OrderID=?""",
                (inv_id),
            )
            if not result:
                raise AuthenticationException()
        except Exception as e:
            print(e)

    def Create_new_Customer(
        self, new_cust_id, first_name, last_name, mail, phone, addr
    ):
        try:
            self.cursor.execute(
                """
insert into Customers values(?,?,?,?,?,?)
                            """,
                (new_cust_id, first_name, last_name, mail, phone, addr),
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def Delete_by_id(self, cust_id):
        try:
            self.cursor.execute(""" delete from orders where CustomerID=?""", (cust_id))
            self.cursor.execute(
                """ delete from Customers where CustomerID=?""", (cust_id)
            )
            self.conn.commit()
        except Exception as e:
            print(e)
