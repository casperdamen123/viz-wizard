import pyodbc
import os
from src.utils.get_secrets import get_secret
from src.logger.queries.events import schema_query, events_query

class EventLogging:

    def __init__(self):
        self.server = f"tcp:{os.getenv('DB_SERVER_NAME') + os.getenv('DB_SERVER_HOSTNAME')}"
        self.database = os.getenv('DB_NAME')
        self.table = 'events'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.username = os.getenv('DB_LOGIN')
        self.key_vault = os.getenv('KV_URI')
        self.password = get_secret(self.key_vault, 'sqlServerPassword')
    
    def log_generated_charts(self, chart_type: str) -> None:
        """Log the generated charts to database
        Args:
            chart_type (str): Name of the chart (i.e. line chart, scatter chart etc)
        Returns:
            None: But the database connection is closed
        """
        conn, cursor = self._connect_to_database()
        self._create_events_table(conn, cursor)
        data = ("chart generation", chart_type)
        cursor.execute(events_query, data)
        conn.commit()
        return conn.close()

    def _create_events_table(self, conn, cursor) -> None:
        """Create events table in logging database if non existent
        Returns:
            None: But commits query to database
        """
        if not self._check_if_table_exists(cursor, 'events'):
            cursor.execute(schema_query)
            return conn.commit()

    
    def _check_if_table_exists(self, cursor, table_name: str) -> bool:
        """Check if table exists in logging database
        Args:
            table_name (str): Name of table
        Returns:
            bool: True or false based on existence of table
        """
        try:
            cursor.execute(f"SELECT COUNT(*) FROM events")
            return True
        except pyodbc.ProgrammingError:
            return False

    def _connect_to_database(self):
        """Setup connection to SQL logging database
        Returns:
            conn: Pyodbc connection to SQL database
            cursor: Pyodbc connection cursor to communicate with databse
        """
        conn = pyodbc.connect(f"DRIVER={self.driver};SERVER={self.server};PORT=1433;DATABASE={self.database};UID={self.username};PWD={self.password};Connection Timeout=30")
        cursor = conn.cursor()
        return conn, cursor
        