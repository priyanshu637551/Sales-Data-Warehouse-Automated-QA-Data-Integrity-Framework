# 🧪 Data Pipeline Quality Assurance Framework

A Python-based automated QA framework to validate the integrity of a PostgreSQL Sales Data Warehouse built on the Superstore dataset.

## 📌 Project Overview

This framework performs automated data quality testing on a star schema data warehouse consisting of 1 fact table and 4 dimension tables. It detects real-world data issues including NULL values, schema mismatches, duplicate records, and row count anomalies.

## 🗂️ Project Structure
```
qa_data_pipeline/
├── tests/
│   ├── test_null_checks.py       # NULL validation across all tables
│   ├── test_schema_checks.py     # Column existence & schema validation
│   ├── test_duplicate_checks.py  # Duplicate key detection
│   └── test_row_counts.py        # Row count & ETL completeness checks
├── utils/
│   └── db_connection.py          # PostgreSQL connection utility
├── reports/
│   └── test_report.html          # Auto-generated HTML test report
├── conftest.py
└── pytest.ini
```

## 🛠️ Tech Stack

- **Python** — Core testing logic
- **Pytest** — Test framework & HTML report generation
- **PostgreSQL** — Data warehouse (star schema)
- **Pandas** — Query result validation
- **psycopg2** — PostgreSQL database connector

## ✅ Test Coverage (21 Test Cases)

| Test Module | What It Validates |
|---|---|
| `test_null_checks.py` | No NULL values in critical columns across all 5 tables |
| `test_schema_checks.py` | All expected columns exist in each table |
| `test_duplicate_checks.py` | No duplicate primary/surrogate keys |
| `test_row_counts.py` | Tables have data + fact table matches original source |

## 🐛 Real Data Quality Finding

During testing, the framework detected **8 duplicate order-product combinations** in `fact_sales`, indicating an ETL loading issue where certain order lines were loaded twice. This was logged as a known bug with a threshold assertion.

## 🚀 How to Run

```bash
# Install dependencies
pip install pytest psycopg2-binary pytest-html pandas

# Run all tests with HTML report
pytest -v
```

HTML report is auto-generated at `reports/test_report.html`

## 📊 Test Results
```
21 passed in 1.53s

<img width="1919" height="911" alt="Screenshot 2026-03-05 145754" src="https://github.com/user-attachments/assets/e47b7cf7-e78a-4eb2-a600-45c722cfce38" />

```
