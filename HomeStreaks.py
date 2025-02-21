import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import numpy as np
from multiLayerPerceptron import mlp
from SecLPAnylaysis import SlPA

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from Austria125"

cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2

HomefullOver1 = ([],[],[],[],[])
HomefullOver2 = ([],[],[],[],[])

teams = []
Hteam = []

def createReport(data1,pd):
 
 #with pd.ExcelWriter('Homestreakss.xlsx') as writer:
 #with pd.ExcelWriter('awaystreaks.xlsx') as writer:
  li1 = data1[0][0]
  li2 = data1[0][1]
  li3 = data1[0][2]
  li4 = data1[0][3]
  my_dict = {'Team': li3, 'GamesPlayed': li2}
  colmns = []
  for ee in data1:
    my_dict.update({ee[3][0]: ee[0]})

  df = pd.DataFrame( my_dict)
  df.to_excel('Streakshominfo.xlsx', sheet_name="Home", index=False)
  #for ee in data1:

def homeFilter(data):
  for ee in sql_data[0]:
   if ee[3] in teams:
    t = ee[3]
   else:
    teams.append(ee[3])

  for w in teams:
   t = w
   occurence = 0
   if t in Hteam:
      occurence = 0
   else:
     rfdA = BtOr.refindedDatam(t,data,3)
     streaksOver = BtOr.StreaksOverUnder(t,rfdA,"k",5,"over")
     streaksOver1 = BtOr.StreaksOverUnder1(t,rfdA,"k",5,"over")
#=====================================================================================================#
#Home Fix fulltime over 0.5 Streaks
            
     HomefullOver1[0].append(str(streaksOver[0])+ "/" +str(streaksOver[1]))
     HomefullOver1[1].append(len(rfdA))
     HomefullOver1[2].append(t)
     HomefullOver1[3].append("HomeFixtureFulltimeOverZ")
     HomefullOver1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fix fulltime over 1.5 Streaks
            
     HomefullOver2[0].append(str(streaksOver1[0])+ "/" +str(streaksOver1[1]))
     HomefullOver2[1].append(len(rfdA))
     HomefullOver2[2].append(t)
     HomefullOver2[3].append("HomeFixtureFulltimeOver1")
     HomefullOver2[4].append("HomeGamesPlayed")
homeFilter(sql_data)
Info=(HomefullOver1,HomefullOver2)
createReport(Info,pd)