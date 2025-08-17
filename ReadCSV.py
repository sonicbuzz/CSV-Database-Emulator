import pandas as pd
import sqlite3

class QueryEngine:
    def __init__(self):
        self.df = None
        self.conn = None

    def load_file(self, file_path):
        """Load CSV/Excel into pandas + SQLite"""
        if file_path.endswith(".csv"):
            self.df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            self.df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type")

        # load into sqlite
        self.conn = sqlite3.connect(":memory:")
        self.df.to_sql("data", self.conn, index=False, if_exists="replace")

        return self.df  # return dataframe for display

    def run_query(self, query, sql_mode=True):
        """Run either SQL query or pandas query"""
        if self.df is None:
            raise ValueError("No file loaded")

        if sql_mode:  # SQL query
            return pd.read_sql_query(query, self.conn)
        else:  # Pandas query
            return self.df.query(query)
