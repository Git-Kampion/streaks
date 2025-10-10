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

# ---- Replace with your actual table names ----
query = """
SELECT * FROM portLeag25
UNION 
SELECT * FROM Turk225
UNION 
SELECT * FROM belgiumJpl25
UNION 
SELECT * FROM Austria225
UNION 
SELECT * FROM BelgiumChall25
ORDER BY Tframe ASC
"""
df = pd.read_sql(query, conn)

# Identify last two columns (scores)
last_two_cols = df.columns[-2:]
score1, score2 = last_two_cols

# Convert to numeric
for col in last_two_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Create sum column
df['SumLastTwo'] = df[score1] + df[score2]

# Round column is 2nd column
round_col = df.columns[1]

# ODD/EVEN
df_odd = df[df['SumLastTwo'] % 2 != 0]
df_even = df[df['SumLastTwo'] % 2 == 0]

odd_counts = df_odd.groupby(round_col).size().reset_index(name='Odd')
even_counts = df_even.groupby(round_col).size().reset_index(name='Even')

# DRAW (equal scores)
df_draw = df[df[score1] == df[score2]]
draw_counts = df_draw.groupby(round_col).size().reset_index(name='Draw')

# G0, G1, G2
g0_counts = df[df['SumLastTwo'] > 0].groupby(round_col).size().reset_index(name='G0')
g1_counts = df[df['SumLastTwo'] > 1].groupby(round_col).size().reset_index(name='G1')
g2_counts = df[df['SumLastTwo'] > 2].groupby(round_col).size().reset_index(name='G2')

# Merge all results
result = odd_counts \
    .merge(even_counts, on=round_col, how="outer") \
    .merge(draw_counts, on=round_col, how="outer") \
    .merge(g0_counts, on=round_col, how="outer") \
    .merge(g1_counts, on=round_col, how="outer") \
    .merge(g2_counts, on=round_col, how="outer") \
    .fillna(0).astype(int)

print(result)

# Export to Excel
result.to_excel("Round_Count_Extended.xlsx", index=False)

# Close connection
conn.close()

# ---- Create Web Report ----
html_report = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Round Stats Report</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f8f9fa; }}
        .card {{ margin: 20px auto; max-width: 95%; }}
        table {{ text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card shadow">
            <div class="card-header text-center bg-primary text-white">
                <h2>Round Statistics Report</h2>
            </div>
            <div class="card-body">
                {result.to_html(classes="table table-bordered table-hover table-sm", index=False)}
            </div>
        </div>
    </div>
</body>
</html>
"""

# Save web report
with open("Round_Report.html", "w", encoding="utf-8") as f:
    f.write(html_report)

print("✅ Report saved as Round_Report.html and Round_Count_Extended.xlsx")
