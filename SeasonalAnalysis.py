import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb


#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
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

aFullTimeOvers= ([],[],[])
aFullTimeOvers2= ([],[],[])
aFullTimeOvers3= ([],[],[])
aFullTimeOvers4= ([],[],[])
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


AwayOver0 = ([],[],[])
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
              
        #aBTS = BtOr.Bts(t,rfdA,"a",6)
        #AwOvers = BtOr.OverUnderSeaon(t,rfdA,"a",6)
        afullTimeOver = BtOr.FixOverUnders(t,rfdA,"a",6)
        #afullTimeOvers = BtOr.FixOverUnders(t,rfd,"k",5)
        #Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
      
        """"
        if len(rfdA) - aBTS[0] <= 1:
          ABTSovers[0].append(aBTS[0])
          ABTSovers[1].append(len(rfdA))
          ABTSovers[2].append(t)
          
        if len(rfdA) - AwOvers[0] <= 1:
          AwayOver0[0].append(AwOvers[0])
          AwayOver0[1].append(len(rfdA))
          AwayOver0[2].append(t)
"""
        if len(rfdA) - afullTimeOver[0][1] <= 1:
          aFullTimeOvers[0].append(afullTimeOver[0][1])
          aFullTimeOvers[1].append(len(rfdA))
          aFullTimeOvers[2].append(t)

        if len(rfdA) - afullTimeOver[0][2] <= 1:
          aFullTimeOvers2[0].append(afullTimeOver[0][2])
          aFullTimeOvers2[1].append(len(rfdA))
          aFullTimeOvers2[2].append(t)

          

        if len(rfdA) - afullTimeOver[0][3] <= 1:
          aFullTimeOvers3[0].append(afullTimeOver[0][3])
          aFullTimeOvers3[1].append(len(rfdA))
          aFullTimeOvers3[2].append(t)

        if len(rfdA) - afullTimeOver[0][4] <= 1:
          aFullTimeOvers4[0].append(afullTimeOver[0][4])
          aFullTimeOvers4[1].append(len(rfdA))
          aFullTimeOvers4[2].append(t)
            
    

df2 = pd.DataFrame(list(zip(aFullTimeOvers[1],aFullTimeOvers[0])),aFullTimeOvers[2],columns =['AwayGamesPlayed','AwayFullTimeOver1'])
df3 = pd.DataFrame(list(zip(aFullTimeOvers2[1],aFullTimeOvers2[0])),aFullTimeOvers2[2],columns =['AwayGamesPlayed','AwayFullTimeOver2'])
df4 = pd.DataFrame(list(zip(aFullTimeOvers3[1],aFullTimeOvers3[0])),aFullTimeOvers3[2],columns =['AwayGamesPlayed','AwayFullTimeOver3'])
df5 = pd.DataFrame(list(zip(aFullTimeOvers4[1],aFullTimeOvers4[0])),aFullTimeOvers4[2],columns =['AwayGamesPlayed','AwayFullTimeOver4'])
df6 = pd.DataFrame(list(zip(AwayOver0[1],AwayOver0[0])),AwayOver0[2],columns =['AwayGamesPlayed','AwayScoredWholeSeason1'])


with pd.ExcelWriter('streaks.xlsx') as writer:
  
  #df1.to_excel(writer, sheet_name='AwayBTS')
  
  df2.to_excel(writer, sheet_name='AwayFullTimeOver1')
  df3.to_excel(writer, sheet_name='AwayFullTimeOver2')
  df4.to_excel(writer, sheet_name='AwayFullTimeOver3')
  df5.to_excel(writer, sheet_name='AwayFullTimeOver4')
  df6.to_excel(writer, sheet_name='AwayScoredWholeSeason1')


#def Rallover1():
  
  
  #df20.to_excel(writer, sheet_name='Home1stHalfBelow3Goal')
  