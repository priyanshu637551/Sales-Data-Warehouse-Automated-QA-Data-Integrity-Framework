from utils.db_connection import run_query

def test_fact_sales_expected_columns():
    df = run_query("SELECT * FROM fact_sales LIMIT 1")
    expected = {"row_id", "order_id", "order_date", "ship_date", "sales", "quantity", "discount", "profit", "customer_key", "product_key", "location_key"}
    missing = expected - set(df.columns)
    assert not missing, f"❌ Missing columns in fact_sales: {missing}"

def test_dim_customer_expected_columns():
    df = run_query("SELECT * FROM dim_customer LIMIT 1")
    expected = {"customer_id", "customer_name", "segment"}
    missing = expected - set(df.columns)
    assert not missing, f"❌ Missing columns in dim_customer: {missing}"

def test_dim_product_expected_columns():
    df = run_query("SELECT * FROM dim_product LIMIT 1")
    expected = {"product_key", "product_id", "category", "sub_category", "product_name"}
    missing = expected - set(df.columns)
    assert not missing, f"❌ Missing columns in dim_product: {missing}"

def test_dim_location_expected_columns():
    df = run_query("SELECT * FROM dim_location LIMIT 1")
    expected = {"location_key", "postal_code", "country", "city", "state", "region"}
    missing = expected - set(df.columns)
    assert not missing, f"❌ Missing columns in dim_location: {missing}"

def test_dim_date_expected_columns():
    df = run_query("SELECT * FROM dim_date LIMIT 1")
    expected = {"order_date", "year", "month", "day"}
    missing = expected - set(df.columns)
    assert not missing, f"❌ Missing columns in dim_date: {missing}"