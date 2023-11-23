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
Ateams = []
numOfGames = []

round = []
Conceededround = []
BothHalvesround = []
BTSovers= ([],[],[])
ABTSovers= ([],[],[])
FullTimeOvers= ([],[],[])
aFullTimeOvers= ([],[],[])
HomeConBothHalvesround = []
HHOver0 = ([],[],[])
HHOver1 = ([],[],[])
HHOver2 = ([],[],[])
HHOver3 = ([],[],[])
HHOver4 = ([],[],[])
HHOver5 = ([],[],[])
HHOver6 = ([],[],[])

HSHOver0 = ([],[],[])
HSHOver1 = ([],[],[])
HSHOver2 = ([],[],[])
HSHOver3 = ([],[],[])
HSHOver4 = ([],[],[])
HSHOver5 = ([],[],[])
HSHOver6 = ([],[],[])


HHunder0 = ([],[],[])
HHunder1 = ([],[],[])
HHunder2 = ([],[],[])

HSHunder0 = ([],[],[])
HSHunder1 = ([],[],[])
HSHunder2 = ([],[],[])
HSHunder3 = ([],[],[])
HSHunder4 = ([],[],[])
HSHunder5 = ([],[],[])
HSHunder3 = ([],[],[])
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
HomeOver3 = ([],[],[])
HomeOver4 = ([],[],[])
HomeOver5 = ([],[],[])

HomeCon0 = ([],[],[])
HomeCon1 = ([],[],[])
HomeCon2 = ([],[],[])
HomeCon3 = ([],[],[])
HomeCon4 = ([],[],[])
HomeCon5 = ([],[],[])

HomeFirstHCon0 = ([],[],[])
HomeFirstHCon1 = ([],[],[])
HomeFirstHCon2 = ([],[],[])
HomeFirstHCon3 = ([],[],[])
HomeFirstHCon4 = ([],[],[])
HomeFirstHCon5 = ([],[],[])

HomeConB0 = ([],[],[])
HomeConB1 = ([],[],[])
HomeConB2 = ([],[],[])
HomeConB3 = ([],[],[])
HomeConB4 = ([],[],[])
HomeConB5 = ([],[],[])

Under0 = ([],[],[])
Under1 = ([],[],[])
Under2 = ([],[],[])
Under3 = ([],[],[])
Under4 = ([],[],[])
Under5 = ([],[],[])


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
Ateam = []


for bb in sql_data[0]:
   if bb[4] in Ateams:
    t = bb[4]
   else:
    Ateams.append(bb[4])

for ee in sql_data[0]:
   if ee[3] in teams:
    t = ee[3]
   else:
    teams.append(ee[3])

for w in Ateams:
    t = w
    occurence = 0
    if t in Ateam:
      occurence = 0
    else:
     # if t == "Brighton":
        
        rfdA = BtOr.refindedDatam(t,sql_data,4)
              
        aBTS = BtOr.Bts(t,rfdA,"a",6)
        afullTimeOver = BtOr.FixOverUnders(t,rfdA,"a",6)
        #afullTimeOvers = BtOr.FixOverUnders(t,rfd,"k",5)
        #Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
      

        if len(rfdA) - aBTS[0] <= 1:
          ABTSovers[0].append(aBTS[0])
          ABTSovers[1].append(len(rfdA))
          ABTSovers[2].append(t)

        if len(rfdA) - afullTimeOver[0][2] <= 1:
          aFullTimeOvers[0].append(afullTimeOver[0][2])
          aFullTimeOvers[1].append(len(rfdA))
          aFullTimeOvers[2].append(t)

for w in teams:
    t = w
    occurence = 0
    if t in team:
      occurence = 0
    else:
     # if t == "Brighton":
        rfd = BtOr.refindedDatam(t,sql_data,3)
       
       
        hBTS = BtOr.Bts(t,rfd,"k",5)
        
        fullTimeOver = BtOr.FixOverUnders(t,rfd,"k",5)
        #afullTimeOvers = BtOr.FixOverUnders(t,rfd,"k",5)
        #Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
      

        if len(rfd) - hBTS[0] <= 1:
          BTSovers[0].append(hBTS[0])
          BTSovers[1].append(len(rfd))
          BTSovers[2].append(t)

        if len(rfd) - fullTimeOver[0][2] <= 1:
          FullTimeOvers[0].append(fullTimeOver[0][2])
          FullTimeOvers[1].append(len(rfd))
          FullTimeOvers[2].append(t)

          

df1 = pd.DataFrame(list(zip(BTSovers[1],BTSovers[0])),BTSovers[2],columns =['HomeGamesPlayed','HomeBTS'])
df2 = pd.DataFrame(list(zip(ABTSovers[1],ABTSovers[0])),ABTSovers[2],columns =['HomeGamesPlayed','AwayBTS'])

df3 = pd.DataFrame(list(zip(aFullTimeOvers[1],aFullTimeOvers[0])),aFullTimeOvers[2],columns =['HomeGamesPlayed','AwayFullTimeOver1'])
df4 = pd.DataFrame(list(zip(FullTimeOvers[1],FullTimeOvers[0])),FullTimeOvers[2],columns =['HomeGamesPlayed','HomeFullTimeOver1'])
       
                


#df14 = pd.DataFrame(list(zip(HomeConB1[1],HomeConB1[0])),HomeConB1[2],columns =['HomeGamesPlayed','HomeConceeded1'])


with pd.ExcelWriter('streaks\streaks.xlsx') as writer:
  
  df1.to_excel(writer, sheet_name='HomeBTS')
  df2.to_excel(writer, sheet_name='AwayBTS')

  df3.to_excel(writer, sheet_name='AwayFullTimeOver1')
  df4.to_excel(writer, sheet_name='HomeFullTimeOver1')
  #df20.to_excel(writer, sheet_name='Home1stHalfBelow3Goal')
  