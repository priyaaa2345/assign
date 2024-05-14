import pyodbc

server_name = "MSI\SQLEXPRESS"
database_name = "TechShop"


conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)


print(conn_str)


class DBConnection:
    def __init__(self):  # for cursor instance
        self.conn = pyodbc.connect(
            conn_str
        )  # if obj is created there will be new connection
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
