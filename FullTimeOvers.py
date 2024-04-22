import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb


#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\odds.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from EplBetOdds"
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

AwyOvs= ([],[],[],[],[])
AwySConceedOvs= ([],[],[],[],[])
AwySConceedOvs2= ([],[],[],[],[])
AwySConceedOvs3= ([],[],[],[],[])

HomeSConceedOvs = ([],[],[],[],[])
HomeSConceedOvs2= ([],[],[],[],[])
HomeSConceedOvs3= ([],[],[],[],[])

AwyFirstfailtToConceedOvs= ([],[],[],[],[])
AwyFirstfailtToConceedOvs2= ([],[],[],[],[])
AwyFirstfailtToConceedOvs3= ([],[],[],[],[])

AwySfailtToConceedOvs= ([],[],[],[],[])
AwySfailtToConceedOvs2= ([],[],[],[],[])
AwySfailtToConceedOvs3= ([],[],[],[],[])

HomeSfailtToConceedOvs= ([],[],[],[],[])
HomeSfailtToConceedOvs2= ([],[],[],[],[])
HomeSfailtToConceedOvs3= ([],[],[],[],[])

HomeFConceedOvs = ([],[],[],[],[])
HomeFConceedOvs2 = ([],[],[],[],[])
HomeFConceedOvs3 = ([],[],[],[],[])

AwyFConceedOvs = ([],[],[],[],[])
AwyFConceedOvs2 = ([],[],[],[],[])
AwyFConceedOvs3 = ([],[],[],[],[])


AwySConceedOvs = ([],[],[],[],[])
AwySConceedOvs2 = ([],[],[],[],[])
AwySConceedOvs3 = ([],[],[],[],[])

AwyFfailtToConceedOvs = ([],[],[],[],[])
AwyFfailtToConceedOvs2 = ([],[],[],[],[])
AwyFfailtToConceedOvs3 = ([],[],[],[],[])

AwySOvs= ([],[],[],[],[])
AwySOvs1= ([],[],[],[],[])
AwySOvs2= ([],[],[],[],[])

HomeSOvs= ([],[],[],[],[])
HomeSOvs1= ([],[],[],[],[])
HomeSOvs2= ([],[],[],[],[])

HomeFrstunder = ([],[],[],[],[])
HomeFrstunder1= ([],[],[],[],[])
HomeFrstunder2= ([],[],[],[],[])

HomefrstOver1 = ([],[],[],[],[])
HomefrstOver2= ([],[],[],[],[])
HomefrstOver3= ([],[],[],[],[])

HomefullOver1 = ([],[],[],[],[])
HomefullOver2= ([],[],[],[],[])
HomefullOver3= ([],[],[],[],[])
HomefullOver4= ([],[],[],[],[])

HomefullUnder1 = ([],[],[],[],[])
HomefullUnder2= ([],[],[],[],[])
HomefullUnder3= ([],[],[],[],[])
HomefullUnder4= ([],[],[],[],[])

HomeFixUnder1 = ([],[],[],[],[])
HomeFixUnder2= ([],[],[],[],[])
HomeFixUnder3= ([],[],[],[],[])
HomeFixUnder4= ([],[],[],[],[])

HomeFixOver1 = ([],[],[],[],[])
HomeFixOver2= ([],[],[],[],[])
HomeFixOver3= ([],[],[],[],[])
HomeFixOver4= ([],[],[],[],[])

HomeSunder= ([],[],[],[],[])
HomeSunder1= ([],[],[],[],[])
HomeSunder2= ([],[],[],[],[])

AwySUnder= ([],[],[],[],[])
AwySUnder1= ([],[],[],[],[])
AwySUnder2= ([],[],[],[],[])

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
H2ndHWins = ([],[],[],[],[])
HWins = ([],[],[],[],[])
a2ndHFailureWins= ([],[],[],[],[])
H2ndHFailureWins = ([],[],[],[],[])
aHalftimeWins= ([],[],[],[],[])
aFuilureToWins= ([],[],[],[],[])
aFuilureToHalfWins = ([],[],[],[],[])
HFuilureToHalfWins = ([],[],[],[],[])
HFuilureToWins = ([],[],[],[],[])
HHalftimeWins = ([],[],[],[],[])

HomeFirstfailtToConceedOvs = ([],[],[],[],[])
HomeFirstfailtToConceedOvs2 = ([],[],[],[],[])
HomeFirstfailtToConceedOvs3 = ([],[],[],[],[])

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
     if len(rfdA) - aWinLose[10] <= 1:          
          a2ndHWins[0].append(aWinLose[10])
          a2ndHWins[1].append(len(rfdA))
          a2ndHWins[2].append(t)
          a2ndHWins[3].append("Away2ndHalfWins")
          a2ndHWins[4].append("AwayGamesPlayed")
#Away 2ndHalf failuir to win
     if len(rfdA) - aWinLose[9] <= 1:          
          a2ndHFailureWins[0].append(aWinLose[9])
          a2ndHFailureWins[1].append(len(rfdA))
          a2ndHFailureWins[2].append(t)
          a2ndHFailureWins[3].append("AwayHalftimeFailToWin")
          a2ndHFailureWins[4].append("AwayGamesPlayed")  

#========================================================================#
#Away halftime wins
     if len(rfdA) - aWinLose[6] <= 1:          
          aHalftimeWins[0].append(aWinLose[6])
          aHalftimeWins[1].append(len(rfdA))
          aHalftimeWins[2].append(t)
          aHalftimeWins[3].append("AwayHalfWins")
          aHalftimeWins[4].append("AwayGamesPlayed")
#Away halftime failuir to win
     if len(rfdA) - aWinLose[5] <= 1:          
          aFuilureToHalfWins[0].append(aWinLose[5])
          aFuilureToHalfWins[1].append(len(rfdA))
          aFuilureToHalfWins[2].append(t)
          aFuilureToHalfWins[3].append("AwayHalftimeFailToWin")
          aFuilureToHalfWins[4].append("AwayGamesPlayed")

#=============================================================================#
#Away wins
     if len(rfdA) - aWinLose[2] <= 1:          
          aWins[0].append(aWinLose[2])
          aWins[1].append(len(rfdA))
          aWins[2].append(t)
          aWins[3].append("AwayWins")
          aWins[4].append("AwayGamesPlayed")
#Away failuir to win
     if len(rfdA) - aWinLose[1] <= 1:          
          aFuilureToWins[0].append(aWinLose[1])
          aFuilureToWins[1].append(len(rfdA))
          aFuilureToWins[2].append(t)
          aFuilureToWins[3].append("AwayFailToWin")
          aFuilureToWins[4].append("AwayGamesPlayed")


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
#Away SecHalf over 0.5
     if len(rfdA) - AwOvers[4][0] <= 1:          
          AwySOvs[0].append(AwOvers[4][0])
          AwySOvs[1].append(len(rfdA))
          AwySOvs[2].append(t)
          AwySOvs[3].append("AwayOverSecHlvGoal")
          AwySOvs[4].append("AwayGamesPlayed")
#Away SecHalf over 1.5
     if len(rfdA) - AwOvers[4][1] <= 5:         
          AwySOvs1[0].append(AwOvers[4][1])
          AwySOvs1[1].append(len(rfdA))
          AwySOvs1[2].append(t)
          AwySOvs1[3].append("AwayOverSecHlv1Goal")
          AwySOvs1[4].append("AwayGamesPlayed")  
#Away SecHalf over 2.5
     if len(rfdA) - AwOvers[4][2] <= 7:          
          AwySOvs2[0].append(AwOvers[4][2])
          AwySOvs2[1].append(len(rfdA))
          AwySOvs2[2].append(t)
          AwySOvs2[3].append("AwayOverSecHlv2Goal")
          AwySOvs2[4].append("AwayGamesPlayed") 


#=====================================================================================================#
#Away SecHalf under 0.5
     if len(rfdA) - AwOvers[5][0] <= 1:          
          AwySUnder[0].append(AwOvers[5][0])
          AwySUnder[1].append(len(rfdA))
          AwySUnder[2].append(t)
          AwySUnder[3].append("AwayUnderSecHlvGoal")
          AwySUnder[4].append("AwayGamesPlayed")
#Away SecHalf under 1.5
     if len(rfdA) - AwOvers[5][1] <= 5:         
          AwySUnder1[0].append(AwOvers[5][1])
          AwySUnder1[1].append(len(rfdA))
          AwySUnder1[2].append(t)
          AwySUnder1[3].append("AwayUnderSecHlv1Goal")
          AwySUnder1[4].append("AwayGamesPlayed")  
#Away SecHalf under 2.5
     if len(rfdA) - AwOvers[5][2] <= 7:          
          AwySUnder2[0].append(AwOvers[5][2])
          AwySUnder2[1].append(len(rfdA))
          AwySUnder2[2].append(t)
          AwySUnder2[3].append("AwayUnderSecHlv2Goal")
          AwySUnder2[4].append("AwayGamesPlayed") 
               
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
#Info=(FullTimeOvers,FullTimeOvers2,FullTimeOvers3,FullTimeOvers4,Bts,AwyOvs,AwyOvs1,AwyOvs2,AwyUnder3,AwySUnder,AwySUnder1,AwySUnder2,AwyUnder4,AwyUnder5,AwyFUnder,AwyFUnder1,AwyFUnder2,AwyFOvs,AwyFOvs1,AwyFOvs2,AwySOvs2,AwySOvs1,AwySOvs,AwySConceedOvs,AwyFConceedOvs,AwyFConceedOvs3,AwyFConceedOvs2,a2ndHWins,a2ndHFailureWins,aHalftimeWins,aFuilureToHalfWins,aWins,aFuilureToWins,AwyFirstfailtToConceedOvs,AwyFirstfailtToConceedOvs2,AwyFirstfailtToConceedOvs3,AwySfailtToConceedOvs3)
  
  
#createReport(Info,pd)

     

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
     HWinLose = BtOr.MatchRes(t,rfdA,"k",5)
     AwOvers = BtOr.OverUnderSeaon(t,rfdA,"k",5)
     HfullTimeOver = BtOr.FixOverUnders(t,rfdA,"k",5)
     #hBTS = BtOr.Bts(t,rfdA,"k",5)
#Home 2ndHalf wins
     if len(rfdA) - HWinLose[8] <= 1:          
          H2ndHWins[0].append(HWinLose[8])
          H2ndHWins[1].append(len(rfdA))
          H2ndHWins[2].append(t)
          H2ndHWins[3].append("Home2ndHalfWins")
          H2ndHWins[4].append("HomeGamesPlayed")
#Home 2ndHalf failuir to win
     if len(rfdA) - HWinLose[11] <= 1:          
          H2ndHFailureWins[0].append(HWinLose[11])
          H2ndHFailureWins[1].append(len(rfdA))
          H2ndHFailureWins[2].append(t)
          H2ndHFailureWins[3].append("Home2ndHalfFailToWin")
          H2ndHFailureWins[4].append("HomeGamesPlayed") 
#========================================================================#
#Home halftime wins
     if len(rfdA) - HWinLose[4] <= 1:          
          HHalftimeWins[0].append(HWinLose[4])
          HHalftimeWins[1].append(len(rfdA))
          HHalftimeWins[2].append(t)
          HHalftimeWins[3].append("HomeHalfTimeWins")
          HHalftimeWins[4].append("HomeGamesPlayed") 
#Home halftime failuir to win
     if len(rfdA) - HWinLose[7] <= 1:          
          HFuilureToHalfWins[0].append(HWinLose[7])
          HFuilureToHalfWins[1].append(len(rfdA))
          HFuilureToHalfWins[2].append(t)
          HFuilureToHalfWins[3].append("HomeHalftimeFailToWin")
          HFuilureToHalfWins[4].append("HomeGamesPlayed")
#=============================================================================#
#Home wins
     if len(rfdA) - HWinLose[0] <= 1:          
          HWins[0].append(HWinLose[0])
          HWins[1].append(len(rfdA))
          HWins[2].append(t)
          HWins[3].append("HomeWins")
          HWins[4].append("HomeGamesPlayed")  
#Home failuir to win
     if len(rfdA) - HWinLose[3] <= 1:          
          HFuilureToWins[0].append(HWinLose[3])
          HFuilureToWins[1].append(len(rfdA))
          HFuilureToWins[2].append(t)
          HFuilureToWins[3].append("HomeFailToWin")
          HFuilureToWins[4].append("HomeGamesPlayed")  
#===============================================================================#

#Home Failed to Conceed 1stHalf over 0.5
     if len(rfdA) - AwOvers[10][0] <= 1:          
          HomeFirstfailtToConceedOvs[0].append(AwOvers[10][0])
          HomeFirstfailtToConceedOvs[1].append(len(rfdA))
          HomeFirstfailtToConceedOvs[2].append(t)
          HomeFirstfailtToConceedOvs[3].append("HomeFailConceed1stHlvGoal")
          HomeFirstfailtToConceedOvs[4].append("HomeGamesPlayed")   
#Home Failed to Conceed 1stHalf over 1.5
     if len(rfdA) - AwOvers[10][1] <= 1:          
          HomeFirstfailtToConceedOvs2[0].append(AwOvers[10][1])
          HomeFirstfailtToConceedOvs2[1].append(len(rfdA))
          HomeFirstfailtToConceedOvs2[2].append(t)
          HomeFirstfailtToConceedOvs2[3].append("HomeFailConceed1stHlv2Goal")
          HomeFirstfailtToConceedOvs2[4].append("HomeGamesPlayed") 
#Home Failed to Conceed 1stHalf over 2.5
     if len(rfdA) - AwOvers[10][2] <= 1:          
          HomeFirstfailtToConceedOvs3[0].append(AwOvers[10][2])
          HomeFirstfailtToConceedOvs3[1].append(len(rfdA))
          HomeFirstfailtToConceedOvs3[2].append(t)
          HomeFirstfailtToConceedOvs3[3].append("HomeFailConceed1stHlv3Goal")
          HomeFirstfailtToConceedOvs3[4].append("HomeGamesPlayed")   
#===============================================================================#
#Home Failed to Conceed SecHalf over 0.5
     if len(rfdA) - AwOvers[12][0] <= 1:          
          HomeSfailtToConceedOvs[0].append(AwOvers[12][0])
          HomeSfailtToConceedOvs[1].append(len(rfdA))
          HomeSfailtToConceedOvs[2].append(t)
          HomeSfailtToConceedOvs[3].append("HomeFailConceedSecHlvGoal")
          HomeSfailtToConceedOvs[4].append("HomeGamesPlayed")
#Home Failed to Conceed SecHalf over 1.5
     if len(rfdA) - AwOvers[12][1] <= 1:          
          HomeSfailtToConceedOvs2[0].append(AwOvers[12][1])
          HomeSfailtToConceedOvs2[1].append(len(rfdA))
          HomeSfailtToConceedOvs2[2].append(t)
          HomeSfailtToConceedOvs2[3].append("HomeFailConceedSecHlv2Goal")
          HomeSfailtToConceedOvs2[4].append("HomeGamesPlayed")
#Home Failed to Conceed SecHalf over 2.5
     if len(rfdA) - AwOvers[12][2] <= 1:          
          HomeSfailtToConceedOvs3[0].append(AwOvers[12][2])
          HomeSfailtToConceedOvs3[1].append(len(rfdA))
          HomeSfailtToConceedOvs3[2].append(t)
          HomeSfailtToConceedOvs3[3].append("HomeFailConceedSecHlv3Goal")
          HomeSfailtToConceedOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed SecHalf over 0.5
     if len(rfdA) - AwOvers[13][0] <= 1:          
          HomeSConceedOvs[0].append(AwOvers[13][0])
          HomeSConceedOvs[1].append(len(rfdA))
          HomeSConceedOvs[2].append(t)
          HomeSConceedOvs[3].append("HomeConceedSecHlvGoal")
          HomeSConceedOvs[4].append("HomeGamesPlayed")
#Home Conceed SecHalf over 1.5
     if len(rfdA) - AwOvers[13][1] <= 1:          
          HomeSConceedOvs2[0].append(AwOvers[13][1])
          HomeSConceedOvs2[1].append(len(rfdA))
          HomeSConceedOvs2[2].append(t)
          HomeSConceedOvs2[3].append("HomeConceedSecHlv2Goal")
          HomeSConceedOvs2[4].append("HomeGamesPlayed")
#Home Conceed SecHalf over 2.5
     if len(rfdA) - AwOvers[13][2] <= 1:          
          HomeSConceedOvs3[0].append(AwOvers[13][2])
          HomeSConceedOvs3[1].append(len(rfdA))
          HomeSConceedOvs3[2].append(t)
          HomeSConceedOvs3[3].append("HomeConceedSecHlv3Goal")
          HomeSConceedOvs3[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed 1stHalf over 0.5
     if len(rfdA) - AwOvers[11][0] <= 1:          
          HomeFConceedOvs[0].append(AwOvers[11][0])
          HomeFConceedOvs[1].append(len(rfdA))
          HomeFConceedOvs[2].append(t)
          HomeFConceedOvs[3].append("HomeConceed1stHlvGoal")
          HomeFConceedOvs[4].append("HomeGamesPlayed")
#Home Conceed 1stHalf over 1.5
     if len(rfdA) - AwOvers[11][1] <= 1:          
          HomeFConceedOvs2[0].append(AwOvers[11][1])
          HomeFConceedOvs2[1].append(len(rfdA))
          HomeFConceedOvs2[2].append(t)
          HomeFConceedOvs2[3].append("HomeConceed1stHlv2Goal")
          HomeFConceedOvs2[4].append("HomeGamesPlayed")
#Home Conceed 1stHalf over 2.5
     if len(rfdA) - AwOvers[11][2] <= 1:          
          HomeFConceedOvs3[0].append(AwOvers[11][2])
          HomeFConceedOvs3[1].append(len(rfdA))
          HomeFConceedOvs3[2].append(t)
          HomeFConceedOvs3[3].append("HomeConceed1stHlv3Goal")
          HomeFConceedOvs3[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home SecHalf over 0.5
     if len(rfdA) - AwOvers[14][0] <= 1:          
          HomeSOvs[0].append(AwOvers[14][0])
          HomeSOvs[1].append(len(rfdA))
          HomeSOvs[2].append(t)
          HomeSOvs[3].append("HomeOverSecHlvGoal")
          HomeSOvs[4].append("HomeGamesPlayed")

#Home SecHalf over 1.5
     if len(rfdA) - AwOvers[14][1] <= 1:          
          HomeSOvs1[0].append(AwOvers[14][0])
          HomeSOvs1[1].append(len(rfdA))
          HomeSOvs1[2].append(t)
          HomeSOvs1[3].append("HomeOverSecHlv1Goal")
          HomeSOvs1[4].append("HomeGamesPlayed")

#Home SecHalf over 2.5
     if len(rfdA) - AwOvers[14][2] <= 1:          
          HomeSOvs2[0].append(AwOvers[14][0])
          HomeSOvs2[1].append(len(rfdA))
          HomeSOvs2[2].append(t)
          HomeSOvs2[3].append("HomeOverSecHlv2Goal")
          HomeSOvs2[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home SecHalf under 0.5
     if len(rfdA) - AwOvers[15][0] <= 1:          
          HomeSunder[0].append(AwOvers[15][0])
          HomeSunder[1].append(len(rfdA))
          HomeSunder[2].append(t)
          HomeSunder[3].append("HomeUnderSecHlvGoal")
          HomeSunder[4].append("HomeGamesPlayed")

#Home SecHalf under 1.5
     if len(rfdA) - AwOvers[15][1] <= 1:          
          HomeSunder1[0].append(AwOvers[15][1])
          HomeSunder1[1].append(len(rfdA))
          HomeSunder1[2].append(t)
          HomeSunder1[3].append("HomeUnderSecHlv2Goal")
          HomeSunder1[4].append("HomeGamesPlayed")

#Home SecHalf under 2.5
     if len(rfdA) - AwOvers[15][2] <= 1:          
          HomeSunder2[0].append(AwOvers[15][1])
          HomeSunder2[1].append(len(rfdA))
          HomeSunder2[2].append(t)
          HomeSunder2[3].append("HomeUnderSecHlv3Goal")
          HomeSunder2[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home 1stHalf under 0.5
     if len(rfdA) - AwOvers[16][0] <= 1:          
          HomeFrstunder[0].append(AwOvers[16][0])
          HomeFrstunder[1].append(len(rfdA))
          HomeFrstunder[2].append(t)
          HomeFrstunder[3].append("HomeUnderFirstHlvGoal")
          HomeFrstunder[4].append("HomeGamesPlayed")

#Home 1stHalf under 1.5
     if len(rfdA) - AwOvers[16][1] <= 1:          
          HomeFrstunder1[0].append(AwOvers[16][1])
          HomeFrstunder1[1].append(len(rfdA))
          HomeFrstunder1[2].append(t)
          HomeFrstunder1[3].append("HomeUnderFirstHlv2Goal")
          HomeFrstunder1[4].append("HomeGamesPlayed")

#Home 1stHalf under 2.5
     if len(rfdA) - AwOvers[16][2] <= 1:          
          HomeFrstunder2[0].append(AwOvers[16][2])
          HomeFrstunder2[1].append(len(rfdA))
          HomeFrstunder2[2].append(t)
          HomeFrstunder2[3].append("HomeUnderFirstHlv3Goal")
          HomeFrstunder2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home 1stHalf over 0.5
     if len(rfdA) - AwOvers[17][0] <= 1:          
          HomefrstOver1[0].append(AwOvers[17][0])
          HomefrstOver1[1].append(len(rfdA))
          HomefrstOver1[2].append(t)
          HomefrstOver1[3].append("HomeOverFirstHlvGoal")
          HomefrstOver1[4].append("HomeGamesPlayed")

#Home 1stHalf over 1.5
     if len(rfdA) - AwOvers[17][1] <= 1:          
          HomefrstOver2[0].append(AwOvers[17][1])
          HomefrstOver2[1].append(len(rfdA))
          HomefrstOver2[2].append(t)
          HomefrstOver2[3].append("HomeOverFirstHlv2Goal")
          HomefrstOver2[4].append("HomeGamesPlayed")

#Home 1stHalf over 2.5
     if len(rfdA) - AwOvers[17][2] <= 1:          
          HomefrstOver3[0].append(AwOvers[17][2])
          HomefrstOver3[1].append(len(rfdA))
          HomefrstOver3[2].append(t)
          HomefrstOver3[3].append("HomeOverFirstHlv3Goal")
          HomefrstOver3[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home fulltime over 0.5
     if len(rfdA) - AwOvers[0][0] <= 5:          
          HomefullOver1[0].append(AwOvers[0][0])
          HomefullOver1[1].append(len(rfdA))
          HomefullOver1[2].append(t)
          HomefullOver1[3].append("HomeOverHlvGoal")
          HomefullOver1[4].append("HomeGamesPlayed")
#Home fulltime over 1.5
     if len(rfdA) - AwOvers[0][1] <= 1:          
          HomefullOver2[0].append(AwOvers[0][1])
          HomefullOver2[1].append(len(rfdA))
          HomefullOver2[2].append(t)
          HomefullOver2[3].append("HomeOverHlv1Goal")
          HomefullOver2[4].append("HomeGamesPlayed")

#Home fulltime over 2.5
     if len(rfdA) - AwOvers[0][2] <= 1:          
          HomefullOver3[0].append(AwOvers[0][2])
          HomefullOver3[1].append(len(rfdA))
          HomefullOver3[2].append(t)
          HomefullOver3[3].append("HomeOverHlv2Goal")
          HomefullOver3[4].append("HomeGamesPlayed")

#Home fulltime over 3.5
     if len(rfdA) - AwOvers[0][3] <= 1:          
          HomefullOver4[0].append(AwOvers[0][3])
          HomefullOver4[1].append(len(rfdA))
          HomefullOver4[2].append(t)
          HomefullOver4[3].append("HomeOverHlv3Goal")
          HomefullOver4[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home fulltime Under 0.5
     if len(rfdA) - AwOvers[1][0] <= 1:          
          HomefullUnder1[0].append(AwOvers[1][0])
          HomefullUnder1[1].append(len(rfdA))
          HomefullUnder1[2].append(t)
          HomefullUnder1[3].append("HomeUnderHlvGoal")
          HomefullUnder1[4].append("HomeGamesPlayed")
#Home fulltime Under 1.5
     if len(rfdA) - AwOvers[1][1] <= 1:          
          HomefullUnder2[0].append(AwOvers[1][1])
          HomefullUnder2[1].append(len(rfdA))
          HomefullUnder2[2].append(t)
          HomefullUnder2[3].append("HomeUnderHlv1Goal")
          HomefullUnder2[4].append("HomeGamesPlayed")

#Home fulltime Under 2.5
     if len(rfdA) - AwOvers[1][2] <= 1:          
          HomefullUnder3[0].append(AwOvers[1][2])
          HomefullUnder3[1].append(len(rfdA))
          HomefullUnder3[2].append(t)
          HomefullUnder3[3].append("HomeUnderHlv2Goal")
          HomefullUnder3[4].append("HomeGamesPlayed")

#Home fulltime Under 3.5
     if len(rfdA) - AwOvers[1][3] <= 1:          
          HomefullUnder4[0].append(AwOvers[1][3])
          HomefullUnder4[1].append(len(rfdA))
          HomefullUnder4[2].append(t)
          HomefullUnder4[3].append("HomeUnderHlv3Goal")
          HomefullUnder4[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home Fix fulltime Under 0.5
     if len(rfdA) - HfullTimeOver[1][0] <= 1:          
          HomeFixOver1[0].append(HfullTimeOver[1][0])
          HomeFixOver1[1].append(len(rfdA))
          HomeFixOver1[2].append(t)
          HomeFixOver1[3].append("HomeFixtureNoGoal")
          HomeFixOver1[4].append("HomeGamesPlayed")
#Home Fix fulltime Under 1.5
     if len(rfdA) - HfullTimeOver[1][1] <= 1:          
          HomeFixOver2[0].append(HfullTimeOver[1][1])
          HomeFixOver2[1].append(len(rfdA))
          HomeFixOver2[2].append(t)
          HomeFixOver2[3].append("HomeFixtureUnde1Goal")
          HomeFixOver2[4].append("HomeGamesPlayed")

#Home Fix fulltime Under 2.5
     if len(rfdA) - HfullTimeOver[1][2] <= 1:          
          HomeFixOver3[0].append(HfullTimeOver[1][2])
          HomeFixOver3[1].append(len(rfdA))
          HomeFixOver3[2].append(t)
          HomeFixOver3[3].append("HomeFixtureUnder2Goal")
          HomeFixOver3[4].append("HomeGamesPlayed")

#Home Fix fulltime Under 3.5
     if len(rfdA) - HfullTimeOver[1][3] <= 1:          
          HomeFixOver4[0].append(HfullTimeOver[1][3])
          HomeFixOver4[1].append(len(rfdA))
          HomeFixOver4[2].append(t)
          HomeFixOver4[3].append("HomeFixtureUnder3Goal")
          HomeFixOver4[4].append("HomeGamesPlayed")

  Info=(HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullUnder1,HomefullUnder2,HomefullUnder3,HomefullUnder4,H2ndHWins,H2ndHFailureWins,HHalftimeWins,HFuilureToHalfWins,HWins,HFuilureToWins,HomeFirstfailtToConceedOvs,HomeFirstfailtToConceedOvs2,HomeFirstfailtToConceedOvs3,HomeSfailtToConceedOvs,HomeSfailtToConceedOvs2,HomeSfailtToConceedOvs3,HomeSfailtToConceedOvs2,HomeSfailtToConceedOvs,HomeSConceedOvs,HomeSConceedOvs2,HomeSConceedOvs3,HomeFConceedOvs3,HomeFConceedOvs2,HomeFConceedOvs,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeSunder,HomeSunder1,HomeSunder2,HomeFrstunder2,HomeFrstunder1,HomeFrstunder,HomefrstOver3,HomefrstOver2,HomefrstOver1)
  createReport(Info,pd)
homeFilter(sql_data)
#awayFilter(sql_data)

