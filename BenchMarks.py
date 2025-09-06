import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
#import sqlalchemy
#import matplotlib.pyplot as plt 
import numpy as np
#import seaborn as sb
from SecLPAnylaysis import SlPA


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select Distinct home from EPL25"
#insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
#data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())

insert_stmt2 = "select * from EPL25 ORDER BY Tframe ASC"
#insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
#data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data2 = pd.DataFrame(cursor.fetchall())

conn.close()
teamCount = 0
halftomeGap = 2

def HomeConceedAwayOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
  
    if tb[3] == tt[0] and int(tb[5]) == actP3 and int(tb[6]) == actP:
      HomeFixFound = True
    if tb[4] == tt[0] and int(tb[6]) <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if tb[4] == tt[0] and int(tb[6]) >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome



#1. Home 0 Away 3, 2. Away Over/Under 3
HomeConceed3ScoreZeroAwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
HomeConceed3ScoreZeroAwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
HomeConceed3ScoreZeroAwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
HomeConceed3Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
HomeConceed3Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
HomeConceed3Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
HomeConceed3Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
HomeConceed3Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
HomeConceed3Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,2)
#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
HomeConceed3Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
HomeConceed3Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
HomeConceed3Score3AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,3)
#========================================================================================#
#
#
#===========================================================================================#
#1. Home 0 Away 2, 2. Away Over/Under 3
HomeConceed2ScoreZeroAwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
HomeConceed2ScoreZeroAwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
HomeConceed2ScoreZeroAwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
HomeConceed2Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
HomeConceed2Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
HomeConceed2Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
HomeConceed2Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
HomeConceed2Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
HomeConceed2Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
HomeConceed2Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
HomeConceed2Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
HomeConceed2Score3AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
HomeConceed1ScoreZeroAwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
HomeConceed1ScoreZeroAwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
HomeConceed1ScoreZeroAwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
HomeConceed1Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
HomeConceed1Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
HomeConceed1Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
HomeConceed1Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
HomeConceed1Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
HomeConceed1Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,2)
#=================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
HomeConceed1Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
HomeConceed1Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
HomeConceed1Score3AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,3)

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
      




















 












  

#homeFilter(sql_data)
#awayFilter(sql_data)
          #1             #2        #3             #4           #5           #6                 #7              #8                 #9             #10               #11         #12            #13            #14         #15      #16      #17       #18            #19       #20       #21          #22              #23            #24        #25      #26       #27       #28         #29       #30       #31         #32        #33       #34         #35          #36                 #37                     #38                       #39                      #40                        #41                    #42                                                                              
#Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ, ConceedFSoutcome,ConceedFSoutcomeOne,ConceedFSoutcomeTwo, ScoreFSoutcome, ScoreFSoutcomeTwo, ScoreFSoutcomeOne,)
                      
#SecLayerInfor = (ScoreFSoutcomeAny,FirstHalfAcionSecondHalfOutput,FirstHalfAcionSecondHalfOverUnderZ,FirstHalfAcionSecondHalfOverUnderZOne,FirstHalfAcionSecondHalfOverUnderZTwo,FirstHalfAcionSecondHalfOverUnderZThree,FirstHalfAcionSecondHalfOverUnderO,FirstHalfAcionSecondHalfOverUnderOOne,FirstHalfAcionSecondHalfOverUnderOTwo,FirstHalfAcionSecondHalfOverUnderOThree,FirstHalfAcionSecondHalfOverUnderTThree,FirstHalfAcionSecondHalfOverUnderTTwo,FirstHalfAcionSecondHalfOverUnderTTOne,FirstHalfAcionSecondHalfOverUnderTT,FirstHalfAcionSecondHalfOverUnderTTThree,FirstHalfAcionSecondHalfOverUnderTTTwo,FirstHalfAwayWinSecondHalfLose,FirstHalfAwayWinSecondHalfHomeWindraw,FirstHalfAwayWinSecondHalfHomeScore,FirstHAwayWinSecHAwayScore1,FirstHAwayWinSecHAwayScore2,FirstHAwayWinSecHAwayScore3,FirstHAwayWinSecHHomeScore1,FirstHAwayWinSecHHomeScore2,FirstHAwayWinSecHHomeScore3)
#createReport(Info,pd)





