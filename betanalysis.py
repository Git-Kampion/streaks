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

insert_stmt2 = "select * from EPL"
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
        res = BtOr.ScoredWholeSeaon(t,rfd,"k",5)    
        cd = BtOr.ConcededWholeSeaon(t,rfd,"k",6)   
        bh = BtOr.ScoredBothHalvesSeaon(t,rfd,"k",5)
        Abh = BtOr.ConceededBothHalvesSeaon(t,rfd,"k",6) 
        Overs = BtOr.HomeOverSeaon(t,rfd,"k",5)      
        BothHalvesround.append(bh)
        HomeConBothHalvesround.append(Abh)
        round.append(res )
        Conceededround.append(cd)
        numOfGames.append(len(rfd))
        team.append(t)
        # print(k)
df = pd.DataFrame(list(zip(numOfGames,round,Conceededround,BothHalvesround,HomeConBothHalvesround)),team,columns =['HomeGamesPlayed','HomeGoalsScored','HomeConceeded','HomeScoredBothHalves','HomeConceededBothHalves'])
#df = pd.DataFrame([round],index=[team], columns=['HomeGoalsScored'])

print(df)
#plt.plot( team,round) 

  
# naming the x axis  k[3] == t and t == "Arsenal" or  }} or k[3] == t and t == "Arsenal"  or k[3] == t and t == "Liverpool" or k[4] == t and t == "Liverpool":
#plt.xlabel('x - axis') 
# naming the y axis   hgoal = 0 and
#plt.ylabel('y - axis') 
  
# giving a title to my graph 
#plt.title('Away Conceeded Whole Season ') 
  
# function to show the plot 
#plt.show()
