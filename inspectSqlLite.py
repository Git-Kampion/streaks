import sqlite3
import pandas as pd

# Open connection
conn = sqlite3.connect("football(1).sqlite")

# List tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

# Loop through table names
for table_name in tables["name"]:
    print(f"\n--- Table: {table_name} ---")
    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5;", conn)  # limit rows for preview
    print(df)


conn.close()
