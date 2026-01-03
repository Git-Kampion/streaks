import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# 1️⃣ Connect to Access Database
# ------------------------------
db_path = r"C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb"

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)

conn = pyodbc.connect(conn_str)

# -----------------------------------
# 2️⃣ Load Table and Prepare Columns
# -----------------------------------
query = """
SELECT * FROM portLeag25
ORDER BY Tframe ASC
"""
df = pd.read_sql(query, conn)

# Identify last two columns (scores)
last_two_cols = df.columns[-2:]
score1, score2 = last_two_cols  # Home score, Away score

# Convert to numeric
for col in last_two_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Create HOZ and AOZ columns
df["HOZ"] = df[score1]
df["AOZ"] = df[score2]

# Create sum column
df["SumLastTwo"] = df["HOZ"] + df["AOZ"]

# Round column (2nd column in dataset)
round_col = df.columns[1]

# ---------------------------------
# 3️⃣ MGSec0Z Condition (Simplified)
# ---------------------------------
# Condition: Sum of last two columns between 1–3 inclusive
df['MGSec0Z'] = (
    (df['SumLastTwo'] > 0) &
    (df['SumLastTwo'] <= 3)
).astype(int)

# -----------------------------------
# 4️⃣ Standard Stats Calculations
# -----------------------------------
# ODD/EVEN
df_odd = df[df["SumLastTwo"] % 2 != 0]
df_even = df[df["SumLastTwo"] % 2 == 0]

odd_counts = df_odd.groupby(round_col).size().reset_index(name="Odd")
even_counts = df_even.groupby(round_col).size().reset_index(name="Even")

# DRAW
df_draw = df[df["HOZ"] == df["AOZ"]]
draw_counts = df_draw.groupby(round_col).size().reset_index(name="Draw")

# G0, G1, G2
g0_counts = df[df["SumLastTwo"] > 0].groupby(round_col).size().reset_index(name="G0")
g1_counts = df[df["SumLastTwo"] > 1].groupby(round_col).size().reset_index(name="G1")
g2_counts = df[df["SumLastTwo"] > 2].groupby(round_col).size().reset_index(name="G2")

# G0U3 = total goals between 1–2 inclusive
df['G0U3'] = ((df['SumLastTwo'] > 0) & (df['SumLastTwo'] < 3)).astype(int)

# Home Wins, Away Wins, BTTS
hwin_counts = df[df["HOZ"] > df["AOZ"]].groupby(round_col).size().reset_index(name="HWin")
awin_counts = df[df["AOZ"] > df["HOZ"]].groupby(round_col).size().reset_index(name="AWin")
btts_counts = df[(df["HOZ"] > 0) & (df["AOZ"] > 0)].groupby(round_col).size().reset_index(name="BTTS")

# Total matches per round
total_counts = df.groupby(round_col).size().reset_index(name="Total")

# Total goals per round
hoz_sum = df.groupby(round_col)["HOZ"].sum().reset_index(name="HOZ")
aoz_sum = df.groupby(round_col)["AOZ"].sum().reset_index(name="AOZ")

# G0U3 counts
g0u3_counts = df[df['G0U3'] == 1].groupby(round_col).size().reset_index(name='G0U3')

# MGSec0Z counts (Simplified)
mgsec0z_counts = df[df['MGSec0Z'] == 1].groupby(round_col).size().reset_index(name='MGSec0Z')

# -----------------------------------
# 5️⃣ Merge All Results into One Table
# -----------------------------------
result = (
    total_counts
    .merge(hoz_sum, on=round_col, how="outer")
    .merge(aoz_sum, on=round_col, how="outer")
    .merge(odd_counts, on=round_col, how="outer")
    .merge(even_counts, on=round_col, how="outer")
    .merge(draw_counts, on=round_col, how="outer")
    .merge(g0_counts, on=round_col, how="outer")
    .merge(g1_counts, on=round_col, how="outer")
    .merge(g0u3_counts, on=round_col, how="outer")
    .merge(mgsec0z_counts, on=round_col, how="outer")  # ⬅️ MGSec0Z simplified here
    .merge(g2_counts, on=round_col, how="outer")
    .merge(hwin_counts, on=round_col, how="outer")
    .merge(awin_counts, on=round_col, how="outer")
    .merge(btts_counts, on=round_col, how="outer")
    .fillna(0)
    .astype(int)
    .sort_values(by=round_col)
)

print(result)

# Export to Excel
result.to_excel("Round_Count_Extended.xlsx", index=False)
conn.close()

# -----------------------------------
# 6️⃣ Create HTML Report (Table View)
# -----------------------------------
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
        th {{ background-color: #007bff; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card shadow">
            <div class="card-header text-center bg-primary text-white">
                <h2>Round Statistics Report</h2>
            </div>
            <div class="card-body">
                <h6><strong>HOZ</strong>: Total Home Goals | <strong>AOZ</strong>: Total Away Goals</h6>
                {result.to_html(classes="table table-bordered table-hover table-sm", index=False)}
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("Round_Report.html", "w", encoding="utf-8") as f:
    f.write(html_report)

print("✅ Report saved as Round_Report.html and Round_Count_Extended.xlsx")

# -----------------------------------
# 7️⃣ Summary + Visualization
# -----------------------------------
summary_data = {
    'Metric': ['G0U3', 'Odd', 'Even', 'MGSec0Z'],
    'Total': [
        result['G0U3'].sum(),
        result['Odd'].sum(),
        result['Even'].sum(),
        result['MGSec0Z'].sum()
    ]
}
summary_df = pd.DataFrame(summary_data)

# Line Chart (Per Round)
plt.figure(figsize=(10,6))
sns.lineplot(data=result, x=round_col, y="G0U3", label="G0U3 (1-2 Goals)", marker="o", linewidth=2)
sns.lineplot(data=result, x=round_col, y="Odd", label="Odd", marker="o", linestyle="--")
sns.lineplot(data=result, x=round_col, y="Even", label="Even", marker="o", linestyle=":")
sns.lineplot(data=result, x=round_col, y="MGSec0Z", label="MGSec0Z", marker="o", linestyle="-.")
plt.title("Round Comparison: G0U3 vs Odd vs Even vs MGSec0Z")
plt.xlabel("Round")
plt.ylabel("Count per Round")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Round_Findings_Chart.png")
plt.close()

# -----------------------------------
# 8️⃣ Findings Report
# -----------------------------------
dominant_metric = summary_df.loc[summary_df['Total'].idxmax(), 'Metric']
insight_text = f"""
<h4>🔍 Findings Summary</h4>
<p>
Across all rounds, the most frequent condition was:
<b style='color:green;'>{dominant_metric}</b>.
This indicates that the <b>{dominant_metric}</b> pattern 
appears more consistently across matches compared to Odd, Even, and G0U3 outcomes.
</p>
"""

html_findings = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Round Findings Report</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f8f9fa; }}
        .card {{ margin: 20px auto; max-width: 95%; }}
        img {{ display: block; margin: 0 auto; max-width: 90%; }}
        table {{ text-align: center; }}
        th {{ background-color: #007bff; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card shadow">
            <div class="card-header text-center bg-success text-white">
                <h2>Round Findings: G0U3 vs Odd vs Even vs MGSec0Z</h2>
            </div>
            <div class="card-body">
                {insight_text}
                <h5>📊 Metric Totals</h5>
                {summary_df.to_html(classes="table table-bordered table-hover table-sm", index=False)}
                <br>
                <h5>📉 Trend Chart</h5>
                <img src="Round_Findings_Chart.png" alt="Round Comparison Chart">
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("Round_Findings_Report.html", "w", encoding="utf-8") as f:
    f.write(html_findings)

print("✅ Findings report saved as Round_Findings_Report.html")
