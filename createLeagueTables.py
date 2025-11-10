import sqlite3

# Path to your SQLite DB
conn = sqlite3.connect(r"C:\Users\letenok.DWA\Documents\streaks\football.sqlite")
cursor = conn.cursor()

# List of table names
tables = [
    "VLeague1","Singapore2","Greece2","Macedonia1","Kenya1","Tunisia2","Tunisia1"
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
