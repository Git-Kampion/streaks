import pyodbc
import pandas as pd

# ======================================================
# 🧩 1️⃣ CONNECT TO ACCESS DATABASE
# ======================================================
db_path = r"C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb"
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)
conn = pyodbc.connect(conn_str)

# ======================================================
# 🧮 2️⃣ LOAD DATA AND SET COLUMN REFERENCES
# ======================================================
query = "SELECT * FROM epl25 Union SELECT * FROM Eredevisie25 ORDER BY Tframe ASC"
df = pd.read_sql(query, conn)

# Column index map:
# ------------------------------------------------------
# 0: Match ID
# 1: Round
# 2: Tframe (timeframe)
# 3: Home Team
# 4: Away Team
# 5: Full_HomeGoals (FT)
# 6: Full_AwayGoals (FT)
# 7: FirstHalf_HomeGoals (1H)
# 8: FirstHalf_AwayGoals (1H)
# ------------------------------------------------------

round_col = df.columns[1]
col5, col6, col7, col8 = df.columns[5], df.columns[6], df.columns[7], df.columns[8]

# Convert to numeric safely
for col in [col5, col6, col7, col8]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ======================================================
# ⚽ 3️⃣ FULL-TIME ANALYSIS
# ======================================================
df["FullSum"] = df[col5] + df[col6]
df["FullHWin"] = (df[col5] > df[col6]).astype(int)
df["FullDC"] = (df[col5] != df[col6]).astype(int)
df["FullBTS"] = ((df[col5] > 0) & (df[col6] > 0)).astype(int)

for n in range(6):
    df[f"FullExcGols{n}"] = (df["FullSum"] == n).astype(int)

df["FullOverZ"] = (df["FullSum"] > 0).astype(int)
df["FullOver1"] = (df["FullSum"] > 1).astype(int)
df["FullOver2"] = (df["FullSum"] > 2).astype(int)
df["FullOver3"] = (df["FullSum"] > 3).astype(int)
df["FullOver4"] = (df["FullSum"] > 4).astype(int)
df["FullOver5"] = (df["FullSum"] > 5).astype(int)
df["FullOdd"] = (df["FullSum"] % 2 != 0).astype(int)
df["FullEven"] = (df["FullSum"] % 2 == 0).astype(int)

df["FullGolRang0-1"] = (df["FullSum"] <= 1).astype(int)
df["FullGolRang2-3"] = ((df["FullSum"] >= 2) & (df["FullSum"] <= 3)).astype(int)
df["FullGolRang4-5"] = ((df["FullSum"] >= 4) & (df["FullSum"] <= 5)).astype(int)

df["FullMultiScor1,2,3:0"] = ((df[col5].between(1, 3)) & (df[col6] == 0)).astype(int)
df["FullMultiScor0:1,2,3"] = ((df[col5] == 0) & (df[col6].between(1, 3))).astype(int)
df["FullMultiScor4,5,6:0"] = ((df[col5].between(4, 6)) & (df[col6] == 0)).astype(int)
df["FullMultiScor0:4,5,6"] = ((df[col5] == 0) & (df[col6].between(4, 6))).astype(int)

# ======================================================
# ⏱️ 4️⃣ FIRST HALF ANALYSIS
# ======================================================
df["FirstSum"] = df[col7] + df[col8]
df["FirstHWin"] = (df[col7] > df[col8]).astype(int)
df["FirstAWin"] = (df[col7] < df[col8]).astype(int)
df["FirstDraw"] = (df[col7] == df[col8]).astype(int)
df["FirstBTS"] = ((df[col7] > 0) & (df[col8] > 0)).astype(int)

for n in range(3):
    df[f"FirstExcGols{n}"] = (df["FirstSum"] == n).astype(int)

df["FirstOver0"] = (df["FirstSum"] > 0).astype(int)
df["FirstOver1"] = (df["FirstSum"] > 1).astype(int)
df["FirstOver2"] = (df["FirstSum"] > 2).astype(int)
df["FirstOdd"] = (df["FirstSum"] % 2 != 0).astype(int)
df["FirstEven"] = (df["FirstSum"] % 2 == 0).astype(int)
df["FirstGolRang0-1"] = (df["FirstSum"] <= 1).astype(int)
df["FirstGolRang2-3"] = ((df["FirstSum"] >= 2) & (df["FirstSum"] <= 3)).astype(int)

# ======================================================
# 🔁 5️⃣ SECOND HALF (DIFFERENCE) ANALYSIS
# ======================================================
df["Sum5_6"] = df[col5] + df[col6]
df["Sum7_8"] = df[col7] + df[col8]
df["Diff56_78"] = df["Sum5_6"] - df["Sum7_8"]

df["SecHWin"] = ((df[col5] - df[col7]) > (df[col6] - df[col8])).astype(int)
df["SecAWin"] = ((df[col5] - df[col7]) < (df[col6] - df[col8])).astype(int)
df["SecDraw"] = ((df[col5] - df[col7]) == (df[col6] - df[col8])).astype(int)
df["SecBTS"] = ((df[col5] - df[col7] > 0) & (df[col6] - df[col8] > 0)).astype(int)

df["SecOdd"] = (df["Diff56_78"] % 2 != 0).astype(int)
df["SecEven"] = (df["Diff56_78"] % 2 == 0).astype(int)
df["SecHandi2:0"] = ((df[col5] - df[col7] + 2) > (df[col6] - df[col8])).astype(int)

# Correct Score Patterns
patterns = [
    ("1:0", 1, 0), ("2:0", 2, 0), ("2:1", 2, 1), ("0:0", 0, 0),
    ("1:1", 1, 1), ("0:1", 0, 1), ("0:2", 0, 2), ("1:2", 1, 2)
]
for name, a, b in patterns:
    df[f"SecCorrScor{name}"] = (((df[col5] - df[col7]) == a) & ((df[col6] - df[col8]) == b)).astype(int)

# ======================================================
# 📊 6️⃣ ROUND SUMMARY AGGREGATION
# ======================================================
# Group by round and sum all numeric columns (metrics)
round_summary = df.groupby(round_col).sum(numeric_only=True).reset_index()

# ======================================================
# 💾 7️⃣ EXPORT RESULTS TO EXCEL
# ======================================================
with pd.ExcelWriter("Full_First_Sec_Analysis_Extended20.xlsx") as writer:
    df.to_excel(writer, sheet_name="Match_Analysis", index=False)
    round_summary.to_excel(writer, sheet_name="Round_Summary", index=False)

conn.close()

print("✅ Full-Time, First-Half, and Second-Half analyses saved to Full_First_Sec_Analysis_Extended20.xlsx")
print("✅ Includes both match-level and round-level summaries")
