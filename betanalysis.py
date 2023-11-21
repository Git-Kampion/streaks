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
Home1stNG = ([],[],[])
Home2ndG = ([],[],[])


Home2ndNG = ([],[],[])

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
        hmeScorsBt = BtOr.ScoredBothHalvesSeaon(t,rfd,"k",5)
        HomeScrd1st = BtOr.ScoredWholeSeaon(t,rfd,"k",7)
        HomeScrd2nd = BtOr.ndScoredWholeSeaon(t,rfd,"k",5)
        Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
       
        if len(rfd) - Overs[0][0] <2:
          HomeOver0[0].append(Overs[0][0])
          HomeOver0[1].append(len(rfd))
          HomeOver0[2].append(t)
        if len(rfd) - Overs[0][1] < 2:
          HomeOver1[0].append(Overs[0][1])
          HomeOver1[1].append(len(rfd))
          HomeOver1[2].append(t)
        if len(rfd) - Overs[0][2] <2:
          HomeOver2[0].append(Overs[0][2])
          HomeOver2[1].append(len(rfd))
          HomeOver2[2].append(t)
##Home Under##

        if len(rfd) - Overs[1][2] <= 1:
          UnderOver2[0].append(Overs[1][2])
          UnderOver2[1].append(len(rfd))
          UnderOver2[2].append(t)
        if len(rfd) - Overs[1][3] <= 1:
          UnderOver3[0].append(Overs[1][3])
          UnderOver3[1].append(len(rfd))
          UnderOver3[2].append(t) 
        if len(rfd) - Overs[1][4] <= 1:
          UnderOver4[0].append(Overs[1][4])
          UnderOver4[1].append(len(rfd))
          UnderOver4[2].append(t)   
        if len(rfd) - Overs[1][5] <= 1:
          UnderOver5[0].append(Overs[1][5])
          UnderOver5[1].append(len(rfd))
          UnderOver5[2].append(t)  
##Home Conceeded##
        Conceededround = BtOr.OverUnderSeaon(t,rfd,"k",6)
        if len(rfd) - Conceededround[0][0] <=1:
          HomeCon1[0].append(Conceededround[0][0])
          HomeCon1[1].append(len(rfd))
          HomeCon1[2].append(t)
        if len(rfd) - Conceededround[0][1] <=1:
          HomeCon2[0].append(Conceededround[0][1])
          HomeCon2[1].append(len(rfd))
          HomeCon2[2].append(t)
        if len(rfd) - Conceededround[0][2] <=1:
          HomeCon3[0].append(Conceededround[0][2])
          HomeCon3[1].append(len(rfd))
          HomeCon3[2].append(t)
        if len(rfd) - Conceededround[0][3] <=1:
          HomeCon4[0].append(Conceededround[0][3])
          HomeCon4[1].append(len(rfd))
          HomeCon4[2].append(t)
          ##HomeScoresBoth###
        if len(rfd) - hmeScorsBt[0] <=1:
          HomeSrBh[0].append(hmeScorsBt[0])
          HomeSrBh[1].append(len(rfd))
          HomeSrBh[2].append(t)
        if len(rfd) == hmeScorsBt[1] :
          HomeNotSrBh[0].append(hmeScorsBt[1])
          HomeNotSrBh[1].append(len(rfd))
          HomeNotSrBh[2].append(t)

        if len(rfd) - HomeScrd1st[0] <=1:
          Home1stG[0].append(HomeScrd1st[0])
          Home1stG[1].append(len(rfd))
          Home1stG[2].append(t)

        if len(rfd) - HomeScrd1st[1] <=1:
          Home1stNG[0].append(HomeScrd1st[1])
          Home1stNG[1].append(len(rfd))
          Home1stNG[2].append(t)

        if len(rfd) - HomeScrd2nd[1] <=1:
          Home2ndNG[0].append(HomeScrd2nd[1])
          Home2ndNG[1].append(len(rfd))
          Home2ndNG[2].append(t)

        if len(rfd) - HomeScrd2nd[0] <=1:
          Home2ndG[0].append(HomeScrd2nd[0])
          Home2ndG[1].append(len(rfd))
          Home2ndG[2].append(t)

                

df = pd.DataFrame(list(zip(HomeOver0[1],HomeOver0[0])),HomeOver0[2],columns =['HomeGamesPlayed','HomeOver:0.5'])
df1 = pd.DataFrame(list(zip(HomeOver1[1],HomeOver1[0])),HomeOver1[2],columns =['HomeGamesPlayed','HomeOver:1.5'])
df2 = pd.DataFrame(list(zip(HomeOver2[1],HomeOver2[0])),HomeOver2[2],columns =['HomeGamesPlayed','HomeOver:2.5'])

df3 = pd.DataFrame(list(zip(UnderOver2[1],UnderOver2[0])),UnderOver2[2],columns =['HomeGamesPlayed','HomeUnder:1.5'])
df4 = pd.DataFrame(list(zip(UnderOver3[1],UnderOver3[0])),UnderOver3[2],columns =['HomeGamesPlayed','HomeUnder:2.5'])
df5 = pd.DataFrame(list(zip(UnderOver4[1],UnderOver4[0])),UnderOver4[2],columns =['HomeGamesPlayed','HomeUnder:3.5'])
df6 = pd.DataFrame(list(zip(UnderOver5[1],UnderOver5[0])),UnderOver5[2],columns =['HomeGamesPlayed','HomeUnder:4.5'])

df7 = pd.DataFrame(list(zip(HomeCon1[1],HomeCon1[0])),HomeCon1[2],columns =['HomeGamesPlayed','HomeConceed:0.5'])
df8 = pd.DataFrame(list(zip(HomeCon2[1],HomeCon2[0])),HomeCon2[2],columns =['HomeGamesPlayed','HomeConceed:1.5'])
df9 = pd.DataFrame(list(zip(HomeCon3[1],HomeCon3[0])),HomeCon3[2],columns =['HomeGamesPlayed','HomeConceed:2.5'])
df10 = pd.DataFrame(list(zip(HomeCon4[1],HomeCon4[0])),HomeCon4[2],columns =['HomeGamesPlayed','HomeConceed:3.5'])
df11 = pd.DataFrame(list(zip(HomeSrBh[1],HomeSrBh[0])),HomeSrBh[2],columns =['HomeGamesPlayed','HomeScoredBoth'])
df12 = pd.DataFrame(list(zip(HomeNotSrBh[1],HomeNotSrBh[0])),HomeNotSrBh[2],columns =['HomeGamesPlayed','HomeNotScoredBoth'])
df13 = pd.DataFrame(list(zip(Home1stG[1],Home1stG[0])),Home1stG[2],columns =['HomeGamesPlayed','Home1stHomeGoal'])
df14 = pd.DataFrame(list(zip(Home1stNG[1],Home1stNG[0])),Home1stNG[2],columns =['HomeGamesPlayed','Home1stNoHomeGoal'])
df15 = pd.DataFrame(list(zip(Home2ndNG[1],Home2ndNG[0])),Home2ndNG[2],columns =['HomeGamesPlayed','Home2ndNoHomeGoal'])
df16 = pd.DataFrame(list(zip(Home2ndG[1],Home2ndG[0])),Home2ndG[2],columns =['HomeGamesPlayed','Home2ndHomeGoal'])




#df = pd.DataFrame(list(zip(numOfGames,round,Conceededround,BothHalvesround,HomeConBothHalvesround,HomeOver0,HHOver0,UnderOver0,HomeOver1,UnderOver1,HomeOver2,UnderOver2,HomeOver3,UnderOver3,HomeOver4,UnderOver4,HomeOver5,UnderOver5,HomeOver6,UnderOver6,AwayUnder6)),team,columns =['HomeGamesPlayed','HomeGoalsScored','HomeConceeded','HomeScoredBothHalves','HomeConceededBothHalves','HomeOver:0.5','HomeUnder:0.5','HomeScored1stH:0.5','HomeOver:1.5','HomeUnder:1.5','HomeOver:2.5','HomeUnder:2.5','HomeOver:3.5','HomeUnder:3.5','HomeOver:4.5','HomeUnder:4.5','HomeOver:5.5','HomeUnder:5.5','HomeOver:6.5,'HomeUnder:6.5','AwayUnder:6.5''])
#df = pd.DataFrame([round],index=[team], columns=['HomeGoalsScored'])    ,'HomeUnder:1.5','HomeUnder:2.5','HomeUnder:3.5','HomeUnder:4.5','HomeUnder:5.5','HomeUnder:6.5'   ,UnderOver1,UnderOver2,UnderOver3,UnderOver4,UnderOver5,UnderOver6

with pd.ExcelWriter('streaks\streaks.xlsx') as writer:

  df.to_excel(writer, sheet_name='HomeOver0.5')
  df1.to_excel(writer, sheet_name='HomeOver1,5')
  df2.to_excel(writer, sheet_name='HomeOver2,5')
  df3.to_excel(writer, sheet_name='HomeUnder1,5')
  df4.to_excel(writer, sheet_name='HomeUnde2,5')
  df5.to_excel(writer, sheet_name='HomeUnde3,5')
  df6.to_excel(writer, sheet_name='HomeUnde4,5')

  df7.to_excel(writer, sheet_name='HomeConceed0,5')
  df8.to_excel(writer, sheet_name='HomeConceed1,5')
  df9.to_excel(writer, sheet_name='HomeConceed2,5')
  df10.to_excel(writer, sheet_name='HomeConceed3,5')
  df11.to_excel(writer, sheet_name='HomeScoredBoth')
  df12.to_excel(writer, sheet_name='HomeNotScoredBoth')
  df13.to_excel(writer, sheet_name='Home1stHGoal')
  df14.to_excel(writer, sheet_name='Home1stNoHomeGoal')
  df16.to_excel(writer, sheet_name='Home2ndHomeGoal')
  df15.to_excel(writer, sheet_name='Home2ndNoHomeGoal')
  
  
 # df.to_excel("streaks\streaks.xlsx","HomeOver1,5",)
#plt.plot( team,round) 

  
# naming the x axis  k[3] == t and t == "Arsenal" or  }} or k[3] == t and t == "Arsenal"  or k[3] == t and t == "Liverpool" or k[4] == t and t == "Liverpool":
#plt.xlabel('x - axis') 
# naming the y axis   hgoal = 0 and
#plt.ylabel('y - axis') 
  
# giving a title to my graph 
#plt.title('Away Conceeded Whole Season ') 
  
# function to show the plot 
#plt.show()
