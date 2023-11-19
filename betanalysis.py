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


HHunder0 = []
HHunder1 = []
HHunder2 = []
HHunder3 = []
HHunder4 = []
HHunder5 = []
HHunder6 = []


HomeOver0 = []
HomeOver1 = []
HomeOver2 = []
HomeOver3 = []
HomeOver4 = []
HomeOver5 = []
HomeOver6 = []
HomeOver6 = []

UnderOver0 = []
UnderOver1 = []
UnderOver2 = []
UnderOver3 = []
UnderOver4 = []
UnderOver5 = []
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
        #res = BtOr.ScoredWholeSeaon(t,rfd,"k",5)    
        cd = BtOr.ConcededWholeSeaon(t,rfd,"k",6)   
        #bh = BtOr.ScoredBothHalvesSeaon(t,rfd,"k",5)
        #Abh = BtOr.ConceededBothHalvesSeaon(t,rfd,"k",6) 
       
        #AOvers = BtOr.OverUnderSeaon(t,rfd,"k",6)
        #H1stOvers = BtOr.OverUnderSeaon(t,rfd,"k",7)
        
          Overs = BtOr.OverUnderSeaon(t,rfd,"k",5) 
        
          HomeOver0.append(Overs[0][0]) 
          HomeOver1.append(Overs[0][1]) 
          HomeOver2.append(Overs[0][2])
          HomeOver3.append(Overs[0][3])                  
          HomeOver4.append(Overs[0][4])                  
          HomeOver5.append(Overs[0][5])                  
          HomeOver6.append(Overs[0][6])      
          UnderOver0.append(Overs[1][0]) 
          UnderOver1.append(Overs[1][1]) 
          UnderOver2.append(Overs[1][2])
          UnderOver3.append(Overs[1][3])                  
          UnderOver4.append(Overs[1][4])                  
          UnderOver5.append(Overs[1][5])                  
          UnderOver6.append(Overs[1][6])   

        AwayOver0.append(AOvers[0][0]) 
        AwayOver1.append(AOvers[0][1]) 
        AwayOver2.append(AOvers[0][2])
        AwayOver3.append(AOvers[0][3])                  
        AwayOver4.append(AOvers[0][4])                  
        AwayOver5.append(AOvers[0][5])                  
        AwayOver6.append(AOvers[0][6])      
        AwayUnder0.append(AOvers[1][0]) 
        AwayUnder1.append(AOvers[1][1]) 
        AwayUnder2.append(AOvers[1][2])
        AwayUnder3.append(AOvers[1][3])                  
        AwayUnder4.append(AOvers[1][4])                  
        AwayUnder5.append(AOvers[1][5])                  
        AwayUnder6.append(AOvers[1][6])  
          
         

        HHOver0.append(H1stOvers[0][0]) 
        HHOver1.append(H1stOvers[0][1]) 
        HHOver2.append(H1stOvers[0][2])
        HHOver3.append(H1stOvers[0][3])                  
        HHOver4.append(H1stOvers[0][4])                  
        HHOver5.append(H1stOvers[0][5])                  
        HHOver6.append(H1stOvers[0][6])    

        HHunder0.append(H1stOvers[1][0]) 
        HHunder1.append(H1stOvers[1][1]) 
        HHunder2.append(H1stOvers[1][2])
        HHunder3.append(H1stOvers[1][3])                  
        HHunder4.append(H1stOvers[1][4])                  
        HHunder5.append(H1stOvers[1][5])                  
        HHunder6.append(H1stOvers[1][6])    
"""
        #BothHalvesround.append(bh)
        #HomeConBothHalvesround.append(Abh)
        if len(rfd) == res:
          round.append(res)
        if len(rfd) == res and len(rfd) == cd:
         
          Conceededround.append(cd)
          numOfGames.append(len(rfd))
          team.append(t)
        # print(k)

df = pd.DataFrame(list(zip(numOfGames,round)),team,columns =['HomeGamesPlayed','HomeOver:0.5'])
#df = pd.DataFrame(list(zip(numOfGames,round,Conceededround,BothHalvesround,HomeConBothHalvesround,HomeOver0,HHOver0,UnderOver0,HomeOver1,UnderOver1,HomeOver2,UnderOver2,HomeOver3,UnderOver3,HomeOver4,UnderOver4,HomeOver5,UnderOver5,HomeOver6,UnderOver6,AwayUnder6)),team,columns =['HomeGamesPlayed','HomeGoalsScored','HomeConceeded','HomeScoredBothHalves','HomeConceededBothHalves','HomeOver:0.5','HomeUnder:0.5','HomeScored1stH:0.5','HomeOver:1.5','HomeUnder:1.5','HomeOver:2.5','HomeUnder:2.5','HomeOver:3.5','HomeUnder:3.5','HomeOver:4.5','HomeUnder:4.5','HomeOver:5.5','HomeUnder:5.5','HomeOver:6.5,'HomeUnder:6.5','AwayUnder:6.5''])
#df = pd.DataFrame([round],index=[team], columns=['HomeGoalsScored'])    ,'HomeUnder:1.5','HomeUnder:2.5','HomeUnder:3.5','HomeUnder:4.5','HomeUnder:5.5','HomeUnder:6.5'   ,UnderOver1,UnderOver2,UnderOver3,UnderOver4,UnderOver5,UnderOver6
with pd.ExcelWriter('streaks\streaks.xlsx') as writer:

  df.to_excel(writer, sheet_name='HomeOver0.5')
  df.to_excel(writer, sheet_name='HomeOver1,5')
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
