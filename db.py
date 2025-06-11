import psycopg2
import pandas as pd
from typing import Any, List, Tuple

def get_db_connection():
    """Establish and return a PostgreSQL database connection."""
    return psycopg2.connect(
        host="localhost",
        database="sports_radar",
        user="postgres",
        password="ASkl1289@"  # ⚠️ Consider securing this via environment variable
    )

def run_query(conn, query: str) -> pd.DataFrame:
    """Execute a SQL query without parameters and return a DataFrame."""
    return pd.read_sql_query(query, conn)

def run_query_params(conn, query: str, params: Tuple[Any, ...]) -> pd.DataFrame:
    """Execute a parameterized SQL query and return a DataFrame."""
    return pd.read_sql_query(query, conn, params=params)
