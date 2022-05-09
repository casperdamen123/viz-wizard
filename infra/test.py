import pyodbc
from typing import Tuple

def _connect_to_database(self) -> pyodbc.connect:
    """Setup connection to SQL logging database
    Returns:
        pyodbc.connect: Connection to SQL database
        pyodbc.connect.cursor: Cursor to communicate with databse
    """
    conn = pyodbc.connect(f"DRIVER={self.driver};SERVER={self.server};PORT=1433;DATABASE={self.database};UID={self.username};PWD={self.password};Connection Timeout=30")
    cursor = conn.cursor()
    print(type(conn))

_connect_to_database()