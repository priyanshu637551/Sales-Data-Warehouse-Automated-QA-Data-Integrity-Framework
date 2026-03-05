import psycopg2
import pandas as pd

DB_CONFIG = {
    "host": "localhost",
    "database": "sales_project_on19feb",
    "user": "postgres",
    "password": "",
    "port": "5432"
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df