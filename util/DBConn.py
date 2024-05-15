import pyodbc
from util.DBPropertyUtil import PropertyUtil


class DBConnection:
    def __init__(self):  # for cursor instance
        conn_str = PropertyUtil.get_property_String()
        self.conn = pyodbc.connect(
            conn_str
        )  # if obj is created there will be new connection
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
