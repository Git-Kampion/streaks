# save as build_combinations.py and run: python build_combinations.py
import pandas as pd
import numpy as np

# CONFIG
INPUT_CSV = "Full_First_Sec_Analysis_Handicaps_CorrectScores.xlsx"             # your datasource (exported Excel saved as CSV)
HIGH_CONF_FILE = "combos_high_confidence.xlsx"
MED_CONF_FILE  = "combos_medium_confidence.xlsx"
HIGH_THRESH = 0.90
MED_LO = 0.60
MED_HI = 0.8999999   # < 0.90

# 1) load
df = pd.read_csv(INPUT_CSV)

# 2) find GamesPlayed column and numeric metric columns
if "GamesPlayed" not in df.columns:
    raise SystemExit("GamesPlayed column not found in input.csv")

games_col = "GamesPlayed"

# Select numeric columns excluding GamesPlayed and the team name column(s)
exclude = {games_col}
# auto-detect possible team-name columns (common: 'home', 'team', 'Team')
possible_name_cols = [c for c in df.columns if c.lower() in ("home","team","team_name","club")]
if possible_name_cols:
    team_col = possible_name_cols[0]
    exclude.add(team_col)
else:
    # if no common team name header present, we still proceed without excluding
    team_col = None

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
metric_cols = [c for c in numeric_cols if c not in exclude]

# 3) Build boolean variants: metric_full (==GamesPlayed) and metric_zero (==0)
bool_cols = []
for m in metric_cols:
    full_name = f"{m}__full"   # equals GamesPlayed
    zero_name = f"{m}__zero"   # equals 0
    # per-row comparison to that row's GamesPlayed:
    df[full_name] = (df[m] == df[games_col])
    df[zero_name] = (df[m] == 0)
    bool_cols.extend([full_name, zero_name])

# 4) helper to compute pairwise co-occurrence and conditional probs
rows = []
n_bool = len(bool_cols)
for i in range(n_bool):
    for j in range(n_bool):
        if i == j:
            continue
        a = bool_cols[i]
        b = bool_cols[j]
        support_a = int(df[a].sum())
        support_b = int(df[b].sum())
        both = int((df[a] & df[b]).sum())
        if support_a == 0:
            p_b_given_a = np.nan
        else:
            p_b_given_a = both / support_a
        if support_b == 0:
            p_a_given_b = np.nan
        else:
            p_a_given_b = both / support_b
        confidence = max(p for p in [p_b_given_a, p_a_given_b] if not pd.isna(p)) if (not pd.isna(p_b_given_a) or not pd.isna(p_a_given_b)) else np.nan

        # parse metric and state
        metric_a, state_a = a.rsplit("__", 1)
        metric_b, state_b = b.rsplit("__", 1)

        rows.append({
            "metric_A": metric_a,
            "state_A": state_a,
            "metric_B": metric_b,
            "state_B": state_b,
            "support_A": support_a,
            "support_B": support_b,
            "both_count": both,
            "P(B|A)": p_b_given_a,
            "P(A|B)": p_a_given_b,
            "confidence": confidence,
            "recommended_direction": (f"{metric_a} ({state_a}) => {metric_b} ({state_b})"
                                      if (not pd.isna(p_b_given_a) and p_b_given_a >= (HIGH_THRESH if p_b_given_a>=HIGH_THRESH else MED_LO))
                                      else (f"{metric_b} ({state_b}) => {metric_a} ({state_a})" if (not pd.isna(p_a_given_b) and p_a_given_b >= (HIGH_THRESH if p_a_given_b>=HIGH_THRESH else MED_LO)) else "")),
        })

pairs_df = pd.DataFrame(rows)

# 5) Filter into High and Medium sets
# High: any direction probability >= HIGH_THRESH
high_df = pairs_df[(pairs_df["P(B|A)"] >= HIGH_THRESH) | (pairs_df["P(A|B)"] >= HIGH_THRESH)].copy()
high_df = high_df.sort_values(["confidence", "both_count"], ascending=[False, False])

# Medium: >= MED_LO and < 0.90 (either way)
cond_med = (
    ((pairs_df["P(B|A) >= " if False else "P(B|A)"] >= MED_LO) & (pairs_df["P(B|A)"] < 0.9)) |
    ((pairs_df["P(A|B)"] >= MED_LO) & (pairs_df["P(A|B)"] < 0.9))
)
# NOTE: above expression needs to reference columns directly — build logically:
med_mask = (
    ((pairs_df["P(B|A)"] >= MED_LO) & (pairs_df["P(B|A)"] < 0.9)) |
    ((pairs_df["P(A|B)"] >= MED_LO) & (pairs_df["P(A|B)"] < 0.9))
)
med_df = pairs_df[med_mask].copy()
med_df = med_df.sort_values(["confidence", "both_count"], ascending=[False, False])

# 6) Small human readable notes
def note_row(r):
    # prefer the direction with higher prob
    pa = r["P(B|A)"]
    pb = r["P(A|B)"]
    if pd.isna(pa) and pd.isna(pb):
        return ""
    if pd.isna(pb) or (not pd.isna(pa) and pa >= pb):
        return f"When {r['metric_A']} ({r['state_A']}) occurs, {r['metric_B']} ({r['state_B']}) also occurs {pa:.2%}"
    else:
        return f"When {r['metric_B']} ({r['state_B']}) occurs, {r['metric_A']} ({r['state_A']}) also occurs {pb:.2%}"

for df_out in (high_df, med_df):
    df_out["notes"] = df_out.apply(note_row, axis=1)

# 7) Export to Excel
with pd.ExcelWriter(HIGH_CONF_FILE) as writer:
    high_df.to_excel(writer, sheet_name="high_conf_pairs", index=False)

with pd.ExcelWriter(MED_CONF_FILE) as writer:
    med_df.to_excel(writer, sheet_name="medium_conf_pairs", index=False)

print("Done. Files written:")
print(" -", HIGH_CONF_FILE)
print(" -", MED_CONF_FILE)
