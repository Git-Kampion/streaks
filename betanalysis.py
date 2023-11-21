import pyodbc
from BetTypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb


#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from EPL UNION select * from LaLiga union select * from BundasLiga1Germ union select * from Bundes2 union select * from Denmark union select * from EplChampionShip23 union select * from Eredevisie union select * from Ligue1Fr union select * from Psl union select * from SerieA union select * from ukraine"
data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2


teams = []
numOfGames = []

round = []
Conceededround = []
BothHalvesround = []
HomeConBothHalvesround = []
HHOver0 = []
HHOver1 = []
HHOver2 = []
HHOver3 = []
HHOver4 = []
HHOver5 = []
HHOver6 = []


HHunder0 = ([],[],[])
HHunder1 = ([],[],[])
HHunder2 = []
HHunder3 = []
HHunder4 = []
HHunder5 = []
HHunder6 = []


HomeOver0 = ([],[],[])
HomeSrBh = ([],[],[])
HomeNotSrBh = ([],[],[])
Home1stG = ([],[],[])
Home1stb2G = ([],[],[])
Home1st2G = ([],[],[])
Home1stNG = ([],[],[])
Home2ndG = ([],[],[])


Home2ndNG = ([],[],[])
Home1st3G = ([],[],[])
Home1stb3G = ([],[],[])
HomeOver1 = ([],[],[])
HomeOver2 = ([],[],[])
HomeCon1 = ([],[],[])
HomeCon2 = ([],[],[])
HomeCon3 = ([],[],[])
HomeCon4 = ([],[],[])
HomeCon5 = ([],[],[])

UnderOver0 = ([],[],[])
UnderOver1 = ([],[],[])
UnderOver2 = ([],[],[])
UnderOver3 = ([],[],[])
UnderOver4 = ([],[],[])
UnderOver5 = ([],[],[])
UnderOver6 = []

AwayOver0 = []
AwayOver1 = []
AwayOver2 = []
AwayOver3 = []
AwayOver4 = []
AwayOver5 = []
AwayOver6 = []

AwayUnder0 = []
AwayUnder1 = []
AwayUnder2 = []
AwayUnder3 = []
AwayUnder4 = []
AwayUnder5 = []
AwayUnder6 = []
team = []
for ee in sql_data[0]:
   if ee[3] in teams:
    t = ee[3]
   else:
    teams.append(ee[3])


for w in teams:
    t = w
    occurence = 0
    if t in team:
      occurence = 0
    else:
     # if t == "Brighton":
        rfd = BtOr.refindedDatam(t,sql_data,3)
     
        Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
      
        if len(rfd) == Overs[0][0]:
          HomeOver0[0].append(Overs[0][0])
          HomeOver0[1].append(len(rfd))
          HomeOver0[2].append(t)
                

df1 = pd.DataFrame(list(zip(HomeOver0[1],HomeOver0[0])),HomeOver0[2],columns =['HomeGamesPlayed','HomeOver0'])
#df2 = pd.DataFrame(list(zip(Overs[1],Overs[0])),Overs[2],columns =['HomeGamesPlayed','HomeOver1'])


with pd.ExcelWriter('streaks\streaks.xlsx') as writer:
  
  df1.to_excel(writer, sheet_name='HomeOver0')
  #df20.to_excel(writer, sheet_name='Home1stHalfBelow3Goal')
  