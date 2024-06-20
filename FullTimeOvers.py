import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb
from SecLPAnylaysis import SlPA


#engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from serieBB"
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

HomeFFOvs = ([],[],[],[],[])
HomeFFOvs2= ([],[],[],[],[])
HomeFFOvs3= ([],[],[],[],[])

ConceedFSoutcome = ([],[],[],[],[])
ConceedFSoutcomeOne = ([],[],[],[],[])

HomeallBTS = ([],[],[],[],[])
HomeFrstHBTS = ([],[],[],[],[])
HomeSecndHBTS = ([],[],[],[],[])

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
HomeFConceedOvs4 = ([],[],[],[],[])
HomeFConceedOvs5 = ([],[],[],[],[])

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

HomeSFOvs3 = ([],[],[],[],[])
HomeSFOvs2 = ([],[],[],[],[])
HomeSFOvs = ([],[],[],[],[])

HomeFrstunder = ([],[],[],[],[])
HomeFrstunder1= ([],[],[],[],[])
HomeFrstunder2= ([],[],[],[],[])

HomeHalftimeOverZ = ([],[],[],[],[])
HomefrstOver1 = ([],[],[],[],[])
HomefrstOver2= ([],[],[],[],[])
HomefrstOver3= ([],[],[],[],[])

HomefullOver1 = ([],[],[],[],[])
HomefullOver2= ([],[],[],[],[])
HomefullOver3= ([],[],[],[],[])
HomefullOver4= ([],[],[],[],[])
HomefullOver5 = ([],[],[],[],[])

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
HomeFixOver5= ([],[],[],[],[])

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
H2ndHLose = ([],[],[],[],[])
HSWinsDraw= ([],[],[],[],[])
HWins = ([],[],[],[],[])
HLose = ([],[],[],[],[])
HWinsDraw = ([],[],[],[],[])
HHWinsDraw = ([],[],[],[],[])
a2ndHFailureWins= ([],[],[],[],[])
H2ndHFailureWins = ([],[],[],[],[])
aHalftimeWins= ([],[],[],[],[])
aFuilureToWins= ([],[],[],[],[])
aFuilureToHalfWins = ([],[],[],[],[])
HHalftimeLose = ([],[],[],[],[])
HFuilureToWins = ([],[],[],[],[])
HHalftimeWins = ([],[],[],[],[])

HomeHalftimeConceedOverZ = ([],[],[],[],[])
HomeHalftimeConceedOverZ2 = ([],[],[],[],[])
HomeHalftimeConceedOverZ3 = ([],[],[],[],[])

HomeSectimeConceedOverZ = ([],[],[],[],[])
HomeSectimeConceedOverZ2 = ([],[],[],[],[])
HomeSectimeConceedOverZ3 = ([],[],[],[],[])

FullTimeOvers= ([],[],[],[],[])
FullTimeOvers2= ([],[],[],[],[])
FullTimeOvers3= ([],[],[],[],[])
FullTimeOvers4= ([],[],[],[],[])


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
      


def awayFilter(data):
  for ee in sql_data[0]:
   if ee[4] in Ateams:
    t = ee[4]
   else:
    Ateams.append(ee[4])
  for w in Ateams:
   t = w
   occurence = 0
   if t in Ateam:
      occurence = 0
   else:
     rfdA = BtOr.refindedDatam(t,data,4)
     HWinLose = BtOr.MatchRes(t,rfdA,"b",6)
     AwOvers = BtOr.OverUnderSeaon(t,rfdA,"b",6)
     HfullTimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"over")
     HHalfimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"first")
     HsecHaTimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"sec")
     hFBTS  = BtOr.Bts(t,rfdA,"b",5,"over")
     hfirstBTS = BtOr.Bts(t,rfdA,"b",5,"first")
     hSecndBTS = BtOr.Bts(t,rfdA,"b",5,"sec")
     HmeConceedFulltime = BtOr.ConcededWholeSeaon(t,rfdA,"b",5)
     ConceedXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"k",5)

     #hBTS = BtOr.Bts(t,rfdA,"k",5)

#=====================================================================================================#
#Away Conceed Zero First Half/Second Half out
     if len(rfdA) - ConceedXnumFrstHalf[0] :          
          ConceedFSoutcome[0].append(str(ConceedXnumFrstHalf[0])+ "/" +str(ConceedXnumFrstHalf[5]))
          ConceedFSoutcome[1].append(len(rfdA))
          ConceedFSoutcome[2].append(t)
          ConceedFSoutcome[3].append("AwayConceedZeroFirstHSecHOut")
          ConceedFSoutcome[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Conceed One First Half/Second Half out
     if len(rfdA) - ConceedXnumFrstHalf[0] :          
          ConceedFSoutcomeOne[0].append(str(ConceedXnumFrstHalf[1])+ "/" +str(ConceedXnumFrstHalf[5]))
          ConceedFSoutcomeOne[1].append(len(rfdA))
          ConceedFSoutcomeOne[2].append(t)
          ConceedFSoutcomeOne[3].append("AwayConceedOneFirstHSecHOut")
          ConceedFSoutcomeOne[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fix fulltime over 0.5
     if len(rfdA) - HfullTimeOver[0][0] :          
          HomefullOver1[0].append(str(HfullTimeOver[0][0])+ "/" +str(HfullTimeOver[1][0]))
          HomefullOver1[1].append(len(rfdA))
          HomefullOver1[2].append(t)
          HomefullOver1[3].append("AwayFixtureFulltimeOverZ")
          HomefullOver1[4].append("AwayGamesPlayed")
#Away Fix fulltime over 1.5
     if len(rfdA) - HfullTimeOver[0][1] :          
          HomefullOver2[0].append(str(HfullTimeOver[0][1])+ "/" +str(HfullTimeOver[1][1]))
          HomefullOver2[1].append(len(rfdA))
          HomefullOver2[2].append(t)
          HomefullOver2[3].append("AwayFixtureFulltimeOver1")
          HomefullOver2[4].append("AwayGamesPlayed")
#Home Fix fulltime over 2.5
     if len(rfdA) - HfullTimeOver[0][2] :          
          HomefullOver3[0].append(str(HfullTimeOver[0][2])+ "/" +str(HfullTimeOver[1][2]))
          HomefullOver3[1].append(len(rfdA))
          HomefullOver3[2].append(t)
          HomefullOver3[3].append("AwayFixtureFulltimeOver2")
          HomefullOver3[4].append("AwayGamesPlayed")

#Away Fix  fulltime over 3.5
     if len(rfdA) - HfullTimeOver[0][3] :          
          HomefullOver4[0].append(str(HfullTimeOver[0][3])+ "/" +str(HfullTimeOver[1][3]))
          HomefullOver4[1].append(len(rfdA))
          HomefullOver4[2].append(t)
          HomefullOver4[3].append("AwayFixtureFulltimeOver3")
          HomefullOver4[4].append("AwayGamesPlayed")
#Away Fix  fulltime over 4.5
     if len(rfdA) - HfullTimeOver[0][4] :          
          HomefullOver5[0].append(str(HfullTimeOver[0][4])+ "/" +str(HfullTimeOver[1][4]))
          HomefullOver5[1].append(len(rfdA))
          HomefullOver5[2].append(t)
          HomefullOver5[3].append("AwayFixtureFulltimeOver4")
          HomefullOver5[4].append("AwayGamesPlayed")

#=============================================================================#
#Away wins
     if len(rfdA) - HWinLose[0]:          
          HWins[0].append(str(HWinLose[0]) + "/" + str(HWinLose[15]))
          HWins[1].append(len(rfdA))
          HWins[2].append(t)
          HWins[3].append("AwayFulltimeWins")
          HWins[4].append("AwayGamesPlayed")
#=============================================================================#
#Away Faulure to Lose/Win Draw
     if len(rfdA) - HWinLose[3] :          
          HWinsDraw[0].append(str(HWinLose[3]) + "/" + str(HWinLose[0]))
          HWinsDraw[1].append(len(rfdA))
          HWinsDraw[2].append(t)
          HWinsDraw[3].append("AwayFulltimeWinDraw")
          HWinsDraw[4].append("AwayGamesPlayed") 
#========================================================================#
#Away halftime wins   
     if len(rfdA) - HWinLose[6] :          
          HHalftimeWins[0].append(str(HWinLose[6])+ "/" +str(HWinLose[4]))
          HHalftimeWins[1].append(len(rfdA))
          HHalftimeWins[2].append(t)
          HHalftimeWins[3].append("AwayHalfTimeWins")
          HHalftimeWins[4].append("AwayGamesPlayed") 
#========================================================================#
#Away halftime  Win Draw/Faulure to Lose
     if len(rfdA) - HWinLose[16] :          
          HHWinsDraw[0].append(str(HWinLose[16]) + "/" + str(HWinLose[4]))
          HHWinsDraw[1].append(len(rfdA))
          HHWinsDraw[2].append(t)
          HHWinsDraw[3].append("AwayHalftimeWinDraw")
          HHWinsDraw[4].append("AwayGamesPlayed") 
#========================================================================#
#Away Secondhalf Win Draw/Faulure to Lose
     if len(rfdA) - HWinLose[13] :          
          HSWinsDraw[0].append(str(HWinLose[13]) + "/" + str(HWinLose[10]))
          HSWinsDraw[1].append(len(rfdA))
          HSWinsDraw[2].append(t)
          HSWinsDraw[3].append("AwaySecondHalfWinDraw")
          HSWinsDraw[4].append("AwayGamesPlayed") 
#========================================================================#
#Away Secondhalf Win 
     if len(rfdA) - HWinLose[12] :          
          H2ndHWins[0].append(str(HWinLose[12])+ "/" +str(HWinLose[10]))
          H2ndHWins[1].append(len(rfdA))
          H2ndHWins[2].append(t)
          H2ndHWins[3].append("AwaySecondHalfWin")
          H2ndHWins[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away First Half over 0.5
     if len(rfdA) - AwOvers[2][0]:          
          HomeHalftimeOverZ[0].append(str(AwOvers[2][0])+ "/" +str(AwOvers[3][0]))
          HomeHalftimeOverZ[1].append(len(rfdA))
          HomeHalftimeOverZ[2].append(t)
          HomeHalftimeOverZ[3].append("AwayFirstHalfOverZ")
          HomeHalftimeOverZ[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away First Half over 1.5
     if len(rfdA) - AwOvers[2][1]:          
          HomefrstOver1[0].append(str(AwOvers[2][1])+ "/" +str(AwOvers[3][1]))
          HomefrstOver1[1].append(len(rfdA))
          HomefrstOver1[2].append(t)
          HomefrstOver1[3].append("AwayFirstHalfOver1")
          HomefrstOver1[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away First Half over 2.5
     if len(rfdA) - AwOvers[2][2] :          
          HomefrstOver2[0].append(str(AwOvers[2][2])+ "/" + str(AwOvers[3][2]))
          HomefrstOver2[1].append(len(rfdA))
          HomefrstOver2[2].append(t)
          HomefrstOver2[3].append("AwayFirstHalfOver2")
          HomefrstOver2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half over 0.5
     if len(rfdA) - AwOvers[4][0]:          
          HomeSOvs[0].append(str(AwOvers[4][0])+ "/" +str(AwOvers[5][0]))
          HomeSOvs[1].append(len(rfdA))
          HomeSOvs[2].append(t)
          HomeSOvs[3].append("AwaySecHalfOverZ")
          HomeSOvs[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half over 1.5
     if len(rfdA) - AwOvers[4][1] :          
          HomeSOvs1[0].append(str(AwOvers[4][1])+ "/" +str(AwOvers[5][1]))
          HomeSOvs1[1].append(len(rfdA))
          HomeSOvs1[2].append(t)
          HomeSOvs1[3].append("AwaySecHalfOver1")
          HomeSOvs1[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half over 2.5
     if len(rfdA) - AwOvers[4][2]:          
          HomeSOvs2[0].append(str(AwOvers[4][2]) + "/" + str(AwOvers[5][2]))
          HomeSOvs2[1].append(len(rfdA))
          HomeSOvs2[2].append(t)
          HomeSOvs2[3].append("AwaySecHalfOver2")
          HomeSOvs2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away First Half Fixture over 0.5
     if len(rfdA) - HHalfimeOver[0][0]:          
          HomeFFOvs[0].append(str(HHalfimeOver[0][0]) + "/" +str(HHalfimeOver[1][0]))
          HomeFFOvs[1].append(len(rfdA))
          HomeFFOvs[2].append(t)
          HomeFFOvs[3].append("AwayFixtureFirstHlfOverZ")
          HomeFFOvs[4].append("AwayGamesPlayed")
#===============================================================================#
#Away First Half Fixture over 1.5
     if len(rfdA) - HHalfimeOver[0][1]:          
          HomeFFOvs2[0].append(str(HHalfimeOver[0][1]) + "/" + str(HHalfimeOver[1][1]))
          HomeFFOvs2[1].append(len(rfdA))
          HomeFFOvs2[2].append(t)
          HomeFFOvs2[3].append("AwayFixtureFirstHalfOver1")
          HomeFFOvs2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away First Half Fixture over 2.5
     if len(rfdA) - HHalfimeOver[0][2]:          
          HomeFFOvs3[0].append(str(HHalfimeOver[0][2]) + "/" + str(HHalfimeOver[1][2]))
          HomeFFOvs3[1].append(len(rfdA))
          HomeFFOvs3[2].append(t)
          HomeFFOvs3[3].append("AwayFixtureFirstHalfOver2" )
          HomeFFOvs3[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half Fixture over 0.5
     if len(rfdA) - HsecHaTimeOver[0][0] :          
          HomeSFOvs[0].append(str(HsecHaTimeOver[0][0]) + "/" + str(HsecHaTimeOver[1][0]))
          HomeSFOvs[1].append(len(rfdA))
          HomeSFOvs[2].append(t)
          HomeSFOvs[3].append("AwayFixtureSecondHalfOverZ")
          HomeSFOvs[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half Fixture over 1.5
     if len(rfdA) - HsecHaTimeOver[0][1] :          
          HomeSFOvs2[0].append(str(HsecHaTimeOver[0][1]) + "/" + str(HsecHaTimeOver[1][1]))
          HomeSFOvs2[1].append(len(rfdA))
          HomeSFOvs2[2].append(t)
          HomeSFOvs2[3].append("AwayFixtureSecondHalfOver1")
          HomeSFOvs2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half Fixture over 2.5
     if len(rfdA) - HsecHaTimeOver[0][2] :          
          HomeSFOvs3[0].append(str(HsecHaTimeOver[0][2])  + "/" + str(HsecHaTimeOver[1][2]))
          HomeSFOvs3[1].append(len(rfdA))
          HomeSFOvs3[2].append(t)
          HomeSFOvs3[3].append("AwayFixtureSecondHalfOver2")
          HomeSFOvs3[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Overall Fixture BTS
     if len(rfdA) - hFBTS[0] :          
          HomeallBTS[0].append(str(hFBTS[0]) + "/" + str(hFBTS[1]))
          HomeallBTS[1].append(len(rfdA))
          HomeallBTS[2].append(t)
          HomeallBTS[3].append("AwayFixtureBTS")
          HomeallBTS[4].append("AwayGamesPlayed")
#===============================================================================#
#Away First Half BTS
     if len(rfdA) - hfirstBTS[0] :          
          HomeFrstHBTS[0].append(str(hfirstBTS[0]) + "/" + str(hfirstBTS[1]))
          HomeFrstHBTS[1].append(len(rfdA))
          HomeFrstHBTS[2].append(t)
          HomeFrstHBTS[3].append("AwayFirstHalfBTS")
          HomeFrstHBTS[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Second Half BTS
     if len(rfdA) - hSecndBTS[0] :          
          HomeSecndHBTS[0].append(str(hSecndBTS[0]) + "/" + str(hSecndBTS[1]))
          HomeSecndHBTS[1].append(len(rfdA))
          HomeSecndHBTS[2].append(t)
          HomeSecndHBTS[3].append("AwaySecondHalfBTS")
          HomeSecndHBTS[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed 1 Fulltime
     if len(rfdA) - HmeConceedFulltime[0] :          
          HomeFConceedOvs[0].append(str(HmeConceedFulltime[0]) + "/" + str(HmeConceedFulltime[1]))
          HomeFConceedOvs[1].append(len(rfdA))
          HomeFConceedOvs[2].append(t)
          HomeFConceedOvs[3].append("AwayConceedFulltime1")
          HomeFConceedOvs[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed 2 Fulltime
     if len(rfdA) - HmeConceedFulltime[2] :          
          HomeFConceedOvs2[0].append(str(HmeConceedFulltime[2]) + "/" + str(HmeConceedFulltime[3]))
          HomeFConceedOvs2[1].append(len(rfdA))
          HomeFConceedOvs2[2].append(t)
          HomeFConceedOvs2[3].append("AwayConceedFulltime2")
          HomeFConceedOvs2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed 3 Fulltime
     if len(rfdA) - HmeConceedFulltime[4] :          
          HomeFConceedOvs3[0].append(str(HmeConceedFulltime[4]) + "/" + str(HmeConceedFulltime[5]))
          HomeFConceedOvs3[1].append(len(rfdA))
          HomeFConceedOvs3[2].append(t)
          HomeFConceedOvs3[3].append("AwayConceedFulltime3")
          HomeFConceedOvs3[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed 4 Fulltime
     if len(rfdA) - HmeConceedFulltime[6] :          
          HomeFConceedOvs4[0].append(str(HmeConceedFulltime[6]) + "/" + str(HmeConceedFulltime[7]))
          HomeFConceedOvs4[1].append(len(rfdA))
          HomeFConceedOvs4[2].append(t)
          HomeFConceedOvs4[3].append("AwayConceedFulltime4")
          HomeFConceedOvs4[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed 5 Fulltime
     if len(rfdA) - HmeConceedFulltime[8] :          
          HomeFConceedOvs5[0].append(str(HmeConceedFulltime[8]) + "/" + str(HmeConceedFulltime[9]))
          HomeFConceedOvs5[1].append(len(rfdA))
          HomeFConceedOvs5[2].append(t)
          HomeFConceedOvs5[3].append("AwayConceedFulltime5")
          HomeFConceedOvs5[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Score 1 
     if len(rfdA) - AwOvers[18][0] :          
          HomeFixOver1[0].append(str(AwOvers[18][0]) + "/" + str(AwOvers[19][0]))
          HomeFixOver1[1].append(len(rfdA))
          HomeFixOver1[2].append(t)
          HomeFixOver1[3].append("AwayOverZero")
          HomeFixOver1[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Score 2 
     if len(rfdA) - AwOvers[18][1] :          
          HomeFixOver2[0].append(str(AwOvers[18][1]) + "/" + str(AwOvers[19][1]))
          HomeFixOver2[1].append(len(rfdA))
          HomeFixOver2[2].append(t)
          HomeFixOver2[3].append("AwayOver1")
          HomeFixOver2[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Score 3 
     if len(rfdA) - AwOvers[18][2] :          
          HomeFixOver3[0].append(str(AwOvers[18][2]) + "/" + str(AwOvers[19][2]))
          HomeFixOver3[1].append(len(rfdA))
          HomeFixOver3[2].append(t)
          HomeFixOver3[3].append("AwayOver2")
          HomeFixOver3[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Score 4 
     if len(rfdA) - AwOvers[18][3] :          
          HomeFixOver4[0].append(str(AwOvers[18][3]) + "/" + str(AwOvers[19][3]))
          HomeFixOver4[1].append(len(rfdA))
          HomeFixOver4[2].append(t)
          HomeFixOver4[3].append("AwayOver3")
          HomeFixOver4[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Score 5 
     if len(rfdA) - AwOvers[18][4] :          
          HomeFixOver5[0].append(str(AwOvers[18][4]) + "/" + str(AwOvers[19][4]))
          HomeFixOver5[1].append(len(rfdA))
          HomeFixOver5[2].append(t)
          HomeFixOver5[3].append("AwayOver4")
          HomeFixOver5[4].append("AwayGamesPlayed")
#===============================================================================#
#Away Conceed First Half over 0.5
     if len(rfdA) - AwOvers[17][0]:          
          HomeHalftimeConceedOverZ[0].append(str(AwOvers[17][0])+ "/" +str(AwOvers[16][0]))
          HomeHalftimeConceedOverZ[1].append(len(rfdA))
          HomeHalftimeConceedOverZ[2].append(t)
          HomeHalftimeConceedOverZ[3].append("AwayFirstHalfConceedOverZ")
          HomeHalftimeConceedOverZ[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away Conceed First Half over 1.5
     if len(rfdA) - AwOvers[17][1]:          
          HomeHalftimeConceedOverZ2[0].append(str(AwOvers[17][1])+ "/" +str(AwOvers[16][1]))
          HomeHalftimeConceedOverZ2[1].append(len(rfdA))
          HomeHalftimeConceedOverZ2[2].append(t)
          HomeHalftimeConceedOverZ2[3].append("AwayFirstHalfConceedOver1")
          HomeHalftimeConceedOverZ2[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away Conceed First Half over 2.5
     if len(rfdA) - AwOvers[17][2]:          
          HomeHalftimeConceedOverZ3[0].append(str(AwOvers[17][2])+ "/" +str(AwOvers[16][2]))
          HomeHalftimeConceedOverZ3[1].append(len(rfdA))
          HomeHalftimeConceedOverZ3[2].append(t)
          HomeHalftimeConceedOverZ3[3].append("AwayFirstHalfConceedOver2")
          HomeHalftimeConceedOverZ3[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away Conceed Second Half over 0.5
     if len(rfdA) - AwOvers[14][0]:          
          HomeSectimeConceedOverZ[0].append(str(AwOvers[14][0])+ "/" +str(AwOvers[15][0]))
          HomeSectimeConceedOverZ[1].append(len(rfdA))
          HomeSectimeConceedOverZ[2].append(t)
          HomeSectimeConceedOverZ[3].append("AwaySecondHalfConceedOverZ")
          HomeSectimeConceedOverZ[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away Conceed Second Half over 1.5
     if len(rfdA) - AwOvers[14][1]:          
          HomeSectimeConceedOverZ2[0].append(str(AwOvers[14][1])+ "/" +str(AwOvers[15][1]))
          HomeSectimeConceedOverZ2[1].append(len(rfdA))
          HomeSectimeConceedOverZ2[2].append(t)
          HomeSectimeConceedOverZ2[3].append("AwaySecondHalfConceedOver1")
          HomeSectimeConceedOverZ2[4].append("AwayGamesPlayed") 
#===============================================================================#
#Away Conceed Second Half over 2.5
     if len(rfdA) - AwOvers[14][2]:          
          HomeSectimeConceedOverZ3[0].append(str(AwOvers[14][2])+ "/" +str(AwOvers[15][2]))
          HomeSectimeConceedOverZ3[1].append(len(rfdA))
          HomeSectimeConceedOverZ3[2].append(t)
          HomeSectimeConceedOverZ3[3].append("AwaySecondHalfConceedOver2")
          HomeSectimeConceedOverZ3[4].append("AwayGamesPlayed") 



#=====================================================================================================#
#Info=(FullTimeOvers,FullTimeOvers2,FullTimeOvers3,FullTimeOvers4,Bts,AwyOvs,AwyOvs1,AwyOvs2,AwyUnder3,AwySUnder,AwySUnder1,AwySUnder2,AwyUnder4,AwyUnder5,AwyFUnder,AwyFUnder1,AwyFUnder2,AwyFOvs,AwyFOvs1,AwyFOvs2,AwySOvs2,AwySOvs1,AwySOvs,AwySConceedOvs,AwyFConceedOvs,AwyFConceedOvs3,AwyFConceedOvs2,a2ndHWins,a2ndHFailureWins,aHalftimeWins,aFuilureToHalfWins,aWins,aFuilureToWins,AwyFirstfailtToConceedOvs,AwyFirstfailtToConceedOvs2,AwyFirstfailtToConceedOvs3,AwySfailtToConceedOvs3)
#awayFilter(sql_data)
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
     HfullTimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"over")
     HHalfimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"first")
     HsecHaTimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"sec")
     hFBTS  = BtOr.Bts(t,rfdA,"k",5,"over")
     hfirstBTS = BtOr.Bts(t,rfdA,"k",5,"first")
     hSecndBTS = BtOr.Bts(t,rfdA,"k",5,"sec")
     HmeConceedFulltime = BtOr.ConcededWholeSeaon(t,rfdA,"k",6)
     ConceedXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"k",5)
     #hBTS = BtOr.Bts(t,rfdA,"k",5)



#=====================================================================================================#
#Home Fix fulltime over 0.5
     if len(rfdA) - HfullTimeOver[0][0] :          
          HomefullOver1[0].append(str(HfullTimeOver[0][0])+ "/" +str(HfullTimeOver[1][0]))
          HomefullOver1[1].append(len(rfdA))
          HomefullOver1[2].append(t)
          HomefullOver1[3].append("HomeFixtureFulltimeOverZ")
          HomefullOver1[4].append("HomeGamesPlayed")
#Home Fix fulltime over 1.5
     if len(rfdA) - HfullTimeOver[0][1] :          
          HomefullOver2[0].append(str(HfullTimeOver[0][1])+ "/" +str(HfullTimeOver[1][1]))
          HomefullOver2[1].append(len(rfdA))
          HomefullOver2[2].append(t)
          HomefullOver2[3].append("HomeFixtureFulltimeOver1")
          HomefullOver2[4].append("HomeGamesPlayed")

#Home Fix fulltime over 2.5
     if len(rfdA) - HfullTimeOver[0][2] :          
          HomefullOver3[0].append(str(HfullTimeOver[0][2])+ "/" +str(HfullTimeOver[1][2]))
          HomefullOver3[1].append(len(rfdA))
          HomefullOver3[2].append(t)
          HomefullOver3[3].append("HomeFixtureFulltimeOver2")
          HomefullOver3[4].append("HomeGamesPlayed")

#Home Fix  fulltime over 3.5
     if len(rfdA) - HfullTimeOver[0][3] :          
          HomefullOver4[0].append(str(HfullTimeOver[0][3])+ "/" +str(HfullTimeOver[1][3]))
          HomefullOver4[1].append(len(rfdA))
          HomefullOver4[2].append(t)
          HomefullOver4[3].append("HomeFixtureFulltimeOver3")
          HomefullOver4[4].append("HomeGamesPlayed")
#Home Fix  fulltime over 4.5
     if len(rfdA) - HfullTimeOver[0][3] :          
          HomefullOver5[0].append(str(HfullTimeOver[0][4])+ "/" +str(HfullTimeOver[1][4]))
          HomefullOver5[1].append(len(rfdA))
          HomefullOver5[2].append(t)
          HomefullOver5[3].append("HomeFixtureFulltimeOver4")
          HomefullOver5[4].append("HomeGamesPlayed")
#=============================================================================#
#Home wins
     if len(rfdA) - HWinLose[0]:          
          HWins[0].append(str(HWinLose[0]) + "/" + str(HWinLose[15]))
          HWins[1].append(len(rfdA))
          HWins[2].append(t)
          HWins[3].append("HomeFulltimeWins")
          HWins[4].append("HomeGamesPlayed")


#=============================================================================#
#Home Faulure to Lose/Win Draw
     if len(rfdA) - HWinLose[12] :          
          HWinsDraw[0].append(str(HWinLose[14]) + "/" + str(HWinLose[2]))
          HWinsDraw[1].append(len(rfdA))
          HWinsDraw[2].append(t)
          HWinsDraw[3].append("HomeFulltimeWinDraw")
          HWinsDraw[4].append("HomeGamesPlayed")    

#========================================================================#
#Home halftime wins
     if len(rfdA) - HWinLose[4] :          
          HHalftimeWins[0].append(str(HWinLose[4])+ "/" +str(HWinLose[7]))
          HHalftimeWins[1].append(len(rfdA))
          HHalftimeWins[2].append(t)
          HHalftimeWins[3].append("HomeHalfTimeWins")
          HHalftimeWins[4].append("HomeGamesPlayed")

#========================================================================#
#Home halftime  Win Draw/Faulure to Lose
     if len(rfdA) - HWinLose[8] :          
          HHWinsDraw[0].append(str(HWinLose[8]) + "/" + str(HWinLose[6]))
          HHWinsDraw[1].append(len(rfdA))
          HHWinsDraw[2].append(t)
          HHWinsDraw[3].append("HomeHalftimeWinDraw")
          HHWinsDraw[4].append("HomeGamesPlayed") 
#========================================================================#
#Home Secondhalf Win Draw/Faulure to Lose
     if len(rfdA) - HWinLose[10] :          
          HSWinsDraw[0].append(str(HWinLose[10]) + "/" + str(HWinLose[14]))
          HSWinsDraw[1].append(len(rfdA))
          HSWinsDraw[2].append(t)
          HSWinsDraw[3].append("HomeSecondHalfWinDraw")
          HSWinsDraw[4].append("HomeGamesPlayed") 
#========================================================================#
#Home Secondhalf Win 
     if len(rfdA) - HWinLose[10] :          
          H2ndHWins[0].append(str(HWinLose[11])+ "/" +str(HWinLose[14]))
          H2ndHWins[1].append(len(rfdA))
          H2ndHWins[2].append(t)
          H2ndHWins[3].append("HomeSecondHalfWin")
          H2ndHWins[4].append("HomeGamesPlayed") 


#===============================================================================#
#Home First Half over 0.5
     if len(rfdA) - AwOvers[17][0]:          
          HomeHalftimeOverZ[0].append(str(AwOvers[17][0])+ "/" +str(AwOvers[16][0]))
          HomeHalftimeOverZ[1].append(len(rfdA))
          HomeHalftimeOverZ[2].append(t)
          HomeHalftimeOverZ[3].append("HomeFirstHalfOverZ")
          HomeHalftimeOverZ[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half over 1.5
     if len(rfdA) - AwOvers[17][1]:          
          HomefrstOver1[0].append(str(AwOvers[17][1])+ "/" +str(AwOvers[16][1]))
          HomefrstOver1[1].append(len(rfdA))
          HomefrstOver1[2].append(t)
          HomefrstOver1[3].append("HomeFirstHalfOver1")
          HomefrstOver1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half over 2.5
     if len(rfdA) - AwOvers[17][2] :          
          HomefrstOver2[0].append(str(AwOvers[17][2])+ "/" + str(AwOvers[16][2]))
          HomefrstOver2[1].append(len(rfdA))
          HomefrstOver2[2].append(t)
          HomefrstOver2[3].append("HomeFirstHalfOver2")
          HomefrstOver2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 0.5
     if len(rfdA) - AwOvers[14][0]:          
          HomeSOvs[0].append(str(AwOvers[14][0])+ "/" +str(AwOvers[15][0]))
          HomeSOvs[1].append(len(rfdA))
          HomeSOvs[2].append(t)
          HomeSOvs[3].append("HomeSecHalfOverZ")
          HomeSOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 1.5
     if len(rfdA) - AwOvers[14][1] :          
          HomeSOvs1[0].append(str(AwOvers[14][1])+ "/" +str(AwOvers[15][1]))
          HomeSOvs1[1].append(len(rfdA))
          HomeSOvs1[2].append(t)
          HomeSOvs1[3].append("HomeSecHalfOver1")
          HomeSOvs1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 2.5
     if len(rfdA) - AwOvers[14][2]:          
          HomeSOvs2[0].append(str(AwOvers[14][2]) + "/" + str(AwOvers[15][2]))
          HomeSOvs2[1].append(len(rfdA))
          HomeSOvs2[2].append(t)
          HomeSOvs2[3].append("HomeSecHalfOver2")
          HomeSOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 0.5
     if len(rfdA) - HHalfimeOver[0][0]:          
          HomeFFOvs[0].append(str(HHalfimeOver[0][0]) + "/" +str(HHalfimeOver[1][0]))
          HomeFFOvs[1].append(len(rfdA))
          HomeFFOvs[2].append(t)
          HomeFFOvs[3].append("HomeFixtureFirstHalfOverZ")
          HomeFFOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 1.5
     if len(rfdA) - HHalfimeOver[0][1]:          
          HomeFFOvs2[0].append(str(HHalfimeOver[0][1]) + "/" + str(HHalfimeOver[1][1]))
          HomeFFOvs2[1].append(len(rfdA))
          HomeFFOvs2[2].append(t)
          HomeFFOvs2[3].append("HomeFixtureFirstHalfOver1")
          HomeFFOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 2.5
     if len(rfdA) - HHalfimeOver[0][2]:          
          HomeFFOvs3[0].append(str(HHalfimeOver[0][2]) + "/" + str(HHalfimeOver[1][2]))
          HomeFFOvs3[1].append(len(rfdA))
          HomeFFOvs3[2].append(t)
          HomeFFOvs3[3].append("HomeFixtureFirstHalfOver2" )
          HomeFFOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 0.5
     if len(rfdA) - HsecHaTimeOver[0][0] :          
          HomeSFOvs[0].append(str(HsecHaTimeOver[0][0]) + "/" + str(HsecHaTimeOver[1][0]))
          HomeSFOvs[1].append(len(rfdA))
          HomeSFOvs[2].append(t)
          HomeSFOvs[3].append("HomeFixtureSecondHalfOverZ")
          HomeSFOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 1.5
     if len(rfdA) - HsecHaTimeOver[0][1] :          
          HomeSFOvs2[0].append(str(HsecHaTimeOver[0][1]) + "/" + str(HsecHaTimeOver[1][1]))
          HomeSFOvs2[1].append(len(rfdA))
          HomeSFOvs2[2].append(t)
          HomeSFOvs2[3].append("HomeFixtureSecondHalfOver1")
          HomeSFOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 2.5
     if len(rfdA) - HsecHaTimeOver[0][2] :          
          HomeSFOvs3[0].append(str(HsecHaTimeOver[0][2])  + "/" + str(HsecHaTimeOver[1][2]))
          HomeSFOvs3[1].append(len(rfdA))
          HomeSFOvs3[2].append(t)
          HomeSFOvs3[3].append("HomeFixtureSecondHalfOver2")
          HomeSFOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Overall Fixture BTS
     if len(rfdA) - hFBTS[0] :          
          HomeallBTS[0].append(str(hFBTS[0]) + "/" + str(hFBTS[1]))
          HomeallBTS[1].append(len(rfdA))
          HomeallBTS[2].append(t)
          HomeallBTS[3].append("HomeFixtureBTS")
          HomeallBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half BTS
     if len(rfdA) - hfirstBTS[0] :          
          HomeFrstHBTS[0].append(str(hfirstBTS[0]) + "/" + str(hfirstBTS[1]))
          HomeFrstHBTS[1].append(len(rfdA))
          HomeFrstHBTS[2].append(t)
          HomeFrstHBTS[3].append("HomeFirstHalfBTS")
          HomeFrstHBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half BTS
     if len(rfdA) - hSecndBTS[0] :          
          HomeSecndHBTS[0].append(str(hSecndBTS[0]) + "/" + str(hSecndBTS[1]))
          HomeSecndHBTS[1].append(len(rfdA))
          HomeSecndHBTS[2].append(t)
          HomeSecndHBTS[3].append("HomeSecondHalfBTS")
          HomeSecndHBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 1 Fulltime
     if len(rfdA) - HmeConceedFulltime[0] :          
          HomeFConceedOvs[0].append(str(HmeConceedFulltime[0]) + "/" + str(HmeConceedFulltime[1]))
          HomeFConceedOvs[1].append(len(rfdA))
          HomeFConceedOvs[2].append(t)
          HomeFConceedOvs[3].append("HomeConceedFulltime1")
          HomeFConceedOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 2 Fulltime
     if len(rfdA) - HmeConceedFulltime[2] :          
          HomeFConceedOvs2[0].append(str(HmeConceedFulltime[2]) + "/" + str(HmeConceedFulltime[3]))
          HomeFConceedOvs2[1].append(len(rfdA))
          HomeFConceedOvs2[2].append(t)
          HomeFConceedOvs2[3].append("HomeConceedFulltime2")
          HomeFConceedOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 3 Fulltime
     if len(rfdA) - HmeConceedFulltime[4] :          
          HomeFConceedOvs3[0].append(str(HmeConceedFulltime[4]) + "/" + str(HmeConceedFulltime[5]))
          HomeFConceedOvs3[1].append(len(rfdA))
          HomeFConceedOvs3[2].append(t)
          HomeFConceedOvs3[3].append("HomeConceedFulltime3")
          HomeFConceedOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 4 Fulltime
     if len(rfdA) - HmeConceedFulltime[6] :          
          HomeFConceedOvs4[0].append(str(HmeConceedFulltime[6]) + "/" + str(HmeConceedFulltime[7]))
          HomeFConceedOvs4[1].append(len(rfdA))
          HomeFConceedOvs4[2].append(t)
          HomeFConceedOvs4[3].append("HomeConceedFulltime4")
          HomeFConceedOvs4[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 5 Fulltime
     if len(rfdA) - HmeConceedFulltime[8] :          
          HomeFConceedOvs5[0].append(str(HmeConceedFulltime[8]) + "/" + str(HmeConceedFulltime[9]))
          HomeFConceedOvs5[1].append(len(rfdA))
          HomeFConceedOvs5[2].append(t)
          HomeFConceedOvs5[3].append("HomeConceedFulltime5")
          HomeFConceedOvs5[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 1 
     if len(rfdA) - AwOvers[0][0] :          
          HomeFixOver1[0].append(str(AwOvers[0][0]) + "/" + str(AwOvers[1][0]))
          HomeFixOver1[1].append(len(rfdA))
          HomeFixOver1[2].append(t)
          HomeFixOver1[3].append("HomeOverZero")
          HomeFixOver1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 2 
     if len(rfdA) - AwOvers[0][1] :          
          HomeFixOver2[0].append(str(AwOvers[0][1]) + "/" + str(AwOvers[1][1]))
          HomeFixOver2[1].append(len(rfdA))
          HomeFixOver2[2].append(t)
          HomeFixOver2[3].append("HomeOver1")
          HomeFixOver2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 3 
     if len(rfdA) - AwOvers[0][2] :          
          HomeFixOver3[0].append(str(AwOvers[0][2]) + "/" + str(AwOvers[1][2]))
          HomeFixOver3[1].append(len(rfdA))
          HomeFixOver3[2].append(t)
          HomeFixOver3[3].append("HomeOver2")
          HomeFixOver3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 4 
     if len(rfdA) - AwOvers[0][3] :          
          HomeFixOver4[0].append(str(AwOvers[0][3]) + "/" + str(AwOvers[1][3]))
          HomeFixOver4[1].append(len(rfdA))
          HomeFixOver4[2].append(t)
          HomeFixOver4[3].append("HomeOver3")
          HomeFixOver4[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 5 
     if len(rfdA) - AwOvers[0][3] :          
          HomeFixOver5[0].append(str(AwOvers[0][4]) + "/" + str(AwOvers[1][4]))
          HomeFixOver5[1].append(len(rfdA))
          HomeFixOver5[2].append(t)
          HomeFixOver5[3].append("HomeOver4")
          HomeFixOver5[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed First Half over 0.5
     if len(rfdA) - AwOvers[2][0]:          
          HomeHalftimeConceedOverZ[0].append(str(AwOvers[2][0])+ "/" +str(AwOvers[3][0]))
          HomeHalftimeConceedOverZ[1].append(len(rfdA))
          HomeHalftimeConceedOverZ[2].append(t)
          HomeHalftimeConceedOverZ[3].append("HomeFirstHalfConceedOverZ")
          HomeHalftimeConceedOverZ[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed First Half over 1.5
     if len(rfdA) - AwOvers[2][1]:          
          HomeHalftimeConceedOverZ2[0].append(str(AwOvers[2][1])+ "/" +str(AwOvers[3][1]))
          HomeHalftimeConceedOverZ2[1].append(len(rfdA))
          HomeHalftimeConceedOverZ2[2].append(t)
          HomeHalftimeConceedOverZ2[3].append("HomeFirstHalfConceedOver1")
          HomeHalftimeConceedOverZ2[4].append("AwayGamesPlayed") 
#===============================================================================#
#Home Conceed First Half over 2.5
     if len(rfdA) - AwOvers[2][2]:          
          HomeHalftimeConceedOverZ3[0].append(str(AwOvers[2][2])+ "/" +str(AwOvers[3][2]))
          HomeHalftimeConceedOverZ3[1].append(len(rfdA))
          HomeHalftimeConceedOverZ3[2].append(t)
          HomeHalftimeConceedOverZ3[3].append("HomeFirstHalfConceedOver2")
          HomeHalftimeConceedOverZ3[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 0.5
     if len(rfdA) - AwOvers[4][0]:          
          HomeSectimeConceedOverZ[0].append(str(AwOvers[4][0])+ "/" +str(AwOvers[5][0]))
          HomeSectimeConceedOverZ[1].append(len(rfdA))
          HomeSectimeConceedOverZ[2].append(t)
          HomeSectimeConceedOverZ[3].append("HomeSecondHalfConceedOverZ")
          HomeSectimeConceedOverZ[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 1.5
     if len(rfdA) - AwOvers[4][1]:          
          HomeSectimeConceedOverZ2[0].append(str(AwOvers[4][1])+ "/" +str(AwOvers[5][1]))
          HomeSectimeConceedOverZ2[1].append(len(rfdA))
          HomeSectimeConceedOverZ2[2].append(t)
          HomeSectimeConceedOverZ2[3].append("HomeSecondHalfConceedOver1")
          HomeSectimeConceedOverZ2[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 2.5
     if len(rfdA) - AwOvers[4][2]:          
          HomeSectimeConceedOverZ3[0].append(str(AwOvers[4][2])+ "/" +str(AwOvers[5][2]))
          HomeSectimeConceedOverZ3[1].append(len(rfdA))
          HomeSectimeConceedOverZ3[2].append(t)
          HomeSectimeConceedOverZ3[3].append("HomeSecondHalfConceedOver2")
          HomeSectimeConceedOverZ3[4].append("HomeGamesPlayed") 



  
#homeFilter(sql_data)
awayFilter(sql_data)
          #1             #2        #3             #4           #5           #6                 #7              #8                 #9             #10               #11         #12            #13            #14         #15      #16      #17       #18            #19       #20       #21          #22              #23            #24        #25      #26       #27       #28         #29       #30       #31         #32        #33       #34         #35          #36                 #37                     #38                       #39                      #40                        #41                    #42                                                                              
#Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ)
                      #1                #2
SecLayerInfor = (ConceedFSoutcome,ConceedFSoutcomeOne)
createReport(SecLayerInfor,pd)





