import pandas as pd
import json

# Read the Excel file
file_path = 'Streakshominfo.xlsx'
sheet_name = 'Home'  # Assuming the sheet name is 'Home'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Extract the first three columns (Team, GamesPlayed, HomeOver1,HomeOver1,HomeOver2,,HomeOver3)
df_subset = df.iloc[:, :40]


# Convert to JSON
json_data = df_subset.to_json(orient='records', indent=4)

# Save JSON to a file
output_file = 'home_stats.json'
with open(output_file, 'w') as f:
    f.write(json_data)

print(f"JSON file saved as {output_file}")