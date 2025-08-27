import sqlite3

# Path to your SQLite DB
conn = sqlite3.connect(r"C:\Users\letenok.DWA\Documents\streaks\football.sqlite")
cursor = conn.cursor()

# List of table names
tables = [
    "ScotlandB25","IsraelB25","PeruA25","SaudiPrem25","Laliga225","Laliga25","UkraineA25","UkrainePresha25","QaterPrem25",
    "CzechA25","MyanmarNatLeag25","SerieBB25","SingPorePrem25","skleague125","SlovakiaAA25","SlovakiaB25","SerbiaB25","pslA2025",
    "RomaniA25","RomaniB25","ScotlandA25","SerbiaA25","SerieA25","SwedenA25","SloveniaB25","MalaysiaPrem25","Eredevisie25","CroatiaB25",
    "portLeag225","Turk25","Turk225","SloveniaA2025","BelgiumChall25","SwedenB25","BrazilA25","portLeag25","SwissChalleng25","SwitzerA25",
    "AlgeriaA25","Austria125","Austria225","AzerBaijan2025","belgiumJpl25","BoliviaPrem25","BulgariaPrem25","Bundas2Liga25","BundasLiga25",
    "Bundes325","ColombiaPrem25","CroatiaA25","CSuper25","CzechB25","CyprusA25","DenmarkA25","DenmarkB25","EersteEredevisie25","EgyptA25",
    "EngLeagua225","EngLeagua125","Epl25","EplChampionShip25","EredevisieTwede25","EstoniaPremB25","EstoniaPrem25","GEORGIAA25","GreeceA25",
    "icelandBesta25","icelandDiv125","IndonesiaPrem25","IranPrem25","irelandPrem25","irelandB25","IsraelA25","israelB25","JapanA25","JapanB25",
    "JordanPrem25","LaLiga225","LaLiga25","LatviaPrem25","Ligue1Fr25","Ligue2Fr25","Ligue1FrNat25","MalaysiaPrem25","NorwayA25","NorwayB25",
    "PolandA25","PolandB25"
]

# Loop to create each table
for name in tables:
    sql = f"""
    CREATE TABLE IF NOT EXISTS "{name}" (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Round TEXT,
        Tframe TEXT,
        home TEXT,
        away TEXT,
        hgoal TEXT,
        agoal TEXT,
        hhgoal TEXT,
        ahgoal TEXT
    )
    """
    cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
