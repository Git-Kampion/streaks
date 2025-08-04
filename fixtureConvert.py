import pyodbc
import json

# Path to Access DB
db_path = r'C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb'

# Connect to Access DB
conn = pyodbc.connect(
    rf'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};'
)
cursor = conn.cursor()

# Read from table
query = "SELECT Round, Tframe, Home, Away FROM Austria125 UNION SELECT Round, Tframe, Home, Away FROM belgiumJpl25 UNION SELECT Round, Tframe, Home, Away FROM BrazilA25 UNION SELECT Round, Tframe, Home, Away FROM BulgariaPrem25 UNION SELECT Round, Tframe, Home, Away FROM Bundas2Liga25 UNION SELECT Round, Tframe, Home, Away FROM Bundes325 UNION SELECT Round, Tframe, Home, Away FROM CroatiaA25 UNION SELECT Round, Tframe, Home, Away FROM CSuper25 UNION SELECT Round, Tframe, Home, Away FROM CzechA25 UNION SELECT Round, Tframe, Home, Away FROM CzechB25 UNION SELECT Round, Tframe, Home, Away FROM DenmarkA25 UNION SELECT Round, Tframe, Home, Away FROM DenmarkB25 UNION SELECT Round, Tframe, Home, Away FROM EngLeagua225 UNION SELECT Round, Tframe, Home, Away FROM EngLeague125 UNION SELECT Round, Tframe, Home, Away FROM EstoniaPrem25 UNION SELECT Round, Tframe, Home, Away FROM IrelandA25  UNION SELECT Round, Tframe, Home, Away FROM irelandPrem25 UNION SELECT Round, Tframe, Home, Away FROM JordanPrem25 UNION SELECT Round, Tframe, Home, Away FROM PolandA25 UNION SELECT Round, Tframe, Home, Away FROM PolandB25 UNION SELECT Round, Tframe, Home, Away FROM RomaniA25 UNION SELECT Round, Tframe, Home, Away FROM ScotlandB25 UNION SELECT Round, Tframe, Home, Away FROM SlovakiaB25 UNION SELECT Round, Tframe, Home, Away FROM Slovenia225 UNION SELECT Round, Tframe, Home, Away FROM SwedenA25 UNION SELECT Round, Tframe, Home, Away FROM SwissChalleng25 UNION SELECT Round, Tframe, Home, Away FROM UkraineA25 UNION SELECT Round, Tframe, Home, Away FROM UkrainePresha25"

cursor.execute(query)

# Convert to JSON-friendly structure
fixtures = []
for row in cursor.fetchall():
    fixtures.append({
        "round": row.Round,
        "date": str(row.Tframe),
        "home": row.Home,
        "away": row.Away
    })

# Save as JSON file
with open("fixtures.json", "w", encoding="utf-8") as f:
    json.dump(fixtures, f, indent=2)

conn.close()
