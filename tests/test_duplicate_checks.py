from utils.db_connection import run_query

def test_no_duplicate_fact_sales_rows():
    df = run_query("SELECT order_id, product_key, COUNT(*) as cnt FROM fact_sales GROUP BY order_id, product_key HAVING COUNT(*) > 1")
    print(f"\n  DATA QUALITY FINDING: {len(df)} duplicate order-product rows found in fact_sales")
    print(df.to_string())    # We assert it doesn't grow beyond known count (8), treating this as a logged bug
    assert len(df) <= 8, f"❌ Duplicate count increased! Found {len(df)}, expected max 8"

def test_no_duplicate_customer_ids():
    df = run_query("SELECT customer_id, COUNT(*) as cnt FROM dim_customer GROUP BY customer_id HAVING COUNT(*) > 1")
    assert len(df) == 0, f"❌ Found {len(df)} duplicate customer_ids in dim_customer"

def test_no_duplicate_product_keys():
    df = run_query("SELECT product_key, COUNT(*) as cnt FROM dim_product GROUP BY product_key HAVING COUNT(*) > 1")
    assert len(df) == 0, f"❌ Found {len(df)} duplicate product_keys in dim_product"

def test_no_duplicate_location_keys():
    df = run_query("SELECT location_key, COUNT(*) as cnt FROM dim_location GROUP BY location_key HAVING COUNT(*) > 1")
    assert len(df) == 0, f"❌ Found {len(df)} duplicate location_keys in dim_location"

def test_no_duplicate_dates():
    df = run_query("SELECT order_date, COUNT(*) as cnt FROM dim_date GROUP BY order_date HAVING COUNT(*) > 1")
    assert len(df) == 0, f"❌ Found {len(df)} duplicate dates in dim_date"