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

def FirstStHalfHomeConceedAwayOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
  
    if tb[3] == tt[0] and int(tb[7]) == actP3 and int(tb[8]) == actP:
      HomeFixFound = True
    if tb[4] == tt[0] and int(tb[6]) <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if tb[4] == tt[0] and int(tb[6]) >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome

def SecHalfHomeConceedAwayOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
    Homesechalfscore = int(tb[5]) - int(tb[7])
    Awaysechalfscore = int(tb[6]) - int(tb[8])
    if tb[3] == tt[0] and Homesechalfscore == actP3 and Awaysechalfscore == actP:
      HomeFixFound = True
    if tb[4] == tt[0] and int(tb[6]) <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if tb[4] == tt[0] and int(tb[6]) >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome

def HalftimeHomeConceedSecHalfOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
    Homesechalfscore = int(tb[5]) - int(tb[7])
    if tb[3] == tt[0] and int(tb[7]) == actP3 and int(tb[8]) == actP:
      HomeFixFound = True
    if Homesechalfscore <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if Homesechalfscore >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome

def HalftimeHomeConceedSecHalfAwayOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
    Awaysechalfscore = int(tb[6]) - int(tb[8])
    if tb[3] == tt[0] and int(tb[7]) == actP3 and int(tb[8]) == actP:
      HomeFixFound = True
    if Awaysechalfscore <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if Awaysechalfscore >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome

def HalftimeHomeConceedSecHalfOverallOutcome(sql_data,actP,actP2,actP3):
 TeamsOutcome = []

 for tt in sql_data: 
  HomeFixFound = False
  Conceed3Under1AwayUnder3 = 0 
  Conceed3Under1AwayOver3 = 0 
  for tb in sql_data2[0]:
    Awaysechalfscore = int(tb[6]) - int(tb[8])
    Homesechalfscore = int(tb[5]) - int(tb[7])
    overallScore = Homesechalfscore + Awaysechalfscore
    if tb[3] == tt[0] and int(tb[7]) == actP3 and int(tb[8]) == actP:
      HomeFixFound = True
    if overallScore <= actP2 and HomeFixFound: 
       Conceed3Under1AwayUnder3 = Conceed3Under1AwayUnder3 + 1
       HomeFixFound = False
    if overallScore >= actP2 and HomeFixFound:
      Conceed3Under1AwayOver3 = Conceed3Under1AwayOver3 + 1
      HomeFixFound = False
  
  TeamsOutcome.append(tt[0]+ " " +str(Conceed3Under1AwayUnder3) + " " +str(Conceed3Under1AwayOver3))
 return TeamsOutcome

#================================================================================================= 
#                                           FullTime
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
HomeConceed3ScoreZeroAwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
HomeConceed3ScoreZeroAwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
HomeConceed3ScoreZeroAwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
HomeConceed3ScoreZeroAwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
HomeConceed3Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
HomeConceed3Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
HomeConceed3Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
HomeConceed3Score1AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
HomeConceed3Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
HomeConceed3Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
HomeConceed3Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
HomeConceed3Score2AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],3,0,2)

#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
HomeConceed3Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
HomeConceed3Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
HomeConceed3Score3AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
HomeConceed3Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],3,0,3)
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
#1. Home 0 Away 2, 2. Away Over/Under 0
HomeConceed2ScoreZeroAwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
HomeConceed2Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
HomeConceed2Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
HomeConceed2Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
HomeConceed2Score1AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
HomeConceed2Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
HomeConceed2Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
HomeConceed2Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
HomeConceed2Score2AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
HomeConceed2Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
HomeConceed2Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
HomeConceed2Score3AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
HomeConceed2Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],2,0,3)

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
#1. Home 0 Away 1, 2. Away Over/Under 0
HomeConceed1ScoreZeroAwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
HomeConceed1Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
HomeConceed1Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
HomeConceed1Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
HomeConceed1Score1AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
HomeConceed1Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
HomeConceed1Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
HomeConceed1Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
HomeConceed1Score2AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],1,0,2)
#=================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
HomeConceed1Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
HomeConceed1Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
HomeConceed1Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
HomeConceed1Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
HomeConceed0ScoreZeroAwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
HomeConceed0ScoreZeroAwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
HomeConceed0ScoreZeroAwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
HomeConceed0ScoreZeroAwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],0,0,0)
#================================================================================================= 
#1. Home 1 Away 0, 2. Away Over/Under 3
HomeConceed0Score1AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
HomeConceed0Score1AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
HomeConceed0Score1AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
HomeConceed0Score1AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
HomeConceed0Score2AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
HomeConceed0Score2AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
HomeConceed0Score2AwayUnder1Outcome = HomeConceedAwayOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
HomeConceed0Score2AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
HomeConceed0Score3AwayUnder3Outcome = HomeConceedAwayOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
HomeConceed0Score3AwayUnder2Outcome = HomeConceedAwayOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
HomeConceed0Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
HomeConceed0Score3AwayUnder0Outcome = HomeConceedAwayOutcome(sql_data[0],0,0,3)

#================================================================================================= 
#                                           HalfTime
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
FirstHomeConceed3ScoreZeroAwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
FirstHomeConceed3ScoreZeroAwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
FirstHomeConceed3ScoreZeroAwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
FirstHomeConceed3ScoreZeroAwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
FirstHomeConceed3Score1AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
FirstHomeConceed3Score1AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
FirstHomeConceed3Score1AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
FirstHomeConceed3Score1AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
FirstHomeConceed3Score2AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
FirstHomeConceed3Score2AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
FirstHomeConceed3Score2AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
FirstHomeConceed3Score2AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,0,2)

#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
FirstHomeConceed3Score3AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
FirstHomeConceed3Score3AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
FirstHomeConceed3Score3AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
FirstHomeConceed3Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],3,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 2, 2. Away Over/Under 3
FirstHomeConceed2ScoreZeroAwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
FirstHomeConceed2ScoreZeroAwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
FirstHomeConceed2ScoreZeroAwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,1,0)
#1. Home 0 Away 2, 2. Away Over/Under 0
FirstHomeConceed2ScoreZeroAwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
FirstHomeConceed2Score1AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
FirstHomeConceed2Score1AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
FirstHomeConceed2Score1AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
FirstHomeConceed2Score1AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
FirstHomeConceed2Score2AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
FirstHomeConceed2Score2AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
FirstHomeConceed2Score2AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
FirstHomeConceed2Score2AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
FirstHomeConceed2Score3AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
FirstHomeConceed2Score3AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
FirstHomeConceed2Score3AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
FirstHomeConceed2Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],2,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
FirstHomeConceed1ScoreZeroAwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
FirstHomeConceed1ScoreZeroAwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
FirstHomeConceed1ScoreZeroAwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,1,0)
#1. Home 0 Away 1, 2. Away Over/Under 0
FirstHomeConceed1ScoreZeroAwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
FirstHomeConceed1Score1AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
FirstHomeConceed1Score1AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
FirstHomeConceed1Score1AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
FirstHomeConceed1Score1AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
FirstHomeConceed1Score2AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
FirstHomeConceed1Score2AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
FirstHomeConceed1Score2AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
FirstHomeConceed1Score2AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,0,2)
#=================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
FirstHomeConceed1Score3AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
FirstHomeConceed1Score3AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
FirstHomeConceed1Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
FirstHomeConceed1Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
FirstHomeConceed0ScoreZeroAwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
FirstHomeConceed0ScoreZeroAwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
FirstHomeConceed0ScoreZeroAwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
FirstHomeConceed0ScoreZeroAwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,0,0)
#==================================================================================================== 
#1. Home 1 Away 0, 2. Away Over/Under 3
FirstHomeConceed0Score1AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
FirstHomeConceed0Score1AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
FirstHomeConceed0Score1AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
FirstHomeConceed1Score1AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
FirstHomeConceed0Score2AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
FirstHomeConceed0Score2AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
FirstHomeConceed0Score2AwayUnder1Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
FirstHomeConceed0Score2AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
FirstHomeConceed0Score3AwayUnder3Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
FirstHomeConceed0Score3AwayUnder2Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
FirstHomeConceed0Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
FirstHomeConceed0Score3AwayUnder0Outcome = FirstStHalfHomeConceedAwayOutcome(sql_data[0],0,0,3)
#================================================================================================= 
#                                        Second HalfTime
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
SecHalfHomeConceed3ScoreZeroAwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
SecHalfHomeConceed3ScoreZeroAwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
SecHalfHomeConceed3ScoreZeroAwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
SecHalfHomeConceed3ScoreZeroAwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
SecHalfHomeConceed3Score1AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
SecHalfHomeConceed3Score1AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
SecHalfHomeConceed3Score1AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
SecHalfHomeConceed3Score1AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
SecHalfHomeConceed3Score2AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
SecHalfHomeConceed3Score2AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
SecHalfHomeConceed3Score2AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
SecHalfHomeConceed3Score2AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,0,2)

#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
SecHalfHomeConceed3Score3AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
SecHalfHomeConceed3Score3AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
SecHalfHomeConceed3Score3AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
SecHalfHomeConceed3Score3AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],3,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 2, 2. Away Over/Under 3
SecHalfHomeConceed2ScoreZeroAwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
SecHalfHomeConceed2ScoreZeroAwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
SecHalfHomeConceed2ScoreZeroAwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,1,0)
#1. Home 0 Away 2, 2. Away Over/Under 0
SecHalfHomeConceed2ScoreZeroAwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
SecHalfHomeConceed2Score1AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
SecHalfHomeConceed2Score1AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
SecHalfHomeConceed2Score1AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
SecHalfHomeConceed2Score1AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
SecHalfHomeConceed2Score2AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
SecHalfHomeConceed2Score2AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
SecHalfHomeConceed2Score2AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
SecHalfHomeConceed2Score2AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
SecHalfHomeConceed2Score3AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
SecHalfHomeConceed2Score3AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
SecHalfHomeConceed2Score3AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
SecHalfHomeConceed2Score3AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],2,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
SecHalfHomeConceed1ScoreZeroAwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
SecHalfHomeConceed1ScoreZeroAwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
SecHalfHomeConceed1ScoreZeroAwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,1,0)
#1. Home 0 Away 1, 2. Away Over/Under 0
SecHalfHomeConceed1ScoreZeroAwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
SecHalfHomeConceed1Score1AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
SecHalfHomeConceed1Score1AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
SecHalfHomeConceed1Score1AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
SecHalfHomeConceed1Score1AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
SecHalfHomeConceed1Score2AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
SecHalfHomeConceed1Score2AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
SecHalfHomeConceed1Score2AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
SecHalfHomeConceed1Score2AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,0,2)
#=================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
SecHalfHomeConceed1Score3AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
SecHalfHomeConceed1Score3AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
SecHalfHomeConceed1Score3AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
SecHalfHomeConceed1Score3AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
SecHalfHomeConceed0ScoreZeroAwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
SecHalfHomeConceed0ScoreZeroAwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
SecHalfHomeConceed0ScoreZeroAwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
SecHalfFirstHomeConceed0ScoreZeroAwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,0,0)
#==================================================================================================== 
#1. Home 1 Away 0, 2. Away Over/Under 3
SecHalfHomeConceed0Score1AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
SecHalfHomeConceed0Score1AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
SecHalfHomeConceed0Score1AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
SecHalfHomeConceed1Score1AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
SecHalfHomeConceed0Score2AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
SecHalfHomeConceed0Score2AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
SecHalfHomeConceed0Score2AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
SecHalfHomeConceed0Score2AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
SecHalfHomeConceed0Score3AwayUnder3Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
SecHalfHomeConceed0Score3AwayUnder2Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
SecHalfHomeConceed0Score3AwayUnder1Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
SecHalfHomeConceed0Score3AwayUnder0Outcome = SecHalfHomeConceedAwayOutcome(sql_data[0],0,0,3)
#================================================================================================= 
#                    Home HalfTime Scoreline - SecondHalf Home Over/Under Outcome
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score0SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score0SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score0SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score0SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score2SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score2SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score2SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score2SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,0,2)
#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score3SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score3SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score3SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score3SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],3,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score0SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score0SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score0SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,1,0)
#1. Home 0 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score0SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score1SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score1SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score1SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score1SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score2SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score2SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score2SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score2SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score3SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score3SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score3SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score3SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],2,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score0SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score0SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score0SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,1,0)
#1. Home 0 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score0SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score1SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score1SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score1SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score1SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score2SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score2SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score2SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score2SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,0,2)
#=======================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score0SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score0SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score0SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score0SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,0,0)
#==================================================================================================== 
#1. Home 1 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score1SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score1SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score1SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score1SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score2SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score2SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score2SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score2SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score3SecHalfHomeScore3Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score3SecHalfHomeScore2Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score3SecHalfHomeScore1Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score3SecHalfHomeScore0Outcome = HalftimeHomeConceedSecHalfOutcome(sql_data[0],0,0,3)
#================================================================================================= 
#                    Home HalfTime Scoreline - SecondHalf Away Over/Under Outcome
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score0SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score0SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score0SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score0SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score2SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score2SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score2SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score2SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,0,2)
#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score3SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score3SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score3SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score3SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],3,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score0SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score0SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score0SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,1,0)
#1. Home 0 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score0SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score1SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score1SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score1SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score1SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score2SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score2SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score2SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score2SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score3SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score3SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score3SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score3SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],2,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score0SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score0SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score0SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,1,0)
#1. Home 0 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score0SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score1SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score1SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score1SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score1SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score2SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score2SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score2SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score2SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,0,2)
#=========================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score0SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score0SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score0SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score0SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,0,0)
#==================================================================================================== 
#1. Home 1 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score1SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score1SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score1SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score1SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score2SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score2SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score2SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score2SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score3SecHalfAwayScore3Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score3SecHalfAwayScore2Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score3SecHalfAwayScore1Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score3SecHalfAwayScore0Outcome = HalftimeHomeConceedSecHalfAwayOutcome(sql_data[0],0,0,3)
#================================================================================================= 
#                    Home HalfTime Scoreline - SecondHalf Overall Scoreline Over/Under Outcome
# 
# ================================================================================================ 
#1. Home 0 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score0SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,3,0)
#1. Home 0 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score0SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,2,0)
#1. Home 0 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score0SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,1,0)
#1. Home 0 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score0SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,0,0)
#=================================================================================================      
#1. Home 1 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,3,1)
#1. Home 1 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,2,1)
#1. Home 1 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,1,1)
#1. Home 1 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,0,1)
#=================================================================================================      
#1. Home 2 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score2SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,3,2)
#1. Home 2 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score2SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,2,2)
#1. Home 2 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score2SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,1,2)
#1. Home 2 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score2SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,0,2)
#=================================================================================================  #    
#1. Home 3 Away 3, 2. Away Over/Under 3
HalftimeHomeConceed3Score3SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,3,3)
#1. Home 3 Away 3, 2. Away Over/Under 2
HalftimeHomeConceed3Score3SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,2,3)
#1. Home 3 Away 3, 2. Away Over/Under 1
HalftimeHomeConceed3Score3SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,1,3)
#1. Home 3 Away 3, 2. Away Over/Under 0
HalftimeHomeConceed3Score3SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],3,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score0SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,3,0)
#1. Home 0 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score0SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,2,0)
#1. Home 0 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score0SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,1,0)
#1. Home 0 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score0SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,0,0)
#============================================================================================#
#1. Home 1 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score1SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,3,1)
#1. Home 1 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score1SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,2,1)
#1. Home 1 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score1SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,1,1)   
#1. Home 1 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score1SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,0,1)   
#=============================================================================================#  
#1. Home 2 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score2SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,3,2)
#1. Home 2 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score2SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,2,2)
#1. Home 2 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score2SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,1,2)
#1. Home 2 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score2SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,0,2)
#=================================================================================================      
#1. Home 3 Away 2, 2. Away Over/Under 3
HalftimeHomeConceed2Score3SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,3,3)
#1. Home 3 Away 2, 2. Away Over/Under 2
HalftimeHomeConceed2Score3SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,2,3)
#1. Home 3 Away 2, 2. Away Over/Under 1
HalftimeHomeConceed2Score3SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,1,3)
#1. Home 3 Away 2, 2. Away Over/Under 0
HalftimeHomeConceed2Score3SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],2,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score0SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,3,0)
#1. Home 0 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score0SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,2,0)
#1. Home 0 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score0SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,1,0)
#1. Home 0 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score0SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,0,0)
#================================================================================================= 
#1. Home 1 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score1SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,3,1)
#1. Home 1 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score1SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,2,1)
#1. Home 1 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score1SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,1,1) 
#1. Home 1 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score1SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,0,1) 
#=================================================================================================      
#1. Home 2 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed1Score2SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,3,2)
#1. Home 2 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed1Score2SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,2,2)
#1. Home 2 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed1Score2SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,1,2)
#1. Home 2 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed1Score2SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,0,2)
#=========================================================================================================      
#1. Home 3 Away 1, 2. Away Over/Under 3
HalftimeHomeConceed3Score1SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,3,3)
#1. Home 3 Away 1, 2. Away Over/Under 2
HalftimeHomeConceed3Score1SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,2,3)
#1. Home 3 Away 1, 2. Away Over/Under 1
HalftimeHomeConceed3Score1SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,1,3)
#1. Home 3 Away 1, 2. Away Over/Under 0
HalftimeHomeConceed3Score1SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],1,0,3)
#================================================================================================= 
# 
# 
# ================================================================================================ 
#1. Home 0 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score0SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,3,0)
#1. Home 0 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score0SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,2,0)
#1. Home 0 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score0SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,1,0)
#1. Home 0 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score0SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,0,0)
#==================================================================================================== 
#1. Home 1 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score1SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,3,1)
#1. Home 1 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score1SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,2,1)
#1. Home 1 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score1SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,1,1) 
#1. Home 1 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score1SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,0,1) 
#=================================================================================================      
#1. Home 2 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score2SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,3,2)
#1. Home 2 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score2SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,2,2)
#1. Home 2 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score2SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,1,2)
#1. Home 2 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score2SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,0,2)
#=================================================================================================      
#1. Home 3 Away 0, 2. Away Over/Under 3
HalftimeHomeConceed0Score3SecHalfOverallScore3Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,3,3)
#1. Home 3 Away 0, 2. Away Over/Under 2
HalftimeHomeConceed0Score3SecHalfOverallScore2Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,2,3)
#1. Home 3 Away 0, 2. Away Over/Under 1
HalftimeHomeConceed0Score3SecHalfOverallScore1Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,1,3)
#1. Home 3 Away 0, 2. Away Over/Under 0
HalftimeHomeConceed0Score3SecHalfOverallScore0Outcome = HalftimeHomeConceedSecHalfOverallOutcome(sql_data[0],0,0,3)


def createReport(data1,pd):
 
 with pd.ExcelWriter('Homestreaks.xlsx') as writer:
 # with pd.ExcelWriter('awaystreaks.xlsx') as writer:

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





