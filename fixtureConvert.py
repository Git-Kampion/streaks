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
query = "SELECT Round, Tframe, Home, Away FROM AlgeriaA25   union SELECT Round, Tframe, Home, Away FROM Austria125   union SELECT Round, Tframe, Home, Away FROM Austria225 union SELECT Round, Tframe, Home, Away FROM AzerBaijan25 union SELECT Round, Tframe, Home, Away FROM belgiumJpl25 union SELECT Round, Tframe, Home, Away FROM BoliviaA25 union SELECT Round, Tframe, Home, Away FROM BulgariaPrem25 union SELECT Round, Tframe, Home, Away FROM Bundas2Liga25 union SELECT Round, Tframe, Home, Away FROM BundasLiga25 union SELECT Round, Tframe, Home, Away FROM Bundes325 union SELECT Round, Tframe, Home, Away FROM ColombiaPrem25 union SELECT Round, Tframe, Home, Away FROM CroatiaA25 union SELECT Round, Tframe, Home, Away FROM CSuper25 union SELECT Round, Tframe, Home, Away FROM  CzechB25 union SELECT Round, Tframe, Home, Away FROM CyprusA25 union SELECT Round, Tframe, Home, Away FROM CzechA25 UNION Select Round, Tframe, Home, Away FROM DenmarkA25 UNION Select Round, Tframe, Home, Away FROM DenmarkB25 UNION Select Round, Tframe, Home, Away FROM Eersterdevisie25 UNION Select Round, Tframe, Home, Away FROM EgyptA25 UNION Select Round, Tframe, Home, Away FROM EngLeagua225 UNION Select Round, Tframe, Home, Away FROM EngLeague125 UNION Select Round, Tframe, Home, Away FROM Epl25 UNION Select Round, Tframe, Home, Away FROM EplChampion25 UNION Select Round, Tframe, Home, Away FROM EredevisieTweede25 UNION Select Round, Tframe, Home, Away FROM EstoniaB25 UNION Select Round, Tframe, Home, Away FROM EstoniaPrem25 UNION Select Round, Tframe, Home, Away FROM GeorgiaA25 UNION Select Round, Tframe, Home, Away FROM GreeceA25 UNION Select Round, Tframe, Home, Away FROM icelandBesta25 UNION Select Round, Tframe, Home, Away FROM icelandBDiv125 UNION Select Round, Tframe, Home, Away FROM IndonesiaA5 UNION Select Round, Tframe, Home, Away FROM IranPrem25 UNION Select Round, Tframe, Home, Away FROM irelandPrem25 UNION Select Round, Tframe, Home, Away FROM israelA25 UNION Select Round, Tframe, Home, Away FROM irelandB25 UNION Select Round, Tframe, Home, Away FROM israelB25 UNION Select Round, Tframe, Home, Away FROM JapanA25 UNION Select Round, Tframe, Home, Away FROM JapanB25 UNION Select Round, Tframe, Home, Away FROM JordanPrem25 UNION Select Round, Tframe, Home, Away FROM  LaLiga225 UNION Select Round, Tframe, Home, Away FROM LaLiga25 UNION Select Round, Tframe, Home, Away FROM laltvia25 UNION Select Round, Tframe, Home, Away FROM Ligue1Fr25 UNION Select Round, Tframe, Home, Away FROM Ligue2Fr25  UNION Select Round, Tframe, Home, Away FROM MalaysiaPrem25 UNION Select Round, Tframe, Home, Away From NorwayA25 UNION Select Round, Tframe, Home, Away From NorwayB25 UNION Select Round, Tframe, Home, Away From PolandA25 UNION Select Round, Tframe, Home, Away From PolandB25 "

cursor.execute(query)

# Convert to JSON-friendly structure

for row in cursor.fetchall():
    date_time = row.Tframe
    date_part = date_time.split("-")[:3]
    result = "-".join(date_part)
    fixtures.append({
        "round": row.Round,
        "date": str(result),
        "home": row.Home,
        "away": row.Away
    })
# Break Access limit

# Read from table
query = "Select Round, Tframe, Home, Away From Portugal25 union SELECT Round, Tframe, Home, Away FROM EPL25 union SELECT Round, Tframe, Home, Away FROM EPLChampion25  union SELECT Round, Tframe, Home, Away FROM USA25 union SELECT Round, Tframe, Home, Away FROM LigueNat25 union SELECT Round, Tframe, Home, Away FROM IrelandB25  union SELECT Round, Tframe, Home, Away FROM BrazilA25 union SELECT Round, Tframe, Home, Away FROM IcelandBesta25 union SELECT Round, Tframe, Home, Away FROM ArgentiNacional25 union SELECT Round, Tframe, Home, Away FROM ArgentitTorneo25 union SELECT Round, Tframe, Home, Away FROM ArgentiNacional25 union SELECT Round, Tframe, Home, Away FROM belgiumChall25 union SELECT Round, Tframe, Home, Away FROM CroatiaB25 union SELECT Round, Tframe, Home, Away FROM Eredevisie25 union Select Round, Tframe, Home, Away From PortugalB25 union Select Round, Tframe, Home, Away From PSLA25 union Select Round, Tframe, Home, Away From RomaniA25 union Select Round, Tframe, Home, Away From RomaniB25 union Select Round, Tframe, Home, Away From ScotlandA25 union Select Round, Tframe, Home, Away From ScotlandB25 union Select Round, Tframe, Home, Away From SerbiaA25 union Select Round, Tframe, Home, Away From SerbiaB25 union Select Round, Tframe, Home, Away From SerieA25 union Select Round, Tframe, Home, Away From SerieBB25 union Select Round, Tframe, Home, Away From SingPrem25 union Select Round, Tframe, Home, Away From skLeague125 union Select Round, Tframe, Home, Away From SlovakiaA25 union Select Round, Tframe, Home, Away From SlovakiaB25  union Select Round, Tframe, Home, Away From SloveniaA25 union Select Round, Tframe, Home, Away From SloveniaB25 union Select Round, Tframe, Home, Away From SwedenA25 union Select Round, Tframe, Home, Away From SwedenB25 union Select Round, Tframe, Home, Away From SwissA25 union Select Round, Tframe, Home, Away From SwissChalleng25 union Select Round, Tframe, Home, Away From Turk225 union Select Round, Tframe, Home, Away From Turk25 union Select Round, Tframe, Home, Away From UkraineA25 union Select Round, Tframe, Home, Away From UkrainePresha25"

cursor.execute(query)

# Convert to JSON-friendly structure

for bow in cursor.fetchall():
    date_time = bow.Tframe
    date_part = date_time.split("-")[:3]
    result = "-".join(date_part)
    fixtures.append({
        "round": bow.Round,
        "date": str(result),
        "home": bow.Home,
        "away": bow.Away
    })
# Save as JSON file
with open("fixtures.json", "w", encoding="utf-8") as f:
    json.dump(fixtures, f, indent=2)

conn.close()
