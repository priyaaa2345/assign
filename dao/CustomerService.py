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
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def cust_data_check(self, FirstName):
        try:
            self.cursor.execute(
                "select * from customers where FirstName like ? ", (FirstName)
            )
            rows = self.cursor.fetchall()
            if not rows:
                raise Exception("No customer found with the given name.")

            return True

        except Exception as e:
            print("Invalid DataException: Invalid credentials..")
            return False

    def UpdateCustomerInfo(self, updation, CustomerId):
        try:
            self.cursor.execute(
                "update Customers set Phone=? where CustomerId=?",
                (updation, CustomerId),
            )
            self.conn.commit()

        except Exception as e:
            print(e)

        # for getters and setters:
