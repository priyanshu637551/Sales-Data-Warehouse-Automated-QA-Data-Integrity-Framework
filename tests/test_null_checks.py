from utils.db_connection import run_query

def test_fact_sales_no_nulls():
    df = run_query("SELECT * FROM fact_sales WHERE order_id IS NULL OR sales IS NULL OR profit IS NULL OR customer_key IS NULL OR product_key IS NULL OR location_key IS NULL")
    assert len(df) == 0, f"❌ Found {len(df)} NULL rows in fact_sales"

def test_dim_customer_no_nulls():
    df = run_query("SELECT * FROM dim_customer WHERE customer_id IS NULL OR customer_name IS NULL")
    assert len(df) == 0, f"❌ Found {len(df)} NULL rows in dim_customer"

def test_dim_product_no_nulls():
    df = run_query("SELECT * FROM dim_product WHERE product_key IS NULL OR product_name IS NULL OR category IS NULL")
    assert len(df) == 0, f"❌ Found {len(df)} NULL rows in dim_product"

def test_dim_location_no_nulls():
    df = run_query("SELECT * FROM dim_location WHERE location_key IS NULL OR city IS NULL OR state IS NULL OR region IS NULL")
    assert len(df) == 0, f"❌ Found {len(df)} NULL rows in dim_location"

def test_dim_date_no_nulls():
    df = run_query("SELECT * FROM dim_date WHERE order_date IS NULL OR year IS NULL OR month IS NULL OR day IS NULL")
    assert len(df) == 0, f"❌ Found {len(df)} NULL rows in dim_date"