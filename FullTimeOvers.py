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

insert_stmt2 = "select * from eplNo"
#insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
data = ("Chelsea")
cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2


teams = []
Ateams = []
Ateam = []
numOfGames = []

AwyOvs= ([],[],[],[],[])
AwySConceedOvs= ([],[],[],[],[])
AwySConceedOvs2= ([],[],[],[],[])
AwySConceedOvs3= ([],[],[],[],[])

AwyFirstfailtToConceedOvs= ([],[],[],[],[])
AwyFirstfailtToConceedOvs2= ([],[],[],[],[])
AwyFirstfailtToConceedOvs3= ([],[],[],[],[])

AwySfailtToConceedOvs= ([],[],[],[],[])
AwySfailtToConceedOvs2= ([],[],[],[],[])
AwySfailtToConceedOvs3= ([],[],[],[],[])

AwyFConceedOvs = ([],[],[],[],[])
AwyFConceedOvs2 = ([],[],[],[],[])
AwyFConceedOvs3 = ([],[],[],[],[])

AwyFfailtToConceedOvs = ([],[],[],[],[])
AwyFfailtToConceedOvs2 = ([],[],[],[],[])
AwyFfailtToConceedOvs3 = ([],[],[],[],[])

AwySOvs= ([],[],[],[],[])
AwySOvs1= ([],[],[],[],[])
AwySOvs2= ([],[],[],[],[])

AwyFOvs= ([],[],[],[],[])
AwyFOvs1= ([],[],[],[],[])
AwyFOvs2= ([],[],[],[],[])

AwyFUnder= ([],[],[],[],[])
AwyFUnder1= ([],[],[],[],[])
AwyFUnder2= ([],[],[],[],[])
AwyFUnder3= ([],[],[],[],[])

AwyUnder= ([],[],[],[],[])
AwyUnder1= ([],[],[],[],[])
AwyUnder2= ([],[],[],[],[])
AwyUnder3= ([],[],[],[],[])
AwyUnder4= ([],[],[],[],[])
AwyUnder5= ([],[],[],[],[])

AwyOvs1= ([],[],[],[],[])
AwyOvs2= ([],[],[],[],[])

Bts= ([],[],[],[],[])
aWins= ([],[],[],[],[])
a2ndHWins= ([],[],[],[],[])
a2ndHFailureWins= ([],[],[],[],[])
aHalftimeWins= ([],[],[],[],[])
aFuilureToWins= ([],[],[],[],[])
aFuilureToHalfWins = ([],[],[],[],[])

FullTimeOvers= ([],[],[],[],[])
FullTimeOvers2= ([],[],[],[],[])
FullTimeOvers3= ([],[],[],[],[])
FullTimeOvers4= ([],[],[],[],[])


def createReport(data1,pd):
 
 with pd.ExcelWriter('streaks.xlsx') as writer:

  for ff in data1:
   if len(ff) >= 1: 
     try:
      sheetName =  ff[3][1]
      df2 = pd.DataFrame(list(zip(ff[1],ff[0])),ff[2],columns =[ff[4][1],sheetName])
      df2.to_excel(writer, sheet_name=sheetName )  
     except:
       g = ""
      


def awayFilter(data):
  for bb in data[0]:
   if bb[4] in Ateams:
    t = bb[4]
   else:
    Ateams.append(bb[4])
  
  for w in Ateams:
    t = w
    occurence = 0
    if t in Ateam:
      occurence = 0
    else:
     rfdA = BtOr.refindedDatam(t,data,4)
     AwOvers = BtOr.OverUnderSeaon(t,rfdA,"a",6)
     afullTimeOver = BtOr.FixOverUnders(t,rfdA,"a",6)
     hBTS = BtOr.Bts(t,rfdA,"a",6)
     aWinLose = BtOr.MatchRes(t,rfdA,"a",6)

   #Away 2ndHalf wins
     if len(rfdA) - aWinLose[0][10] <= 1:          
          a2ndHWins[0].append(aWinLose[0][10])
          a2ndHWins[1].append(len(rfdA))
          a2ndHWins[2].append(t)
          a2ndHWins[3].append("Away2ndHalfWins")
          a2ndHWins[4].append("AwayGamesPlayed")
#Away 2ndHalf failuir to win
     if len(rfdA) - aWinLose[0][9] <= 1:          
          a2ndHFailureWins[0].append(aWinLose[0][9])
          a2ndHFailureWins[1].append(len(rfdA))
          a2ndHFailureWins[2].append(t)
          a2ndHFailureWins[3].append("AwayHalftimeFailToWin")
          a2ndHFailureWins[4].append("AwayGamesPlayed")  
#========================================================================#
#Away halftime wins
     if len(rfdA) - aWinLose[0][6] <= 1:          
          aHalftimeWins[0].append(aWinLose[0][6])
          aHalftimeWins[1].append(len(rfdA))
          aHalftimeWins[2].append(t)
          aHalftimeWins[3].append("AwayHalfWins")
          aHalftimeWins[4].append("AwayGamesPlayed")
#Away halftime failuir to win
     if len(rfdA) - aWinLose[0][5] <= 1:          
          aFuilureToHalfWins[0].append(aWinLose[0][5])
          aFuilureToHalfWins[1].append(len(rfdA))
          aFuilureToHalfWins[2].append(t)
          aFuilureToHalfWins[3].append("AwayHalftimeFailToWin")
          aFuilureToHalfWins[4].append("AwayGamesPlayed")
#=============================================================================#
#Away wins
     if len(rfdA) - aWinLose[0][2] <= 1:          
          aWins[0].append(aWinLose[0][2])
          aWins[1].append(len(rfdA))
          aWins[2].append(t)
          aWins[3].append("AwayWins")
          aWins[4].append("AwayGamesPlayed")
#Away failuir to win
     if len(rfdA) - aWinLose[0][1] <= 1:          
          aFuilureToWins[0].append(aWinLose[0][1])
          aFuilureToWins[1].append(len(rfdA))
          aFuilureToWins[2].append(t)
          aFuilureToWins[3].append("AwayFailToWin")
          aFuilureToWins[4].append("AwayGamesPlayed")
#=============================================================================#
#Away Failed to Conceed 1stHalf over 0.5
     if len(rfdA) - AwOvers[9][0] <= 1:          
          AwyFirstfailtToConceedOvs[0].append(AwOvers[9][0])
          AwyFirstfailtToConceedOvs[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs[2].append(t)
          AwyFirstfailtToConceedOvs[3].append("AwayFailConceed1stHlvGoal")
          AwyFirstfailtToConceedOvs[4].append("AwayGamesPlayed")
          
    #Away Failed to Conceed 1stHalf over 1.5
     if len(rfdA) - AwOvers[9][1] <= 5:         
          AwyFirstfailtToConceedOvs2[0].append(AwOvers[9][1])
          AwyFirstfailtToConceedOvs2[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs2[2].append(t)
          AwyFirstfailtToConceedOvs2[3].append("AwayFailConceed21stHlvGoal")
          AwyFirstfailtToConceedOvs2[4].append("AwayGamesPlayed")  
     #Away Failed to Conceed 1stHalf over 2.5
     if len(rfdA) - AwOvers[9][2] <= 7:          
          AwyFirstfailtToConceedOvs3[0].append(AwOvers[9][2])
          AwyFirstfailtToConceedOvs3[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs3[2].append(t)
          AwyFirstfailtToConceedOvs3[3].append("AwayFailConceed31stHlvGoal")
          AwyFirstfailtToConceedOvs3[4].append("AwayGamesPlayed") 
#===============================================================================#

 #Away Failed to Conceed 1stHalf over 0.5
     if len(rfdA) - AwOvers[9][0] <= 1:          
          AwyFirstfailtToConceedOvs[0].append(AwOvers[9][0])
          AwyFirstfailtToConceedOvs[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs[2].append(t)
          AwyFirstfailtToConceedOvs[3].append("AwayFailConceed1stHlvGoal")
          AwyFirstfailtToConceedOvs[4].append("AwayGamesPlayed")
          
    #Away Failed to Conceed 1stHalf over 1.5
     if len(rfdA) - AwOvers[9][1] <= 5:         
          AwyFirstfailtToConceedOvs2[0].append(AwOvers[9][1])
          AwyFirstfailtToConceedOvs2[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs2[2].append(t)
          AwyFirstfailtToConceedOvs2[3].append("AwayFailConceed21stHlvGoal")
          AwyFirstfailtToConceedOvs2[4].append("AwayGamesPlayed")  
     #Away Failed to Conceed 1stHalf over 2.5
     if len(rfdA) - AwOvers[9][2] <= 7:          
          AwyFirstfailtToConceedOvs3[0].append(AwOvers[9][2])
          AwyFirstfailtToConceedOvs3[1].append(len(rfdA))
          AwyFirstfailtToConceedOvs3[2].append(t)
          AwyFirstfailtToConceedOvs3[3].append("AwayFailConceed31stHlvGoal")
          AwyFirstfailtToConceedOvs3[4].append("AwayGamesPlayed") 
#===============================================================================#
     #Away Failed to Conceed SecHalf over 0.5
     if len(rfdA) - AwOvers[8][0] <= 1:          
          AwySfailtToConceedOvs[0].append(AwOvers[8][0])
          AwySfailtToConceedOvs[1].append(len(rfdA))
          AwySfailtToConceedOvs[2].append(t)
          AwySfailtToConceedOvs[3].append("AwayFailConceedSecHlvGoal")
          AwySfailtToConceedOvs[4].append("AwayGamesPlayed")
          
    #Away Failed to Conceed SecHalf over 1.5
     if len(rfdA) - AwOvers[8][1] <= 5:         
          AwySfailtToConceedOvs2[0].append(AwOvers[8][1])
          AwySfailtToConceedOvs2[1].append(len(rfdA))
          AwySfailtToConceedOvs2[2].append(t)
          AwySfailtToConceedOvs2[3].append("AwayFailConceed2SecHlvGoal")
          AwySfailtToConceedOvs2[4].append("AwayGamesPlayed")  
     #Away Failed to Conceed SecHalf over 2.5
     if len(rfdA) - AwOvers[8][2] <= 7:          
          AwySfailtToConceedOvs3[0].append(AwOvers[8][2])
          AwySfailtToConceedOvs3[1].append(len(rfdA))
          AwySfailtToConceedOvs3[2].append(t)
          AwySfailtToConceedOvs3[3].append("AwayFailConceed3SecHlvGoal")
          AwySfailtToConceedOvs3[4].append("AwayGamesPlayed") 
#===============================================================================#
      #Away Conceed SecHalf over 0.5
     if len(rfdA) - AwOvers[6][0] <= 1:          
          AwySConceedOvs[0].append(AwOvers[6][0])
          AwySConceedOvs[1].append(len(rfdA))
          AwySConceedOvs[2].append(t)
          AwySConceedOvs[3].append("AwayConceedSecHlvGoal")
          AwySConceedOvs[4].append("AwayGamesPlayed")
          
    #Away Conceed SecHalf over 1.5
     if len(rfdA) - AwOvers[6][1] <= 5:         
          AwySConceedOvs2[0].append(AwOvers[6][1])
          AwySConceedOvs2[1].append(len(rfdA))
          AwySConceedOvs2[2].append(t)
          AwySConceedOvs2[3].append("AwayConceed2SecHlvGoal")
          AwySConceedOvs2[4].append("AwayGamesPlayed")  
     #Away Conceed SecHalf over 2.5
     if len(rfdA) - AwOvers[6][2] <= 7:          
          AwySConceedOvs3[0].append(AwOvers[6][2])
          AwySConceedOvs3[1].append(len(rfdA))
          AwySConceedOvs3[2].append(t)
          AwySConceedOvs3[3].append("AwayConceed3SecHlvGoal")
          AwySConceedOvs3[4].append("AwayGamesPlayed") 
#=====================================================================================================#
          #Away Conceed 1stHalf over 0.5
          if len(rfdA) - AwOvers[7][0] <= 1:          
               AwyFConceedOvs[0].append(AwOvers[7][0])
               AwyFConceedOvs[1].append(len(rfdA))
               AwyFConceedOvs[2].append(t)
               AwyFConceedOvs[3].append("AwayConceed1stHlvGoal")
               AwyFConceedOvs[4].append("AwayGamesPlayed")
          #Away Conceed 1stHalf over 1.5
          if len(rfdA) - AwOvers[7][1] <= 5:         
               AwyFConceedOvs2[0].append(AwOvers[7][1])
               AwyFConceedOvs2[1].append(len(rfdA))
               AwyFConceedOvs2[2].append(t)
               AwyFConceedOvs2[3].append("AwayConceed1stcHlvGoal2")
               AwyFConceedOvs2[4].append("AwayGamesPlayed")  
          #Away Conceed 1stHalf over 2.5
          if len(rfdA) - AwOvers[7][2] <= 1:          
               AwyFConceedOvs3[0].append(AwOvers[7][2])
               AwyFConceedOvs3[1].append(len(rfdA))
               AwyFConceedOvs3[2].append(t)
               AwyFConceedOvs3[3].append("AwayConceed1stHlvGoal3")
               AwyFConceedOvs3[4].append("AwayGamesPlayed") 
#=====================================================================================================#
          #Away SecHalf under 0.5
          if len(rfdA) - AwOvers[4][0] <= 1:          
               AwySOvs[0].append(AwOvers[4][0])
               AwySOvs[1].append(len(rfdA))
               AwySOvs[2].append(t)
               AwySOvs[3].append("AwayOverSecHlvGoal")
               AwySOvs[4].append("AwayGamesPlayed")
     #Away SecHalf under 1.5
          if len(rfdA) - AwOvers[4][1] <= 5:         
               AwySOvs1[0].append(AwOvers[4][1])
               AwySOvs1[1].append(len(rfdA))
               AwySOvs1[2].append(t)
               AwySOvs1[3].append("AwayOverSecHlv1Goal")
               AwySOvs1[4].append("AwayGamesPlayed")  
          #Away SecHalf under 2.5
          if len(rfdA) - AwOvers[4][2] <= 7:          
               AwySOvs2[0].append(AwOvers[4][2])
               AwySOvs2[1].append(len(rfdA))
               AwySOvs2[2].append(t)
               AwySOvs2[3].append("AwayOverSecHlv2Goal")
               AwySOvs2[4].append("AwayGamesPlayed") 
#=====================================================================================================#


          #Away FirstHalf over 0.5
          if len(rfdA) - AwOvers[2][0] <= 3:          
               AwyFOvs[0].append(AwOvers[2][0])
               AwyFOvs[1].append(len(rfdA))
               AwyFOvs[2].append(t)
               AwyFOvs[3].append("AwayOverFirstHlvGoal")
               AwyFOvs[4].append("AwayGamesPlayed")
     #Away FirstHalf over 1.5
          if len(rfdA) - AwOvers[2][1] <= 3:          
               AwyFOvs1[0].append(AwOvers[2][1])
               AwyFOvs1[1].append(len(rfdA))
               AwyFOvs1[2].append(t)
               AwyFOvs1[3].append("AwayOverFirstHlv1Goal")
               AwyFOvs1[4].append("AwayGamesPlayed")  
          #Away FirstHalf over 2.5
          if len(rfdA) - AwOvers[2][2] <= 3:          
               AwyFOvs2[0].append(AwOvers[2][2])
               AwyFOvs2[1].append(len(rfdA))
               AwyFOvs2[2].append(t)
               AwyFOvs2[3].append("AwayOverFirstHlv2Goal")
               AwyFOvs2[4].append("AwayGamesPlayed") 
#=====================================================================================================#
          #Away FirstHalf over 0.5
     if len(rfdA) - AwOvers[2][0] <= 3:          
          AwyFOvs[0].append(AwOvers[2][0])
          AwyFOvs[1].append(len(rfdA))
          AwyFOvs[2].append(t)
          AwyFOvs[3].append("AwayOverFirstHlvGoal")
          AwyFOvs[4].append("AwayGamesPlayed")
    #Away FirstHalf over 1.5
     if len(rfdA) - AwOvers[2][1] <= 3:          
          AwyFOvs1[0].append(AwOvers[2][1])
          AwyFOvs1[1].append(len(rfdA))
          AwyFOvs1[2].append(t)
          AwyFOvs1[3].append("AwayOverFirstHlv1Goal")
          AwyFOvs1[4].append("AwayGamesPlayed")  
     #Away FirstHalf over 2.5
     if len(rfdA) - AwOvers[2][2] <= 3:          
          AwyFOvs2[0].append(AwOvers[2][2])
          AwyFOvs2[1].append(len(rfdA))
          AwyFOvs2[2].append(t)
          AwyFOvs2[3].append("AwayOverFirstHlv2Goal")
          AwyFOvs2[4].append("AwayGamesPlayed") 
#=====================================================================================================#
      #Away FirstHalf under 0.5
     if len(rfdA) - AwOvers[3][0] <= 1:          
          AwyFUnder[0].append(AwOvers[3][0])
          AwyFUnder[1].append(len(rfdA))
          AwyFUnder[2].append(t)
          AwyFUnder[3].append("AwayUnderFirstHlvGoal")
          AwyFUnder[4].append("AwayGamesPlayed")
    #Away FirstHalf under 1.5
     if len(rfdA) - AwOvers[3][1] <= 1:          
          AwyFUnder1[0].append(AwOvers[3][1])
          AwyFUnder1[1].append(len(rfdA))
          AwyFUnder1[2].append(t)
          AwyFUnder1[3].append("AwayUnderFirstHlv1Goal")
          AwyFUnder1[4].append("AwayGamesPlayed")  
     #Away FirstHalf under 2.5
     if len(rfdA) - AwOvers[3][2] <= 1:          
          AwyFUnder2[0].append(AwOvers[3][2])
          AwyFUnder2[1].append(len(rfdA))
          AwyFUnder2[2].append(t)
          AwyFUnder2[3].append("AwayUnderFirstHlv2Goal")
          AwyFUnder2[4].append("AwayGamesPlayed") 
#=====================================================================================================#    
  
     #Away under 0.5
     if len(rfdA) - AwOvers[1][0] <= 1:          
          AwyUnder[0].append(AwOvers[1][0])
          AwyUnder[1].append(len(rfdA))
          AwyUnder[2].append(t)
          AwyUnder[3].append("AwayUnder1Goal")
          AwyUnder[4].append("AwayGamesPlayed")
    #Away under 1.5
     if len(rfdA) - AwOvers[1][1] <= 1:          
          AwyUnder2[0].append(AwOvers[1][1])
          AwyUnder2[1].append(len(rfdA))
          AwyUnder2[2].append(t)
          AwyUnder2[3].append("AwayUnder2Goal")
          AwyUnder2[4].append("AwayGamesPlayed")  
     #Away under 2.5
     if len(rfdA) - AwOvers[1][2] <= 1:          
          AwyUnder3[0].append(AwOvers[1][2])
          AwyUnder3[1].append(len(rfdA))
          AwyUnder3[2].append(t)
          AwyUnder3[3].append("AwayUnder3Goal")
          AwyUnder3[4].append("AwayGamesPlayed") 
     #Away Under 3.5
     if len(rfdA) - AwOvers[1][3] <= 1:          
          AwyUnder4[0].append(AwOvers[1][3])
          AwyUnder4[1].append(len(rfdA))
          AwyUnder4[2].append(t)
          AwyUnder4[3].append("AwayUnder4Goal")
          AwyUnder4[4].append("AwayGamesPlayed")
    #Away under 4.5
     if len(rfdA) - AwOvers[1][4] <= 1:          
          AwyUnder5[0].append(AwOvers[1][4])
          AwyUnder5[1].append(len(rfdA))
          AwyUnder5[2].append(t)
          AwyUnder5[3].append("AwayUnder5Goal")
          AwyUnder5[4].append("AwayGamesPlayed")  
#=====================================================================================================#    
     #Away over 0.5
     if len(rfdA) - AwOvers[0][0] <= 1:          
          AwyOvs[0].append(AwOvers[0][0])
          AwyOvs[1].append(len(rfdA))
          AwyOvs[2].append(t)
          AwyOvs[3].append("AwayGoal")
          AwyOvs[4].append("AwayGamesPlayed")
    #Away over 1.5
     if len(rfdA) - AwOvers[0][1] <= 1:          
          AwyOvs1[0].append(AwOvers[0][1])
          AwyOvs1[1].append(len(rfdA))
          AwyOvs1[2].append(t)
          AwyOvs1[3].append("AwayGoalover2")
          AwyOvs1[4].append("AwayGamesPlayed")  
     #Away over 2.5
     if len(rfdA) - AwOvers[0][2] <= 1:          
          AwyOvs2[0].append(AwOvers[0][2])
          AwyOvs2[1].append(len(rfdA))
          AwyOvs2[2].append(t)
          AwyOvs2[3].append("AwayGoalover3")
          AwyOvs2[4].append("AwayGamesPlayed")    
#=====================================================================================================#
     #AwayBTS Yes
     if len(rfdA) - hBTS[0] <= 1:          
          Bts[0].append(hBTS[0])
          Bts[1].append(len(rfdA))
          Bts[2].append(t)
          Bts[3].append("AwayBTS")
          Bts[4].append("AwayGamesPlayed")
#=====================================================================================================#
     #FullTimeOver 1.5
     if len(rfdA) == afullTimeOver[0][1]:          
          FullTimeOvers[0].append(afullTimeOver[0][1])
          FullTimeOvers[1].append(len(rfdA))
          FullTimeOvers[2].append(t)
          FullTimeOvers[3].append("AwayFullTimeOver1")
          FullTimeOvers[4].append("AwayGamesPlayed")
          
          #FullTimeOver 2.5
     if len(rfdA) - afullTimeOver[0][2] <= 1:          
          FullTimeOvers2[0].append(afullTimeOver[0][2])
          FullTimeOvers2[1].append(len(rfdA))
          FullTimeOvers2[2].append(t)
          FullTimeOvers2[3].append("AwayFullTimeOver2")
          FullTimeOvers2[4].append("AwayGamesPlayed")

          #FullTimeOver 3.5
     if len(rfdA) == afullTimeOver[0][3]:          
          FullTimeOvers3[0].append(afullTimeOver[0][3])
          FullTimeOvers3[1].append(len(rfdA))
          FullTimeOvers3[2].append(t)
          FullTimeOvers3[3].append("AwayFullTimeOver3")
          FullTimeOvers3[4].append("AwayGamesPlayed")

          #FullTimeOver 4.5
     if len(rfdA) == afullTimeOver[0][4]:          
          FullTimeOvers4[0].append(afullTimeOver[0][4])
          FullTimeOvers4[1].append(len(rfdA))
          FullTimeOvers4[2].append(t)
          FullTimeOvers4[3].append("AwayFullTimeOver4")
          FullTimeOvers4[4].append("AwayGamesPlayed")
#=====================================================================================================#
  
  Info=(FullTimeOvers,FullTimeOvers2,FullTimeOvers3,FullTimeOvers4,Bts,AwyOvs,AwyOvs1,AwyOvs2,AwyUnder3,AwyUnder4,AwyFUnder,AwyFUnder1,AwyFUnder2,AwyFOvs,AwyFOvs1,AwyFOvs2,AwySOvs2,AwySOvs1,AwySOvs,AwySConceedOvs,AwyFConceedOvs3,AwyFConceedOvs2)
  
  createReport(Info,pd)

     

def homeFilter(data):
  for ee in sql_data[0]:
   if ee[3] in teams:
    t = ee[3]
   else:
    teams.append(ee[3])

awayFilter(sql_data)

