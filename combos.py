import pandas as pd

# ============================
# 1. LOAD EXCEL
# ============================
file_path = "Full_First_Sec_Analysis_Handicaps_CorrectScores20260121.xlsx"
df = pd.read_excel(file_path)

# Ensure required columns exist
required_cols = ["Round", "home", "away", "FirstHalfHomeOverZ", "FirstOver0", "FulltimeMultiGoals2-6","2ndHalfOverZ"]
for c in required_cols:
    if c not in df.columns:
        raise Exception(f"Missing column in Excel: {c}")

# ============================
# 2. BUILD COMBO #1 (Away + BTS)
# ============================
df["Eligible_Away"] = (df["FirstHalfAwayOverZ"] == 1).astype(int)
df["ComboHit_Away"] = (
    (df["FirstHalfAwayOverZ"] == 1) &
    (df["FullBTS"] == 1)
).astype(int)

home_summary_away = df.groupby("home").agg(
    GamesPlayed=("Eligible_Away", "sum"),
    ComboHits=("ComboHit_Away", "sum")
).reset_index().rename(columns={"home": "Home"})

away_summary_away = df.groupby("away").agg(
    GamesPlayed=("Eligible_Away", "sum"),
    ComboHits=("ComboHit_Away", "sum")
).reset_index().rename(columns={"away": "Away"})

home_summary_away["HitRate"] = (home_summary_away["ComboHits"] / home_summary_away["GamesPlayed"]).replace({float('inf'): 0}).round(2)
away_summary_away["HitRate"] = (away_summary_away["ComboHits"] / away_summary_away["GamesPlayed"]).replace({float('inf'): 0}).round(2)

home_summary_away = home_summary_away[home_summary_away["GamesPlayed"] > 0]
away_summary_away = away_summary_away[away_summary_away["GamesPlayed"] > 0]

# ============================
# 3. BUILD COMBO #2 (Home + BTS)
# ============================
df["Eligible_Home"] = (df["FirstHalfHomeOverZ"] == 1).astype(int)
df["ComboHit_Home"] = (
    (df["FirstHalfHomeOverZ"] == 1) &
    (df["FullBTS"] == 1)
).astype(int)

home_summary_home = df.groupby("home").agg(
    GamesPlayed=("Eligible_Home", "sum"),
    ComboHits=("ComboHit_Home", "sum")
).reset_index().rename(columns={"home": "Home"})

away_summary_home = df.groupby("away").agg(
    GamesPlayed=("Eligible_Home", "sum"),
    ComboHits=("ComboHit_Home", "sum")
).reset_index().rename(columns={"away": "Away"})

home_summary_home["HitRate"] = (home_summary_home["ComboHits"] / home_summary_home["GamesPlayed"]).replace({float('inf'): 0}).round(2)
away_summary_home["HitRate"] = (away_summary_home["ComboHits"] / away_summary_home["GamesPlayed"]).replace({float('inf'): 0}).round(2)

home_summary_home = home_summary_home[home_summary_home["GamesPlayed"] > 0]
away_summary_home = away_summary_home[away_summary_home["GamesPlayed"] > 0]

# ============================
# 4. HTML CONVERSION
# ============================
home_away_table_1 = home_summary_away.to_html(index=False)
away_away_table_1 = away_summary_away.to_html(index=False)

home_home_table_2 = home_summary_home.to_html(index=False)
away_home_table_2 = away_summary_home.to_html(index=False)

# ============================
# 5. HTML OUTPUT TEMPLATE
# ============================
html_template = """
<html>
<head>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 20px;
}}
h2 {{
    background: #f2f2f2;
    padding: 10px;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 25px;
}}
table, th, td {{
    border: 1px solid #999;
}}
th, td {{
    padding: 8px;
    text-align: center;
}}
th {{
    background: #e3e3e3;
}}
</style>
</head>
<body>

<h1>Consistency Combinations Summary Report</h1>

<h2>Combo 1: FirstHalfAwayOverZ + FullBTS</h2>
<h3>Summary by Home Team</h3>
{home_away_table_1}
<h3>Summary by Away Team</h3>
{away_away_table_1}

<hr>

<h2>Combo 2: FirstHalfHomeOverZ + FullBTS</h2>
<h3>Summary by Home Team</h3>
{home_home_table_2}
<h3>Summary by Away Team</h3>
{away_home_table_2}

</body>
</html>
"""

html_filled = html_template.format(
    home_away_table_1=home_away_table_1,
    away_away_table_1=away_away_table_1,
    home_home_table_2=home_home_table_2,
    away_home_table_2=away_home_table_2
)

output_file = "combo_report.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_filled)

print("HTML report generated:", output_file)
