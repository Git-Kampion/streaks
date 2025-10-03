import pyodbc
import json

# Path to Access DB
db_path = r'C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb'
fixtures = []
# Connect to Access DB
conn = pyodbc.connect(
    rf'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};'
)
cursor = conn.cursor()

# Read from table
query = "Select Round, Tframe, Home, Away From Portugal25 union SELECT Round, Tframe, Home, Away FROM EPL25 union SELECT Round, Tframe, Home, Away FROM EPLChampion25  union SELECT Round, Tframe, Home, Away FROM USA25 union SELECT Round, Tframe, Home, Away FROM LigueNat25 union SELECT Round, Tframe, Home, Away FROM IrelandB25  union SELECT Round, Tframe, Home, Away FROM BrazilA25 union SELECT Round, Tframe, Home, Away FROM IcelandBesta25 union SELECT Round, Tframe, Home, Away FROM ArgentiNacional25 union SELECT Round, Tframe, Home, Away FROM ArgentitTorneo25 union SELECT Round, Tframe, Home, Away FROM ArgentiNacional25 union SELECT Round, Tframe, Home, Away FROM belgiumChall25 union SELECT Round, Tframe, Home, Away FROM CroatiaB25 union SELECT Round, Tframe, Home, Away FROM Eredevisie25 union Select Round, Tframe, Home, Away From PortugalB25 union Select Round, Tframe, Home, Away From PSLA25 union Select Round, Tframe, Home, Away From RomaniA25 union Select Round, Tframe, Home, Away From RomaniB25 union Select Round, Tframe, Home, Away From ScotlandA25 union Select Round, Tframe, Home, Away From ScotlandB25 union Select Round, Tframe, Home, Away From SerbiaA25 union Select Round, Tframe, Home, Away From SerbiaB25 union Select Round, Tframe, Home, Away From SerieA25 union Select Round, Tframe, Home, Away From SerieBB25 union Select Round, Tframe, Home, Away From SingPrem25 union Select Round, Tframe, Home, Away From skLeague125 union Select Round, Tframe, Home, Away From SlovakiaA25 union Select Round, Tframe, Home, Away From SlovakiaB25  union Select Round, Tframe, Home, Away From SloveniaA25 union Select Round, Tframe, Home, Away From SloveniaB25 union Select Round, Tframe, Home, Away From SwedenA25 union Select Round, Tframe, Home, Away From SwedenB25 union Select Round, Tframe, Home, Away From SwissA25 union Select Round, Tframe, Home, Away From SwissChalleng25 union Select Round, Tframe, Home, Away From Turk225 union Select Round, Tframe, Home, Away From Turk25 union Select Round, Tframe, Home, Away From UkraineA25 union Select Round, Tframe, Home, Away From UkrainePresha25"

cursor.execute(query)

# Convert to JSON-friendly structure

for bow in cursor.fetchall():
    date_time = bow.Tframe
   
    fixtures.append({
        "round": bow.Round,
        "date": str(date_time),
        "home": bow.Home,
        "away": bow.Away
    })
# Save as JSON file
with open("fixturesAnlytics.json", "w", encoding="utf-8") as f:
    json.dump(fixtures, f, indent=2)

conn.close()
