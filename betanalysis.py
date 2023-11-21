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
        #hmeScorsBt = BtOr.ScoredBothHalvesSeaon(t,rfd,"k",5)
        #HomeScrd1st = BtOr.ScoredWholeSeaon(t,rfd,"k",7)
        #HomeScrd2nd = BtOr.ndScoredWholeSeaon(t,rfd,"k",5)
        #Overs = BtOr.OverUnderSeaon(t,rfd,"k",5)
        HomeScrd1st = BtOr.OverUnderSeaon(t,rfd,"k",7) 
        HomeScrd2nd = BtOr.OverUnderSeaon(t,rfd,"L",5) 
       


      
        if len(rfd) - HomeScrd2nd[1][0] <=1:
          Home2ndNG[0].append(HomeScrd2nd[1])
          Home2ndNG[1].append(len(rfd))
          Home2ndNG[2].append(t)

        if len(rfd) - HomeScrd2nd[0][0] <=1:
          Home2ndG[0].append(HomeScrd2nd[0])
          Home2ndG[1].append(len(rfd))
          Home2ndG[2].append(t)
       
                

df19 = pd.DataFrame(list(zip(Home1st3G[1],Home1st3G[0])),Home1st3G[2],columns =['HomeGamesPlayed','Home1stHalf3Goal'])
df20 = pd.DataFrame(list(zip(Home1stb3G[1],Home1stb3G[0])),Home1stb3G[2],columns =['HomeGamesPlayed','Home1stHalfBelow3Goal'])




#df = pd.DataFrame(list(zip(numOfGames,round,Conceededround,BothHalvesround,HomeConBothHalvesround,HomeOver0,HHOver0,UnderOver0,HomeOver1,UnderOver1,HomeOver2,UnderOver2,HomeOver3,UnderOver3,HomeOver4,UnderOver4,HomeOver5,UnderOver5,HomeOver6,UnderOver6,AwayUnder6)),team,columns =['HomeGamesPlayed','HomeGoalsScored','HomeConceeded','HomeScoredBothHalves','HomeConceededBothHalves','HomeOver:0.5','HomeUnder:0.5','HomeScored1stH:0.5','HomeOver:1.5','HomeUnder:1.5','HomeOver:2.5','HomeUnder:2.5','HomeOver:3.5','HomeUnder:3.5','HomeOver:4.5','HomeUnder:4.5','HomeOver:5.5','HomeUnder:5.5','HomeOver:6.5,'HomeUnder:6.5','AwayUnder:6.5''])
#df = pd.DataFrame([round],index=[team], columns=['HomeGoalsScored'])    ,'HomeUnder:1.5','HomeUnder:2.5','HomeUnder:3.5','HomeUnder:4.5','HomeUnder:5.5','HomeUnder:6.5'   ,UnderOver1,UnderOver2,UnderOver3,UnderOver4,UnderOver5,UnderOver6

with pd.ExcelWriter('streaks\streaks.xlsx') as writer:

  
 
  
  df19.to_excel(writer, sheet_name='Home1stHalf3Goal')
  df20.to_excel(writer, sheet_name='Home1stHalfBelow3Goal')
  
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
