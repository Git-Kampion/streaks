import pyodbc
import pandas as pd

# Path to your Access database
db_path = r"C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb"

# Build connection string
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)

# Connect to Access
conn = pyodbc.connect(conn_str)

# ---- Replace with your actual table name ----
table_name = "Laliga25"

# Load table into pandas
df = pd.read_sql(f"SELECT * FROM [{table_name}] ORDER BY Tframe ASC", conn)

# Identify last two columns
last_two_cols = df.columns[-2:]

# Convert last two columns to numeric (strict)
for col in last_two_cols:
    df[col] = pd.to_numeric(df[col])   # will raise error if non-numeric

# Create sum column
df['SumLastTwo'] = df[last_two_cols[0]] + df[last_two_cols[1]]

# Round column is the 2nd column
round_col = df.columns[1]

# Filter where sum > 2
#df_filtered = df[df['SumLastTwo'] == 3]

# Filter where sum is an odd number
#df_filtered = df[df['SumLastTwo'] % 2 == 0]

df_odd = df[df['SumLastTwo'] % 2 != 0]
df_even = df[df['SumLastTwo'] % 2 == 0]

# Count per Round
odd_counts = df_odd.groupby(round_col).size().reset_index(name='OddCount')
even_counts = df_even.groupby(round_col).size().reset_index(name='EvenCount')

# Merge side by side
result = pd.merge(odd_counts, even_counts, on=round_col, how='outer').fillna(0).astype(int)


# Count occurrences per Round
#result = df_filtered.groupby(round_col).size().reset_index(name='Count')

print(result)

# Export to Excel
result.to_excel("Round_Count.xlsx", index=False)

# Close connection
conn.close()
