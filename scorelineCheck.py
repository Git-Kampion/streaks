import pyodbc

# Path to your Access database (.accdb or .mdb)
db_path = r"C:\Users\letenok.DWA\Documents\streaks\results2026.accdb"

# Connection string (for Access using ACE OLEDB driver)
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={db_path};"
)
#insert_stmt2 = "Select * FROM portLeag25 union Select * FROM SwissChalleng25 union select * from CzechA25 union select * from Ligue1FrNat25 union select * from IsraelB25 union select * from UkraineA25  union select * from UkrainePresha25 union Select * FROM SwitzerA25 union Select * FROM Turk25 union Select * FROM Turk225 union Select * FROM SloveniaA2025 union Select * FROM skLeague125  union Select * FROM BelgiumChall25 union Select * FROM SwedenB25 union Select * FROM BrazilA25 union Select * FROM SwedenA25 union Select * FROM SloveniaB25 union Select * FROM MalaysiaPrem25 union Select * FROM Eredevisie25 union Select * FROM CroatiaB25 union Select * FROM  portLeag225 union Select * FROM  pslA2025 union Select * FROM  RomaniA25 union Select * FROM  RomaniB25 union Select * FROM  ScotlandA25  union Select * FROM  SerbiaA25 union Select * FROM  SerieA25 union Select * FROM  SerieBB25 union Select * FROM  SingPorePrem25 union Select * FROM  skleague125 union Select * FROM  SlovakiaAA25 union Select * FROM  SlovakiaB25 union select * from SerbiaB25 union select * from AzerBaijan2025"

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    query = query = """
SELECT *
FROM (
    SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM portLeag25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SwissChalleng25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM CzechA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM Ligue1FrNat25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM IsraelB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM UkraineA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM UkrainePresha25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SwitzerA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM Turk25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM Turk225
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SloveniaA2025
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM skLeague125
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM BelgiumChall25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SwedenB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM BrazilA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SwedenA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SloveniaB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM MalaysiaPrem25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM Eredevisie25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM CroatiaB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM portLeag225
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM pslA2025
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM RomaniA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM RomaniB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM ScotlandA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SerbiaA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SerieA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SerieBB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SingPorePrem25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM skleague125
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SlovakiaAA25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SlovakiaB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM SerbiaB25
    UNION ALL SELECT ID, Round, Tframe, Home, Away, hgoal, agoal, hhgoal, ahgoal FROM AzerBaijan2025
) AS AllGames
WHERE VAL(agoal) > 3
AND VAL(Round) = (
    SELECT MAX(VAL(Round))
    FROM (
        SELECT Round FROM portLeag25
        UNION ALL SELECT Round FROM SwissChalleng25
        UNION ALL SELECT Round FROM CzechA25
        UNION ALL SELECT Round FROM Ligue1FrNat25
        UNION ALL SELECT Round FROM IsraelB25
        UNION ALL SELECT Round FROM UkraineA25
        UNION ALL SELECT Round FROM UkrainePresha25
        UNION ALL SELECT Round FROM SwitzerA25
        UNION ALL SELECT Round FROM Turk25
        UNION ALL SELECT Round FROM Turk225
        UNION ALL SELECT Round FROM SloveniaA2025
        UNION ALL SELECT Round FROM skLeague125
        UNION ALL SELECT Round FROM BelgiumChall25
        UNION ALL SELECT Round FROM SwedenB25
        UNION ALL SELECT Round FROM BrazilA25
        UNION ALL SELECT Round FROM SwedenA25
        UNION ALL SELECT Round FROM SloveniaB25
        UNION ALL SELECT Round FROM MalaysiaPrem25
        UNION ALL SELECT Round FROM Eredevisie25
        UNION ALL SELECT Round FROM CroatiaB25
        UNION ALL SELECT Round FROM portLeag225
        UNION ALL SELECT Round FROM pslA2025
        UNION ALL SELECT Round FROM RomaniA25
        UNION ALL SELECT Round FROM RomaniB25
        UNION ALL SELECT Round FROM ScotlandA25
        UNION ALL SELECT Round FROM SerbiaA25
        UNION ALL SELECT Round FROM SerieA25
        UNION ALL SELECT Round FROM SerieBB25
        UNION ALL SELECT Round FROM SingPorePrem25
        UNION ALL SELECT Round FROM skleague125
        UNION ALL SELECT Round FROM SlovakiaAA25
        UNION ALL SELECT Round FROM SlovakiaB25
        UNION ALL SELECT Round FROM SerbiaB25
        UNION ALL SELECT Round FROM AzerBaijan2025
    ) AS R
);
"""


    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if 'conn' in locals():
        conn.close()
