import pytest
from utils.db_connection import get_connection

@pytest.fixture(scope="session")
def db_conn():
    conn = get_connection()
    yield conn
    conn.close()