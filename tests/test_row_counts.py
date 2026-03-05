from utils.db_connection import run_query

def test_fact_sales_has_data():
    df = run_query("SELECT COUNT(*) as cnt FROM fact_sales")
    assert df["cnt"][0] > 0, "❌ fact_sales is empty"

def test_dim_customer_has_data():
    df = run_query("SELECT COUNT(*) as cnt FROM dim_customer")
    assert df["cnt"][0] > 0, "❌ dim_customer is empty"

def test_dim_product_has_data():
    df = run_query("SELECT COUNT(*) as cnt FROM dim_product")
    assert df["cnt"][0] > 0, "❌ dim_product is empty"

def test_dim_location_has_data():
    df = run_query("SELECT COUNT(*) as cnt FROM dim_location")
    assert df["cnt"][0] > 0, "❌ dim_location is empty"

def test_dim_date_has_data():
    df = run_query("SELECT COUNT(*) as cnt FROM dim_date")
    assert df["cnt"][0] > 0, "❌ dim_date is empty"

def test_fact_sales_matches_original_row_count():
    fact = run_query("SELECT COUNT(*) as cnt FROM fact_sales")
    original = run_query("SELECT COUNT(*) as cnt FROM original_table")
    assert fact["cnt"][0] == original["cnt"][0], \
        f"❌ Row mismatch: fact_sales={fact['cnt'][0]}, original={original['cnt'][0]}"