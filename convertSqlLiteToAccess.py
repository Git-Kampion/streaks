import sqlite3
import pyodbc
import pandas as pd

def sqlite_to_access(sqlite_db_path, access_db_path):
    """
    Convert SQLite database to Access database
    """
    try:
        # Connect to SQLite
        sqlite_conn = sqlite3.connect(sqlite_db_path)
        sqlite_cursor = sqlite_conn.cursor()
        
        # Connect to Access
        access_conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={access_db_path};'
        )
        access_conn = pyodbc.connect(access_conn_str)
        access_cursor = access_conn.cursor()
        
        # Get all table names from SQLite
        sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in sqlite_cursor.fetchall()]
        
        print(f"Found {len(tables)} tables: {tables}")
        
        for table in tables:
            print(f"Processing table: {table}")
            
            # Get data from SQLite
            sqlite_cursor.execute(f"SELECT * FROM {table}")
            rows = sqlite_cursor.fetchall()
            
            # Get column names and types
            sqlite_cursor.execute(f"PRAGMA table_info({table})")
            columns_info = sqlite_cursor.fetchall()
            columns = [col[1] for col in columns_info]
            
            if not rows:
                print(f"  No data in table {table}, skipping...")
                continue
            
            # Create table in Access (simplified - you might need to adjust data types)
            try:
                # Drop table if exists
                access_cursor.execute(f"DROP TABLE {table}")
            except:
                pass  # Table doesn't exist
            
            # Create table with columns (using TEXT for simplicity)
            create_table_sql = f"CREATE TABLE {table} ("
            create_table_sql += ", ".join([f"{col} TEXT" for col in columns])
            create_table_sql += ")"
            access_cursor.execute(create_table_sql)
            
            # Insert data
            placeholders = ", ".join(["?" for _ in columns])
            insert_sql = f"INSERT INTO {table} VALUES ({placeholders})"
            
            for row in rows:
                access_cursor.execute(insert_sql, row)
            
            print(f"  Transferred {len(rows)} rows")
        
        # Commit changes
        access_conn.commit()
        print("Conversion completed successfully!")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        raise
    finally:
        # Close connections
        if 'sqlite_conn' in locals():
            sqlite_conn.close()
        if 'access_conn' in locals():
            access_conn.close()

# Usage
sqlite_to_access('C:\\Users\\letenok.DWA\\Documents\\streaks\\football.sqlite', 'C:\\Users\\letenok.DWA\\Documents\\streaks\\results2026.accdb')