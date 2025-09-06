import sqlite3
import pandas as pd

# Open connection
conn = sqlite3.connect("football.sqlite")

# List tables
#tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
#print(tables)

# View first rows of a table
df = pd.read_sql_query("SELECT * FROM MyanmarNatLeag25 LIMIT 10;", conn)
print(df)

conn.close()
