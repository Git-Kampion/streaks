import pyodbc
from BetTypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb




#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\Database1.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from Epl where hgoal > 0"
data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2



teams = []
round = []
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
        res = BtOr.findConcurrentMAtche(t,sql_data,occurence)     
        round.append(res)
        team.append(t)
        # print(k)
plt.plot( team,round) 
  
# naming the x axis  k[3] == t and t == "Arsenal" or  }} or k[3] == t and t == "Arsenal"  or k[3] == t and t == "Liverpool" or k[4] == t and t == "Liverpool":
plt.xlabel('x - axis') 
# naming the y axis   hgoal = 0 and
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Scored Whole Season at Home') 
  
# function to show the plot 
plt.show()
