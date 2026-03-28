import pyodbc

source = r"C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb"
target = r"C:\Users\letenok.DWA\Documents\streaks\Fixtures26.accdb"

conn_src = pyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={source};"
)
conn_tgt = pyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={target};"
)

cursor_src = conn_src.cursor()
cursor_tgt = conn_tgt.cursor()

# Enumerate user tables only
tables = [r.table_name for r in cursor_src.tables(tableType='TABLE')]

for tbl in tables:
    print(f"Cloning schema for table: {tbl}")

    col_defs = []
    for col in cursor_src.columns(table=tbl):
        name = col.column_name
        dtype = col.type_name.upper()
        length = col.column_size

        # Basic type mapping for Access
        if dtype in ("VARCHAR", "TEXT", "CHAR"):
            ddl = f"TEXT({length})" if length and length > 0 else "LONGTEXT"
        elif dtype in ("LONGCHAR", "MEMO"):
            ddl = "LONGTEXT"
        elif dtype in ("COUNTER",):
            ddl = "AUTOINCREMENT"
        elif dtype in ("INTEGER", "INT", "LONG"):
            ddl = "INTEGER"
        elif dtype in ("BYTE",):
            ddl = "BYTE"
        elif dtype in ("DOUBLE", "FLOAT", "REAL", "SINGLE"):
            ddl = "DOUBLE"
        elif dtype in ("DECIMAL", "NUMERIC"):
            ddl = f"DECIMAL({length}, 2)" if length else "DECIMAL"
        elif dtype in ("DATETIME", "DATE", "TIME"):
            ddl = "DATETIME"
        elif dtype in ("YESNO", "BIT", "BOOLEAN"):
            ddl = "YESNO"
        else:
            ddl = dtype  # fallback (unlikely in your scenario)

        col_defs.append(f"[{name}] {ddl}")

    ddl = f"CREATE TABLE [{tbl}] (\n    " + ",\n    ".join(col_defs) + "\n);"
    print(ddl)

    cursor_tgt.execute(ddl)
    conn_tgt.commit()

conn_src.close()
conn_tgt.close()

print("Schema cloned successfully (no data).")
