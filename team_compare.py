import pandas as pd

# ==================================
# CONFIG
# ==================================
DATA_FILE = "Full_First_Sec_Analysis_Handicaps_CorrectScores20260114.xlsx"

# Example user inputs (could later be CLI or UI inputs)
TEAM_A = "Inter"
TEAM_B = "BayernMunich"
METRICS = ["FirstHalfHomeOverZ", "FullBTS", "FullOver2","FullHWin","FulltimeHomeOver2"]  # can expand

# ==================================
# LOAD DATA
# ==================================
df = pd.read_excel(DATA_FILE)

# Ensure required cols exist
for col in ["home", "away"] + METRICS:
    if col not in df.columns:
        raise Exception(f"Missing column in dataset: {col}")

# ==================================
# FILTER HOME MATCHES for both teams
# ==================================
df_A = df[df["home"] == TEAM_A].copy()
df_B = df[df["home"] == TEAM_B].copy()

# ==================================
# BUILD COMPARISON TABLE
# ==================================
rows = []
for metric in METRICS:
    if df_A.shape[0] == 0 and df_B.shape[0] == 0:
        continue

    gp_A = df_A.shape[0]
    gp_B = df_B.shape[0]

    hits_A = df_A[metric].sum() if gp_A > 0 else 0
    hits_B = df_B[metric].sum() if gp_B > 0 else 0

    rate_A = round(hits_A / gp_A, 2) if gp_A > 0 else 0
    rate_B = round(hits_B / gp_B, 2) if gp_B > 0 else 0

    delta = round(rate_A - rate_B, 2)

    rows.append({
        "Metric": metric,
        f"{TEAM_A}_GP": gp_A,
        f"{TEAM_A}_Hits": hits_A,
        
        f"{TEAM_B}_GP": gp_B,
        f"{TEAM_B}_Hits": hits_B
        
    })

compare_df = pd.DataFrame(rows)

# ==================================
# CONVERT TO HTML
# ==================================
html_table = compare_df.to_html(index=False)

html_template = f"""
<html>
<head>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 20px;
}}
h1 {{
    padding: 10px;
    background: #e3e3e3;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}
table, th, td {{
    border: 1px solid #999;
}}
td, th {{
    text-align: center;
    padding: 6px;
}}
th {{
    background: #f2f2f2;
}}
</style>
</head>
<body>

<h1>Team Comparison (Home Matches)</h1>
<h2>{TEAM_A} vs {TEAM_B}</h2>

<p>Metrics compared: {", ".join(METRICS)}</p>

{html_table}

</body>
</html>
"""

output = "team_compare.html"
with open(output, "w", encoding="utf-8") as f:
    f.write(html_template)

print("Comparison report generated ->", output)
