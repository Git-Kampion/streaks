import pyodbc

# Connect to Access DB
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\2026.accdb')
cursor = conn.cursor()

# List of table names

tables =  ["SerieBB25","SingPorePrem25","skleague125","SlovakiaAA25","SlovakiaB25","SerbiaB25","pslA2025","RomaniA25","RomaniB25","ScotlandA25","SerbiaA25","SerieA25","SwedenA25","SloveniaB25","MalaysiaPrem25","Eredevisie25","CroatiaB25","portLeag225","Turk25","Turk225","SloveniaA2025","BelgiumChall25","SwedenB25","BrazilA25","portLeag25","SwissChalleng25","SwitzerA25","AlgeriaA25","Austria125","Austria225","AzerBaijan2025","belgiumJpl25","BoliviaPrem25","BulgariaPrem25","Bundas2Liga25","BundasLiga25","Bundes325","ColombiaPrem25","CroatiaA25","CSuper25","CzechB25","CyprusA25","DenmarkA25","DenmarkB25","EersteEredevisie25","EgyptA25","EngLeagua225","EngLeagua125","Epl25","EplChampionShip25","EredevisieTwede25","EstoniaPremB25","EstoniaPrem25","GEORGIAA25","GreeceA25","icelandBesta25","icelandDiv125","IndonesiaPrem25","IranPrem25","irelandPrem25","irelandB25","IsraelA25","israelB25","JapanA25","JapanB25","JordanPrem25","LaLiga225","LaLiga25","LatviaPrem25","Ligue1Fr25","Ligue2Fr25","MalaysiaPrem25","NorwayA25","NorwayB25","PolandA25","PolandB25"]



# Loop to create each table
for name in tables:
    sql = f"""
    CREATE TABLE [{name}] (
        ID AUTOINCREMENT PRIMARY KEY,
        Round TEXT(50),
        Tframe DATETIME,
        home TEXT(50),
        away TEXT(50),
        hgoal TEXT(50),
        agoal TEXT(50),
        hhgoal TEXT(50),
        ahgoal TEXT(50)
    )
  """
    cursor.execute(sql)
    conn.commit()

cursor.close()
conn.close()
