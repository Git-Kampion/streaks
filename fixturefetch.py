import pandas as pd
import json

# Read the Excel file
file_path = 'Streakshominfo.xlsx'
sheet_name = 'Home'  # Assuming the sheet name is 'Home'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Extract the first three columns (Team, GamesPlayed, HomeOver1,HomeOver1,HomeOver2,,HomeOver3)
df_subset = df.iloc[:, :40]


# Second DataFrame (second Excel file)
df2 = pd.read_excel("Streakshominfo2.xlsx")
df2_subset = df2.iloc[:, :40]  # match the same first 40 columns

# Append (stack) them together
df_combined = pd.concat([df_subset, df2_subset], ignore_index=True)
# Convert to JSON
json_data = df_combined.to_json(orient='records', indent=4)

# Save JSON to a file
output_file = 'home_stats.json'
with open(output_file, 'w') as f:
    f.write(json_data)

print(f"JSON file saved as {output_file}")