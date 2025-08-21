import json
from collections import defaultdict
import pandas as pd

# Load the JSON data
with open('fixturesAnlytics.json', 'r') as f:
    fixtures = json.load(f)

# Create a dictionary to count fixtures by timeframe
timeframe_counts = defaultdict(int)

for fixture in fixtures:
    timeframe = fixture['date']
    timeframe_counts[timeframe] += 1

# Convert to DataFrame
df = pd.DataFrame(
    [{"date": timeframe, "count": count} 
     for timeframe, count in sorted(timeframe_counts.items())]
)

# Export to Excel
df.to_excel("fixtures_counts.xlsx", index=False)

print("Exported to fixtures_counts.xlsx")
