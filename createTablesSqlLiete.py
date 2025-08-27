import pyodbc
import sqlite3

# Path to Access DB
access_db = r"C:\path\to\your\database.accdb"

# Path to SQLite DB (will be created if not exists)
sqlite_db = r"C:\path\to\football.sqlite"

# Connect to Access
access_conn = pyodbc.connect(
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + access_db + ";"
)
access_cursor = access_conn.cursor()

# Connect to SQLite
sqlite_conn = sqlite3.connect(sqlite_db)
sqlite_cursor = sqlite_conn.cursor()

# Get all tables from Access
tables = [row.table_name for row in access_cursor.tables(tableType="TABLE")]

for table in tables:
    print(f"Processing table: {table}")
    
    # Get column info
    access_cursor.execute(f"SELECT * FROM {table}")
    col_names = [column[0] for column in access_cursor.description]
    
    # Drop table in SQLite if exists
    sqlite_cursor.execute(f"DROP TABLE IF EXISTS {table}")
    
    # Create table in SQLite
    col_defs = ", ".join([f"{col} TEXT" for col in col_names])  # store all as TEXT for safety
    sqlite_cursor.execute(f"CREATE TABLE {table} ({col_defs})")
    
    # Insert rows
    rows = access_cursor.fetchall()
    placeholders = ", ".join("?" * len(col_names))
    sqlite_cursor.executemany(
        f"INSERT INTO {table} VALUES ({placeholders})",
        [tuple(map(str, row)) for row in rows]
    )
    sqlite_conn.commit()

print("✅ Migration complete!")

# Close connections
access_conn.close()
sqlite_conn.close()
