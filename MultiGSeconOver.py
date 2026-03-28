import pyodbc
import pandas as pd

# ======================================================
# 🧩 1️⃣ CONNECT TO ACCESS DATABASE
# ======================================================
db_path = r"C:\Users\letenok.DWA\Documents\streaks\results2026.accdb"
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)
conn = pyodbc.connect(conn_str)

# ======================================================  UNION SELECT * FROM Eredevisie25 ORDER BY Tframe ASC
# 🧮 2️⃣ LOAD DATA AND SET COLUMN REFERENCES
# ======================================================
query = "SELECT * FROM IndonesiaPrem25 UNION SELECT * FROM MyanmarNatLeag25 UNION SELECT * FROM SingPorePrem25 UNION SELECT * FROM IsraelA25 UNION SELECT * FROM AlgeriaA25 UNION SELECT * FROM Turk225 UNION SELECT * FROM SerieA25 ORDER BY Tframe ASC"
df = pd.read_sql(query, conn)

# Column index map:
# ------------------------------------------------------
# 0: Match ID
# 1: Round
# 2: Tframe (timeframe)
# 3: Home Team
# 4: Away Team
# 5: Home Full time Score
# 6: Away Full time Score
# 7: Home First Half Score
# 8: Away First Half Score
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
df["FullAWin"] = (df[col6] > df[col5]).astype(int)
df["FullDC"] = (df[col5] == df[col6]).astype(int)
df["FullBTS"] = ((df[col5] > 0) & (df[col6] > 0)).astype(int)

for n in range(6):
    df[f"FullExcGols{n}"] = (df["FullSum"] == n).astype(int)

df["FullOver0"] = (df["FullSum"] > 0).astype(int)
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
# 🎯 FULL-TIME MULTI-GOALS MODELS
# ======================================================
df["FulltimeMultiGoals1-2"] = ((df["FullSum"] >= 1) & (df["FullSum"] <= 2)).astype(int)
df["FulltimeMultiGoals1-3"] = ((df["FullSum"] >= 1) & (df["FullSum"] <= 3)).astype(int)
df["FulltimeMultiGoals1-4"] = ((df["FullSum"] >= 1) & (df["FullSum"] <= 4)).astype(int)
df["FulltimeMultiGoals1-5"] = ((df["FullSum"] >= 1) & (df["FullSum"] <= 5)).astype(int)
df["FulltimeMultiGoals1-6"] = ((df["FullSum"] >= 1) & (df["FullSum"] <= 6)).astype(int)
df["FulltimeMultiGoals2-3"] = ((df["FullSum"] >= 2) & (df["FullSum"] <= 3)).astype(int)
df["FulltimeMultiGoals2-4"] = ((df["FullSum"] >= 2) & (df["FullSum"] <= 4)).astype(int)
df["FulltimeMultiGoals2-5"] = ((df["FullSum"] >= 2) & (df["FullSum"] <= 5)).astype(int)
df["FulltimeMultiGoals2-6"] = ((df["FullSum"] >= 2) & (df["FullSum"] <= 6)).astype(int)
df["FulltimeMultiGoals3-4"] = ((df["FullSum"] >= 3) & (df["FullSum"] <= 4)).astype(int)
df["FulltimeMultiGoals3-5"] = ((df["FullSum"] >= 3) & (df["FullSum"] <= 5)).astype(int)
df["FulltimeMultiGoals3-6"] = ((df["FullSum"] >= 3) & (df["FullSum"] <= 6)).astype(int)
df["FulltimeMultiGoals4-5"] = ((df["FullSum"] >= 4) & (df["FullSum"] <= 5)).astype(int)
df["FulltimeMultiGoals4-6"] = ((df["FullSum"] >= 4) & (df["FullSum"] <= 6)).astype(int)
df["FulltimeMultiGoals5-6"] = ((df["FullSum"] >= 5) & (df["FullSum"] <= 6)).astype(int)
df["FulltimeMultiGoals7+"]  = (df["FullSum"] >= 7).astype(int)

# ======================================================
# 🏆 FULL-TIME WINNING MARGINS
# ======================================================

# Full-time Home and Away Goal Difference
df["FulltimeGoalDiff"] = df[col5] - df[col6]

# 🏠 Home Winning Margins
df["WinningMarginHomeBy1"] = ((df["FulltimeGoalDiff"] == 1)).astype(int)
df["WinningMarginHomeBy2"] = ((df["FulltimeGoalDiff"] == 2)).astype(int)
df["WinningMarginHomeBy3"] = ((df["FulltimeGoalDiff"] == 3)).astype(int)

# ✈️ Away Winning Margins
df["WinningMarginAwayBy1"] = ((df["FulltimeGoalDiff"] == -1)).astype(int)
df["WinningMarginAwayBy2"] = ((df["FulltimeGoalDiff"] == -2)).astype(int)
df["WinningMarginAwayBy3"] = ((df["FulltimeGoalDiff"] == -3)).astype(int)

# ======================================================
# ⚽ FULL-TIME HOME & AWAY OVER GOALS
# ======================================================

# 🏠 Full-Time Home Over Goals
df["FulltimeHomeOverZ"] = (df[col5] > 0).astype(int)
df["FulltimeHomeOver1"] = (df[col5] > 1).astype(int)
df["FulltimeHomeOver2"] = (df[col5] > 2).astype(int)
df["FulltimeHomeOver3"] = (df[col5] > 3).astype(int)

# ✈️ Full-Time Away Over Goals
df["FulltimeAwayOverZ"] = (df[col6] > 0).astype(int)
df["FulltimeAwayOver1"] = (df[col6] > 1).astype(int)
df["FulltimeAwayOver2"] = (df[col6] > 2).astype(int)
df["FulltimeAwayOver3"] = (df[col6] > 3).astype(int)


# ======================================================
# ⏱️ FIRST HALF HOME & AWAY OVER GOALS
# ======================================================

# 🏠 First Half Home Over Goals
df["FirstHalfHomeOverZ"] = (df[col7] > 0).astype(int)
df["FirstHalfHomeOver1"] = (df[col7] > 1).astype(int)
df["FirstHalfHomeOver2"] = (df[col7] > 2).astype(int)
df["FirstHalfHomeOver3"] = (df[col7] > 3).astype(int)

# ✈️ First Half Away Over Goals
df["FirstHalfAwayOverZ"] = (df[col8] > 0).astype(int)
df["FirstHalfAwayOver1"] = (df[col8] > 1).astype(int)
df["FirstHalfAwayOver2"] = (df[col8] > 2).astype(int)
df["FirstHalfAwayOver3"] = (df[col8] > 3).astype(int)


# ======================================================
# 🏠🏃 HOME & AWAY MULTI-GOALS MODELS
# ======================================================

# ---- HOME MULTI GOALS ----
df["HomeMultiGoals1-2"] = ((df[col5] >= 1) & (df[col5] <= 2)).astype(int)
df["HomeMultiGoals1-3"] = ((df[col5] >= 1) & (df[col5] <= 3)).astype(int)
df["HomeMultiGoals2-3"] = ((df[col5] >= 2) & (df[col5] <= 3)).astype(int)
df["HomeMultiGoals4+"]  = (df[col5] >= 4).astype(int)

# ---- AWAY MULTI GOALS ----
df["AwayMultiGoals1-2"] = ((df[col6] >= 1) & (df[col6] <= 2)).astype(int)
df["AwayMultiGoals1-3"] = ((df[col6] >= 1) & (df[col6] <= 3)).astype(int)
df["AwayMultiGoals2-3"] = ((df[col6] >= 2) & (df[col6] <= 3)).astype(int)
df["AwayMultiGoals4+"]  = (df[col6] >= 4).astype(int)


# ======================================================
# 🎯 FULL-TIME CORRECT SCORES (ALL 0–4)
# ======================================================
for h in range(5):
    for a in range(5):
        df[f"FulltimeCorrectScore{h}-{a}"] = ((df[col5] == h) & (df[col6] == a)).astype(int)

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
# 🎯 FIRST HALF CORRECT SCORES (9 CORE)
# ======================================================
correct_scores_half = [
    (1, 0), (2, 0), (0, 0), (0, 1), (1, 1),
    (0, 2), (2, 1), (2, 2), (1, 2)
]
for h, a in correct_scores_half:
    df[f"FirstHalfCorrectScore{h}-{a}"] = ((df[col7] == h) & (df[col8] == a)).astype(int)

# ======================================================
# 🎯 FIRST HALF MULTIGOALS
# ======================================================
df["1stHalfMultigoals1-2"] = ((df["FirstSum"] >= 1) & (df["FirstSum"] <= 2)).astype(int)
df["1stHalfMultigoals1-3"] = ((df["FirstSum"] >= 1) & (df["FirstSum"] <= 3)).astype(int)
df["1stHalfMultigoals2-3"] = ((df["FirstSum"] >= 2) & (df["FirstSum"] <= 3)).astype(int)
df["1stHalfMultigoals4+"]  = (df["FirstSum"] >= 4).astype(int)

# ======================================================
# 🔁 5️⃣ SECOND HALF ANALYSIS (DIFFERENCE)
# ======================================================
df["SecHome"] = df[col5] - df[col7]
df["SecAway"] = df[col6] - df[col8]
df["Diff56_78"] = df[col5] + df[col6] - df[col7] - df[col8]

df["SecHWin"] = (df["SecHome"] > df["SecAway"]).astype(int)
df["SecAWin"] = (df["SecHome"] < df["SecAway"]).astype(int)
df["SecDraw"] = (df["SecHome"] == df["SecAway"]).astype(int)
df["SecBTS"] = ((df["SecHome"] > 0) & (df["SecAway"] > 0)).astype(int)
df["SecOdd"] = (df["Diff56_78"] % 2 != 0).astype(int)
df["SecEven"] = (df["Diff56_78"] % 2 == 0).astype(int)

# ======================================================
# 🎯 SECOND HALF CORRECT SCORES (9 CORE)
# ======================================================
for h, a in correct_scores_half:
    df[f"SecondHalfCorrectScore{h}-{a}"] = ((df["SecHome"] == h) & (df["SecAway"] == a)).astype(int)

# ======================================================
# ⏳ SECOND HALF MULTIGOALS
# ======================================================
df["2ndHalfMultigoals1-2"] = (((df["SecHome"] + df["SecAway"]) >= 1) & ((df["SecHome"] + df["SecAway"]) <= 2)).astype(int)
df["2ndHalfMultigoals1-3"] = (((df["SecHome"] + df["SecAway"]) >= 1) & ((df["SecHome"] + df["SecAway"]) <= 3)).astype(int)
df["2ndHalfMultigoals2-3"] = (((df["SecHome"] + df["SecAway"]) >= 2) & ((df["SecHome"] + df["SecAway"]) <= 3)).astype(int)
df["2ndHalfMultigoals4+"]  = ((df["SecHome"] + df["SecAway"]) >= 4).astype(int)

# ======================================================
# 🚀 SECOND HALF OVER MODELS
# ======================================================

df["2ndHalfOverZ"] = ((df["SecHome"] + df["SecAway"]) > 0).astype(int)
df["2ndHalfOver1"] = ((df["SecHome"] + df["SecAway"]) > 1).astype(int)
df["2ndHalfOver2"] = ((df["SecHome"] + df["SecAway"]) > 2).astype(int)

# ======================================================
# 🎯 SECOND HALF EXACT GOALS
# ======================================================

df["2ndHalfExcatGoal0"] = ((df["SecHome"] + df["SecAway"]) == 0).astype(int)
df["2ndHalfExcatGoal1"] = ((df["SecHome"] + df["SecAway"]) == 1).astype(int)
df["2ndHalfExcatGoal2"] = ((df["SecHome"] + df["SecAway"]) >= 2).astype(int)

# ======================================================
# 🏠 SECOND HALF HOME OVER MODELS
# ======================================================

df["2ndHalfHomeOverZ"] = (df["SecHome"] > 0).astype(int)
df["2ndHalfHomeOver1"] = (df["SecHome"] > 1).astype(int)
df["2ndHalfHomeOver2"] = (df["SecHome"] > 2).astype(int)

# ======================================================
# 🛫 SECOND HALF AWAY OVER MODELS
# ======================================================

df["2ndHalfAwayOverZ"] = (df["SecAway"] > 0).astype(int)
df["2ndHalfAwayOver1"] = (df["SecAway"] > 1).astype(int)
df["2ndHalfAwayOver2"] = (df["SecAway"] > 2).astype(int)


# ======================================================
# 🏁 FULL-TIME HANDICAPS
# ======================================================
df["FulltimeHandiHome0:1"] = (df[col6] + 1 < df[col5]).astype(int)
df["FulltimeHandiAway0:1"] = (df[col5] < df[col6] + 1).astype(int)
df["FulltimeHandiDraw0:1"] = (df[col5] == df[col6] + 1).astype(int)

df["FulltimeHandiHome0:2"] = (df[col6] + 2 < df[col5]).astype(int)
df["FulltimeHandiAway0:2"] = (df[col5]  < df[col6] + 2).astype(int)
df["FulltimeHandiDraw0:2"] = (df[col5]  == df[col6] + 2).astype(int)

df["FulltimeHandiHome0:3"] = (df[col6] + 3 < df[col5]).astype(int)
df["FulltimeHandiAway0:3"] = (df[col5]  < df[col6] + 3).astype(int)
df["FulltimeHandiDraw0:3"] = (df[col5]  == df[col6] + 3).astype(int)

df["FulltimeHandiHome0:4"] = (df[col6] + 4 < df[col5]).astype(int)
df["FulltimeHandiAway0:4"] = (df[col5]  < df[col6] + 4).astype(int)
df["FulltimeHandiDraw0:4"] = (df[col5]  == df[col6] + 4).astype(int)

df["FulltimeHandiHome0:5"] = (df[col6] + 5 < df[col5]).astype(int)
df["FulltimeHandiAway0:5"] = (df[col5]  < df[col6] + 5).astype(int)
df["FulltimeHandiDraw0:5"] = (df[col5]  == df[col6] + 5).astype(int)

# ======================================================
# 🏆 EITHER HALF WINNING ANALYSIS
# ======================================================
# Home wins either half if home scored more than away in 1st or 2nd half
df["HomeWinEitherHalfYes"] = (
    ((df[col7] > df[col8]) | (df["SecHome"] > df["SecAway"]))
).astype(int)
df["HomeWinEitherHalfNo"] = (1 - df["HomeWinEitherHalfYes"]).astype(int)

# Away wins either half if away scored more than home in 1st or 2nd half
df["AwayWinEitherHalfYes"] = (
    ((df[col8] > df[col7]) | (df["SecAway"] > df["SecHome"]))
).astype(int)
df["AwayWinEitherHalfNo"] = (1 - df["AwayWinEitherHalfYes"]).astype(int)

# ======================================================
# ⚖️ HIGHEST SCORING HALF (HOME & AWAY)
# ======================================================

# 🏠 HOME TEAM
df["HomeHighestScoringHalve1st"] = (df[col7] > df["SecHome"]).astype(int)
df["HomeHighestScoringHalve2nd"] = (df["SecHome"] > df[col7]).astype(int)
df["HomeHighestScoringHalveEqual"] = (df[col7] == df["SecHome"]).astype(int)

# 🚗 AWAY TEAM
df["AwayHighestScoringHalve1st"] = (df[col8] > df["SecAway"]).astype(int)
df["AwayHighestScoringHalve2nd"] = (df["SecAway"] > df[col8]).astype(int)
df["AwayHighestScoringHalveEqual"] = (df[col8] == df["SecAway"]).astype(int)


for h in [1, 2, 3, 4, 5]:
    df[f"FulltimeHandiHome{h}:0"] = ((df[col5] + h) > df[col6]).astype(int)
    df[f"FulltimeHandiAway{h}:0"] = ((df[col6] + h) > df[col5]).astype(int)
    df[f"FulltimeHandiDraw{h}:0"] = ((df[col5] + h) == df[col6]).astype(int)

# ======================================================
# ⏱️ FIRST-HALF HANDICAPS
# ======================================================
df["FirstHalfHandiHome0:1"] = (df[col8] + 1 < df[col7]).astype(int)
df["FirstHalfHandiAway0:1"] = (df[col7]  < df[col8] + 1).astype(int)
df["FirstHalfHandiDraw0:1"] = (df[col7]  == df[col8] + 1).astype(int)

df["FirstHalfHandiHome0:2"] = (df[col8] + 2 < df[col7]).astype(int)
df["FirstHalfHandiAway0:2"] = (df[col7]  < df[col8] + 2).astype(int)
df["FirstHalfHandiDraw0:2"] = (df[col7]  == df[col8] + 2).astype(int)

df["FirstHalfHandiHome0:3"] = (df[col8] + 3 < df[col7]).astype(int)
df["FirstHalfHandiAway0:3"] = (df[col7]  < df[col8] + 3).astype(int)
df["FirstHalfHandiDraw0:3"] = (df[col7]  == df[col8] + 3).astype(int)

for h in [1, 2, 3]:
    df[f"FirstHalfHandiHome{h}:0"] = ((df[col7] + h) > df[col8]).astype(int)
    df[f"FirstHalfHandiAway{h}:0"] = ((df[col8] + h) > df[col7]).astype(int)
    df[f"FirstHalfHandiDraw{h}:0"] = ((df[col7] + h) == df[col8]).astype(int)

# ======================================================
# ⏳ SECOND-HALF HANDICAPS
# ======================================================
df["SecHalfHandiHome0:1"] = (df["SecAway"] + 1 < df["SecHome"]).astype(int)
df["SecHalfHandiAway0:1"] = (df["SecHome"]  < df["SecAway"] + 1).astype(int)
df["SecHalfHandiDraw0:1"] = (df["SecHome"] == df["SecAway"] + 1).astype(int)

df["SecHalfHandiHome0:2"] = (df["SecAway"] + 2 < df["SecHome"]).astype(int)
df["SecHalfHandiAway0:2"] = (df["SecHome"]  < df["SecAway"] + 2).astype(int)
df["SecHalfHandiDraw0:2"] = (df["SecHome"] == df["SecAway"] + 2).astype(int)

for h in [1, 2, 3]:
    df[f"SecHalfHandiHome{h}:0"] = ((df["SecHome"] + h) > df["SecAway"]).astype(int)
    df[f"SecHalfHandiAway{h}:0"] = ((df["SecAway"] + h) > df["SecHome"]).astype(int)
    df[f"SecHalfHandiDraw{h}:0"] = ((df["SecHome"] + h) == df["SecAway"]).astype(int)


# ======================================================
# 🔗 8️⃣ COMBINED WIN/DRAW METRICS (Full / 1H / 2H)
# ======================================================

# --- Full-Time Combined ---
df["Full_HomeOrDraw"] = ((df["FullHWin"] == 1) | (df["FullDC"] == 1)).astype(int)
df["Full_AwayOrDraw"] = ((df["FullAWin"] == 1) | (df["FullDC"] == 1)).astype(int)
df["Full_HomeOrAway"] = ((df["FullHWin"] == 1) | (df["FullAWin"] == 1)).astype(int)

# --- First-Half Combined ---
df["1H_HomeOrDraw"] = ((df["FirstHWin"] == 1) | (df["FirstDraw"] == 1)).astype(int)
df["1H_AwayOrDraw"] = ((df["FirstAWin"] == 1) | (df["FirstDraw"] == 1)).astype(int)
df["1H_HomeOrAway"] = ((df["FirstHWin"] == 1) | (df["FirstAWin"] == 1)).astype(int)

# --- Second-Half Combined ---
df["2H_HomeOrDraw"] = ((df["SecHWin"] == 1) | (df["SecDraw"] == 1)).astype(int)
df["2H_AwayOrDraw"] = ((df["SecAWin"] == 1) | (df["SecDraw"] == 1)).astype(int)
df["2H_HomeOrAway"] = ((df["SecHWin"] == 1) | (df["SecAWin"] == 1)).astype(int)

# ======================================================
# 🎯 Multigoal Combination Metric (Full + 1H + 2H + DC)
# ======================================================

df["Multigoal1st2ndfullDC"] = (
    (df["FulltimeMultiGoals3-6"] == 1) &
    (df["1stHalfMultigoals1-3"] == 1) &
    (df["2ndHalfMultigoals1-3"] == 1) &
    (
        (df["Full_HomeOrDraw"] == 1) |
        (df["Full_AwayOrDraw"] == 1) |
        (df["Full_HomeOrAway"] == 1)
    )
).astype(int)



# ======================================================
# 📊 6️⃣ ROUND SUMMARY AGGREGATION
# ======================================================
round_summary = df.groupby(round_col).sum(numeric_only=True).reset_index()

# ======================================================
# 🏟️ 6B️⃣ GROUPING BY HOME TEAM & AWAY TEAM
# ======================================================

home_team_col = df.columns[3]   # Home Team
away_team_col = df.columns[4]   # Away Team

Home_Team_Summary = df.groupby(home_team_col).sum(numeric_only=True).reset_index()
Away_Team_Summary = df.groupby(away_team_col).sum(numeric_only=True).reset_index()

Home_Team_Summary.to_csv("Home_Team_Summary.csv", index=False)
Away_Team_Summary.to_csv("Away_Team_Summary.csv", index=False)

# ======================================================
# 🏟️ REFRESH TEAM SUMMARIES INCLUDING NEW METRIC
# ======================================================
Home_Team_Summary = df.groupby(home_team_col).sum(numeric_only=True).reset_index()
Away_Team_Summary = df.groupby(away_team_col).sum(numeric_only=True).reset_index()

Home_Team_Summary.to_csv("Home_Team_Summary.csv", index=False)
Away_Team_Summary.to_csv("Away_Team_Summary.csv", index=False)


# ======================================================
# 💾 EXPORT TO EXCEL
# ======================================================
with pd.ExcelWriter("Full_First_Sec_Analysis_Handicaps_CorrectScores20260121.xlsx") as writer:
    df.to_excel(writer, sheet_name="Match_Analysis", index=False)
    round_summary.to_excel(writer, sheet_name="Round_Summary", index=False)
    Home_Team_Summary.to_excel(writer, sheet_name="Home_Team_Summary", index=False)
    Away_Team_Summary.to_excel(writer, sheet_name="Away_Team_Summary", index=False)

print("✅ Done — Metric added to match data, team summaries, and round summary!")
