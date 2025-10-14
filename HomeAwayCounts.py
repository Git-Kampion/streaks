import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("🚀 Script started...")

# Path to your Access database
db_path = r"C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb"

# Build connection string
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
)

try:
    print("🔗 Connecting to database...")
    # Connect to Access
    conn = pyodbc.connect(conn_str)
    print("✅ Database connected successfully")

    # ---- Replace with your actual table names ----
    query = """
    SELECT * FROM portLeag25
    ORDER BY Tframe ASC
    """
    
    print("📊 Loading data from database...")
    df = pd.read_sql(query, conn)
    print(f"✅ Data loaded: {len(df)} rows")
    
    # Identify columns
    home_team_col = df.columns[3]  # 4th column (index 3)
    away_team_col = df.columns[4]  # 5th column (index 4)
    last_two_cols = df.columns[-2:]
    score1, score2 = last_two_cols  # Home score, Away score

    print(f"🏠 Home Team Column: {home_team_col}")
    print(f"✈️ Away Team Column: {away_team_col}")
    print(f"📊 Score Columns: {score1}, {score2}")

    # Convert to numeric (only score columns)
    for col in last_two_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Create HOZ and AOZ columns
    df["HOZ"] = df[score1]  # Home team goals
    df["AOZ"] = df[score2]  # Away team goals

    # Create sum column
    df["SumLastTwo"] = df["HOZ"] + df["AOZ"]

    # Create G0U3 column: 1 if total goals between 1 and 2 (inclusive)
    df['G0U3'] = ((df['SumLastTwo'] > 0) & (df['SumLastTwo'] < 3)).astype(int)

    # --- Stats Calculations for HOME TEAMS ---
    print("📈 Calculating HOME team stats...")
    
    # ODD/EVEN for Home Teams
    df_odd_home = df[df["SumLastTwo"] % 2 != 0]
    df_even_home = df[df["SumLastTwo"] % 2 == 0]

    odd_counts_home = df_odd_home.groupby(home_team_col).size().reset_index(name="Odd")
    even_counts_home = df_even_home.groupby(home_team_col).size().reset_index(name="Even")

    # DRAW for Home Teams
    df_draw_home = df[df["HOZ"] == df["AOZ"]]
    draw_counts_home = df_draw_home.groupby(home_team_col).size().reset_index(name="Draw")

    # G0, G1, G2 for Home Teams
    g0_counts_home = df[df["SumLastTwo"] > 0].groupby(home_team_col).size().reset_index(name="G0")
    g1_counts_home = df[df["SumLastTwo"] > 1].groupby(home_team_col).size().reset_index(name="G1")
    g2_counts_home = df[df["SumLastTwo"] > 2].groupby(home_team_col).size().reset_index(name="G2")
    g0u3_counts_home = df[df['G0U3'] == 1].groupby(home_team_col).size().reset_index(name='G0U3')

    # Home Wins for Home Teams (when HOZ > AOZ)
    hwin_counts_home = df[df["HOZ"] > df["AOZ"]].groupby(home_team_col).size().reset_index(name="HWin")
    
    # Away Wins for Home Teams (when AOZ > HOZ) - from home team's perspective
    awin_counts_home = df[df["AOZ"] > df["HOZ"]].groupby(home_team_col).size().reset_index(name="AWin")
    
    # BTTS for Home Teams
    btts_counts_home = df[(df["HOZ"] > 0) & (df["AOZ"] > 0)].groupby(home_team_col).size().reset_index(name="BTTS")

    # HOZ and AOZ counts for Home Teams (counting occurrences, not summing goals)
    hoz_counts_home = df[df["HOZ"] > 0].groupby(home_team_col).size().reset_index(name="HOZ_Count")  # Count matches where HOZ > 0
    aoz_counts_home = df[df["AOZ"] > 0].groupby(home_team_col).size().reset_index(name="AOZ_Count")  # Count matches where AOZ > 0

    # Total matches per home team
    total_counts_home = df.groupby(home_team_col).size().reset_index(name="Total")

    # --- Stats Calculations for AWAY TEAMS ---
    print("📈 Calculating AWAY team stats...")
    
    # ODD/EVEN for Away Teams
    df_odd_away = df[df["SumLastTwo"] % 2 != 0]
    df_even_away = df[df["SumLastTwo"] % 2 == 0]

    odd_counts_away = df_odd_away.groupby(away_team_col).size().reset_index(name="Odd")
    even_counts_away = df_even_away.groupby(away_team_col).size().reset_index(name="Even")

    # DRAW for Away Teams
    df_draw_away = df[df["HOZ"] == df["AOZ"]]
    draw_counts_away = df_draw_away.groupby(away_team_col).size().reset_index(name="Draw")

    # G0, G1, G2 for Away Teams
    g0_counts_away = df[df["SumLastTwo"] > 0].groupby(away_team_col).size().reset_index(name="G0")
    g1_counts_away = df[df["SumLastTwo"] > 1].groupby(away_team_col).size().reset_index(name="G1")
    g2_counts_away = df[df["SumLastTwo"] > 2].groupby(away_team_col).size().reset_index(name="G2")
    g0u3_counts_away = df[df['G0U3'] == 1].groupby(away_team_col).size().reset_index(name='G0U3')

    # Home Wins for Away Teams (when HOZ > AOZ) - from away team's perspective
    hwin_counts_away = df[df["HOZ"] > df["AOZ"]].groupby(away_team_col).size().reset_index(name="HWin")
    
    # Away Wins for Away Teams (when AOZ > HOZ)
    awin_counts_away = df[df["AOZ"] > df["HOZ"]].groupby(away_team_col).size().reset_index(name="AWin")
    
    # BTTS for Away Teams
    btts_counts_away = df[(df["HOZ"] > 0) & (df["AOZ"] > 0)].groupby(away_team_col).size().reset_index(name="BTTS")

    # HOZ and AOZ counts for Away Teams (counting occurrences, not summing goals)
    hoz_counts_away = df[df["HOZ"] > 0].groupby(away_team_col).size().reset_index(name="HOZ_Count")  # Count matches where HOZ > 0
    aoz_counts_away = df[df["AOZ"] > 0].groupby(away_team_col).size().reset_index(name="AOZ_Count")  # Count matches where AOZ > 0

    # Total matches per away team
    total_counts_away = df.groupby(away_team_col).size().reset_index(name="Total")

    # --- Merge HOME Team Results ---
    print("🔄 Merging HOME team data...")
    
    # Start with total counts and preserve team names as strings
    result_home = total_counts_home.copy()
    
    # List of dataframes to merge for HOME teams
    home_dfs = [
        odd_counts_home, even_counts_home, draw_counts_home,
        g0_counts_home, g1_counts_home, g2_counts_home, g0u3_counts_home,
        hwin_counts_home, awin_counts_home, btts_counts_home,
        hoz_counts_home, aoz_counts_home
    ]
    
    # Merge all dataframes for HOME teams
    for merge_df in home_dfs:
        result_home = result_home.merge(merge_df, on=home_team_col, how="left")
    
    # Fill NaN values with 0 and convert only numeric columns to int
    numeric_cols = result_home.columns.drop(home_team_col)
    result_home[numeric_cols] = result_home[numeric_cols].fillna(0).astype(int)
    result_home = result_home.sort_values(by=home_team_col)

    # Rename home team column for clarity
    result_home = result_home.rename(columns={home_team_col: "Team"})
    result_home["Team_Type"] = "Home"

    # --- Merge AWAY Team Results ---
    print("🔄 Merging AWAY team data...")
    
    # Start with total counts and preserve team names as strings
    result_away = total_counts_away.copy()
    
    # List of dataframes to merge for AWAY teams
    away_dfs = [
        odd_counts_away, even_counts_away, draw_counts_away,
        g0_counts_away, g1_counts_away, g2_counts_away, g0u3_counts_away,
        hwin_counts_away, awin_counts_away, btts_counts_away,
        hoz_counts_away, aoz_counts_away
    ]
    
    # Merge all dataframes for AWAY teams
    for merge_df in away_dfs:
        result_away = result_away.merge(merge_df, on=away_team_col, how="left")
    
    # Fill NaN values with 0 and convert only numeric columns to int
    numeric_cols = result_away.columns.drop(away_team_col)
    result_away[numeric_cols] = result_away[numeric_cols].fillna(0).astype(int)
    result_away = result_away.sort_values(by=away_team_col)

    # Rename away team column for clarity
    result_away = result_away.rename(columns={away_team_col: "Team"})
    result_away["Team_Type"] = "Away"

    # --- Combine Home and Away Data ---
    print("🔗 Combining home and away data...")
    result_combined = pd.concat([result_home, result_away], ignore_index=True)

    # --- Calculate Averages and Percentages ---
    print("📊 Calculating percentages...")
    
    # For combined data
    result_combined["Odd_Pct"] = (result_combined["Odd"] / result_combined["Total"] * 100).round(1)
    result_combined["Even_Pct"] = (result_combined["Even"] / result_combined["Total"] * 100).round(1)
    result_combined["Draw_Pct"] = (result_combined["Draw"] / result_combined["Total"] * 100).round(1)
    result_combined["G0U3_Pct"] = (result_combined["G0U3"] / result_combined["Total"] * 100).round(1)
    
    # Calculate win percentage based on team type
    result_combined["Win_Pct"] = 0.0
    home_mask = result_combined["Team_Type"] == "Home"
    away_mask = result_combined["Team_Type"] == "Away"
    
    # Home teams use HWin (home wins), Away teams use AWin (away wins)
    result_combined.loc[home_mask, "Win_Pct"] = (result_combined.loc[home_mask, "HWin"] / result_combined.loc[home_mask, "Total"] * 100).round(1)
    result_combined.loc[away_mask, "Win_Pct"] = (result_combined.loc[away_mask, "AWin"] / result_combined.loc[away_mask, "Total"] * 100).round(1)
    
    result_combined["BTTS_Pct"] = (result_combined["BTTS"] / result_combined["Total"] * 100).round(1)
    
    # Calculate HOZ and AOZ percentages
    result_combined["HOZ_Pct"] = (result_combined["HOZ_Count"] / result_combined["Total"] * 100).round(1)
    result_combined["AOZ_Pct"] = (result_combined["AOZ_Count"] / result_combined["Total"] * 100).round(1)

    print("✅ Data processing completed!")
    print(f"🏠 Home teams analyzed: {len(result_home)}")
    print(f"✈️ Away teams analyzed: {len(result_away)}")
    print(f"📊 Total records: {len(result_combined)}")

    # Display sample of data with verification
    print("\n📋 Sample of Home Teams Data:")
    print(result_home[['Team', 'Total', 'HOZ_Count', 'AOZ_Count', 'HWin', 'AWin', 'Draw']].head())
    print("\n📋 Sample of Away Teams Data:")
    print(result_away[['Team', 'Total', 'HOZ_Count', 'AOZ_Count', 'HWin', 'AWin', 'Draw']].head())

    # Quick verification
    print("\n🔍 Data Verification:")
    print(f"Total matches where HOZ > 0: {(df['HOZ'] > 0).sum()}")
    print(f"Total matches where AOZ > 0: {(df['AOZ'] > 0).sum()}")
    print(f"Sum of home team HOZ_Count: {result_home['HOZ_Count'].sum()}")
    print(f"Sum of away team AOZ_Count: {result_away['AOZ_Count'].sum()}")
    print(f"Total home wins in dataset: {(df['HOZ'] > df['AOZ']).sum()}")
    print(f"Total away wins in dataset: {(df['AOZ'] > df['HOZ']).sum()}")
    print(f"Total draws in dataset: {(df['HOZ'] == df['AOZ']).sum()}")

    # Export to Excel
    print("💾 Exporting to Excel...")
    with pd.ExcelWriter("Team_Stats_Extended.xlsx") as writer:
        result_home.to_excel(writer, sheet_name="Home_Teams", index=False)
        result_away.to_excel(writer, sheet_name="Away_Teams", index=False)
        result_combined.to_excel(writer, sheet_name="Combined_Stats", index=False)

    # ---- Create Web Report ----
    print("🌐 Creating web report...")
    
    # Create separate HTML tables for home and away
    home_table = result_home.to_html(classes="table table-bordered table-hover table-sm home", index=False, escape=False)
    away_table = result_away.to_html(classes="table table-bordered table-hover table-sm away", index=False, escape=False)
    combined_table = result_combined.to_html(classes="table table-bordered table-hover table-sm", index=False, escape=False)

    html_report = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Team Stats Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f8f9fa; }}
            .card {{ margin: 20px auto; max-width: 98%; }}
            table {{ text-align: center; font-size: 0.9em; }}
            th {{ background-color: #007bff; color: white; }}
            .home th {{ background-color: #1976d2; }}
            .away th {{ background-color: #f57c00; }}
            .home tr:nth-child(even) {{ background-color: #e3f2fd; }}
            .away tr:nth-child(even) {{ background-color: #fff3e0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card shadow">
                <div class="card-header text-center bg-primary text-white">
                    <h2>Team Statistics Report</h2>
                    <p>Analysis based on Home and Away performances</p>
                </div>
                <div class="card-body">
                    <h4>🏠 Home Teams Performance</h4>
                    {home_table}
                    
                    <h4 class="mt-5">✈️ Away Teams Performance</h4>
                    {away_table}
                    
                    <h4 class="mt-5">📊 Combined Statistics with Percentages</h4>
                    {combined_table}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Save web report
    with open("Team_Stats_Report.html", "w", encoding="utf-8") as f:
        f.write(html_report)

    print("✅ All reports generated successfully!")
    print("📁 Files created:")
    print("   - Team_Stats_Extended.xlsx (with multiple sheets)")
    print("   - Team_Stats_Report.html")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

finally:
    # Close connection
    if 'conn' in locals():
        conn.close()
        print("🔒 Database connection closed")