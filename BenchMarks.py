import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
#import sqlalchemy
#import matplotlib.pyplot as plt 
import numpy as np
#import seaborn as sb
from SecLPAnylaysis import SlPA


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select home from serieBB Distinct"
#insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2


teams = []
Ateams = []
Ateam = []
Hteam = []
numOfGames = []

whoBeatT
def createReport(data1,pd):
 
 #with pd.ExcelWriter('Homestreaks.xlsx') as writer:
 with pd.ExcelWriter('awaystreaks.xlsx') as writer:

  for ff in data1:
   if len(ff) >= 1: 
     try:
      sheetName =  ff[3][1]
      df2 = pd.DataFrame(list(zip(ff[1],ff[0])),ff[2],columns =[ff[4][1],sheetName])
      df2.to_excel(writer, sheet_name=sheetName )  
     except:
       g = ""
      
def whoBeatT(tems,Tem,actP):
      insert_stmt2 = "select * from serieBB25 Where away = " + Tem + " and hgoal = "+ actP + "Order By Tframe ASC"
      data = ("Chelsea")
      cursor.execute(insert_stmt2)
      sql_data = pd.DataFrame(cursor.fetchall())
      outcome = whobeatT2(tems,sql_data,"1")
      return outcome

def whobeatT2(tems,Tem,actP):
      pcount = 0
      ucount = 0
      for easch in Tem:
       for bea in tems:
        insert_stmt2 = "select * from serieBB25 Where Home = " + easch + " AND away = " + bea + " and hgoal >= "+ actP 
        data = ("Chelsea")
        cursor.execute(insert_stmt2)
        sql_data = pd.DataFrame(cursor.fetchall())
       if len(sql_data) > 0:
          pcount = pcount + 1
       else:
          ucount = ucount + 1 
      return pcount + " " + ucount
      


def awayFilter(data,actP):
  for ee in data[0]:
      insert_stmt2 = "select * from serieBB25 Where home = " + ee[3] + " Order By Tframe ASC"
      data = ("Chelsea")
      cursor.execute(insert_stmt2)
      sql_data = pd.DataFrame(cursor.fetchall())
      step1Teams = []
      for eash in sql_data[0]:
        if eash[5] >= actP:
         step1Teams.append(eash[4])
      whoBeatT(step1Teams,ee[3],actP)




















 












  

#homeFilter(sql_data)
#awayFilter(sql_data)
          #1             #2        #3             #4           #5           #6                 #7              #8                 #9             #10               #11         #12            #13            #14         #15      #16      #17       #18            #19       #20       #21          #22              #23            #24        #25      #26       #27       #28         #29       #30       #31         #32        #33       #34         #35          #36                 #37                     #38                       #39                      #40                        #41                    #42                                                                              
#Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ, ConceedFSoutcome,ConceedFSoutcomeOne,ConceedFSoutcomeTwo, ScoreFSoutcome, ScoreFSoutcomeTwo, ScoreFSoutcomeOne,)
                      
#SecLayerInfor = (ScoreFSoutcomeAny,FirstHalfAcionSecondHalfOutput,FirstHalfAcionSecondHalfOverUnderZ,FirstHalfAcionSecondHalfOverUnderZOne,FirstHalfAcionSecondHalfOverUnderZTwo,FirstHalfAcionSecondHalfOverUnderZThree,FirstHalfAcionSecondHalfOverUnderO,FirstHalfAcionSecondHalfOverUnderOOne,FirstHalfAcionSecondHalfOverUnderOTwo,FirstHalfAcionSecondHalfOverUnderOThree,FirstHalfAcionSecondHalfOverUnderTThree,FirstHalfAcionSecondHalfOverUnderTTwo,FirstHalfAcionSecondHalfOverUnderTTOne,FirstHalfAcionSecondHalfOverUnderTT,FirstHalfAcionSecondHalfOverUnderTTThree,FirstHalfAcionSecondHalfOverUnderTTTwo,FirstHalfAwayWinSecondHalfLose,FirstHalfAwayWinSecondHalfHomeWindraw,FirstHalfAwayWinSecondHalfHomeScore,FirstHAwayWinSecHAwayScore1,FirstHAwayWinSecHAwayScore2,FirstHAwayWinSecHAwayScore3,FirstHAwayWinSecHHomeScore1,FirstHAwayWinSecHHomeScore2,FirstHAwayWinSecHHomeScore3)
#createReport(Info,pd)





