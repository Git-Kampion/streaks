


import sqlite3, json
conn = sqlite3.connect('football.sqlite')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [r[0] for r in cur.fetchall()]
all_tables = {}
for t in tables:
    cur.execute(f"SELECT * FROM '{t}';")
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    all_tables[t] = {
    'columns': cols,
    'rows': rows
    }
with open('tables.json','w', encoding='utf-8') as f:
    json.dump(all_tables, f, ensure_ascii=False)
print('Wrote tables.json with', len(all_tables), 'tables')

