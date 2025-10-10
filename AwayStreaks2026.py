import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import numpy as np
from multiLayerPerceptron import mlp
from SecLPAnylaysis import SlPA

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\results2026.accdb')
cursor = conn.cursor()
insert_stmt2 = "select * from AlgeriaA25  union select * from Austria125 union select * from Austria225  union select * from AzerBaijan2025 union select * from belgiumJpl25 union select * from BoliviaPrem25 union select * from BulgariaPrem25 union select * from Bundas2Liga25 union select * from BundasLiga25 union select * from Bundes325 union select * from ColombiaPrem25 union select * from CroatiaA25 union select * from CSuper25 UNION select * from CzechB25 UNION select * from CyprusA25 UNION select * from DenmarkA25 UNION select * from DenmarkB25 UNION select * from EersteEredevisie25 UNION select * from EgyptA25 UNION select * from EngLeagua225 UNION select * from EngLeagua125 UNION select * from Epl25 UNION select * from EplChampionShip25 UNION select * from EredevisieTwede25 UNION select * from EstoniaPremB25 UNION select * from EstoniaPrem25 UNION select * from GEORGIAA25 UNION select * from GreeceA25 UNION select * from icelandBesta25 UNION select * from icelandDiv125 UNION select * from IndonesiaPrem25 UNION select * from IranPrem25 UNION select * from  irelandPrem25 UNION select * from irelandB25 UNION select * from IsraelA25 UNION select * from israelB25 UNION select * from JapanA25 UNION select * from  JapanB25 UNION select * from JordanPrem25 UNION select * from  LaLiga225 UNION Select * FROM LaLiga25 UNION Select * FROM LatviaPrem25 UNION Select * FROM Ligue1Fr25 UNION Select * FROM Ligue2Fr25 UNION Select * FROM MalaysiaPrem25 UNION Select * FROM NorwayA25 UNION Select * FROM NorwayB25 UNION Select * FROM PolandA25 UNION Select * FROM PolandB25" 

cursor.execute(insert_stmt2)
sql_data = pd.DataFrame(cursor.fetchall())
teamCount = 0
halftomeGap = 2

HomefullOver1 = ([],[],[],[],[])
HomefullOver2 = ([],[],[],[],[])
HomefullOver3 = ([],[],[],[],[])
HomefullOver4 = ([],[],[],[],[])

HomefullConceed1 = ([],[],[],[],[])
HomefullConceed2 = ([],[],[],[],[])
HomefullConceed3 = ([],[],[],[],[])
HomefullConceed4 = ([],[],[],[],[])

HomefullFixOver0 = ([],[],[],[],[])
HomefullFixOver1 = ([],[],[],[],[])
HomefullFixOver2 = ([],[],[],[],[])
HomefullFixOver3 = ([],[],[],[],[])
HomefullFixOver4 = ([],[],[],[],[])

HomefullFixWin = ([],[],[],[],[])
HomefullFixWinD = ([],[],[],[],[])
HomefullFixLoseD = ([],[],[],[],[])

HomefullHalfWin = ([],[],[],[],[])
HomefullHalfWinD = ([],[],[],[],[])

HomefullSecHalfWinD = ([],[],[],[],[])
HomefullSecHalfWin = ([],[],[],[],[])

HomefullFirstHalfOverZ = ([],[],[],[],[])
HomefullFirstHalfOver1 = ([],[],[],[],[])
HomefullFirstHalfOver2 = ([],[],[],[],[])


HomefullSecHalfOverZ = ([],[],[],[],[])
HomefullSecHalfOver1 = ([],[],[],[],[])
HomefullSecHalfOver2 = ([],[],[],[],[])

HomefullFirstHalfConceedOVZ = ([],[],[],[],[])
HomefullFirstHalfConceedOV1 = ([],[],[],[],[])
HomefullFirstHalfConceedOV2 = ([],[],[],[],[])

HomefullSecHalfConceedOVZ = ([],[],[],[],[])
HomefullSecHalfConceedOV1 = ([],[],[],[],[])
HomefullSecHalfConceedOV2 = ([],[],[],[],[])

HomefullFirstHalfFixtureOVZ = ([],[],[],[],[])
HomefullFirstHalfFixtureOV1 = ([],[],[],[],[])
HomefullFirstHalfFixtureOV2 = ([],[],[],[],[])

HomefullSecHalfFixtureOVZ = ([],[],[],[],[])
HomefullSecHalfFixtureOV1 = ([],[],[],[],[])
HomefullSecHalfFixtureOV2 = ([],[],[],[],[])



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
  df.to_excel('StreaksAwayinfo26.xlsx', sheet_name="Away", index=False)
  #for ee in data1:

def homeFilter(data):
  for ee in sql_data[0]:
   if ee[4] in teams:
    t = ee[4]
   else:
    teams.append(ee[4])

  for w in teams:
   t = w
   occurence = 0
   if t in Hteam:
      occurence = 0
   else:
     rfdA = BtOr.refindedDatam(t,data,4)
     streaksOver = BtOr.StreaksOverUnder(t,rfdA,"k",6,"over")
     streaksOver1 = BtOr.StreaksOverUnder1(t,rfdA,"k",6,"over")
     streaksOver2 = BtOr.StreaksOverUnder2(t,rfdA,"k",6,"over")
     streaksOver3 = BtOr.StreaksOverUnder3(t,rfdA,"k",6,"over")
     streaksOver4 = BtOr.StreaksConceed1(t,rfdA,"k",5,"over")
     streaksOver5 = BtOr.StreaksConceed2(t,rfdA,"k",5,"over")
     streaksOver6 = BtOr.StreaksConceed3(t,rfdA,"k",5,"over")
     streaksOver7 = BtOr.StreaksConceed4(t,rfdA,"k",5,"over")
     streaksOver8 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,0)
     streaksOver9 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,1)
     streaksOver10 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,2)
     streaksOver11 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,3)
     streaksOver12 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,4)
     streaksOver13 = BtOr.StreaksHomeFullWinLose(t,rfdA,"T",6,"over")
     streaksOver14 = BtOr.StreaksHomeFullWinDraw(t,rfdA,"T",6,"over")
     streaksOver15 = BtOr.StreaksHomeFullLoseDraw(t,rfdA,"T",6,"over")
     streaksOver16 = BtOr.StreaksHomeFullHalfWin(t,rfdA,"T",6,"over")
     streaksOver17 = BtOr.StreaksHomeFullHalfWinD(t,rfdA,"T",6,"over")
     streaksOver18 = BtOr.StreaksHomeSeconHalfWinD(t,rfdA,"T",6,"over")
     streaksOver19 = BtOr.StreaksHomeSeconHalfWin(t,rfdA,"T",6,"over")
     streaksOver20 = BtOr.StreaksHomeFirstHalf(t,rfdA,"T",6,0)
     streaksOver21 = BtOr.StreaksHomeFirstHalf(t,rfdA,"T",6,1)
     streaksOver22 = BtOr.StreaksHomeFirstHalf(t,rfdA,"T",6,2)
     streaksOver23 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",6,0)
     streaksOver24 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",6,1)
     streaksOver25 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",6,2)
     streaksOver26 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",7,0)
     streaksOver27 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",7,1)
     streaksOver28 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",7,2)
     streaksOver29 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",7,2)
     streaksOver30 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",7,1)
     streaksOver31 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",7,0)
     streaksOver32 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"T",6,0)
     streaksOver33 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"T",6,1)
     streaksOver34 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"T",6,2)
     streaksOver35 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"T",6,0)
     streaksOver36 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"T",6,1)
     streaksOver37 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"T",6,2)
     
    
     
#=====================================================================================================#
#Away Over  0.5 Streaks
            
     HomefullOver1[0].append(str(streaksOver[0])+ "/" +str(streaksOver[1]))
     HomefullOver1[1].append(len(rfdA))
     HomefullOver1[2].append(t)
     HomefullOver1[3].append("AwayOverZ")
     HomefullOver1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Over 1.5 Streaks
            
     HomefullOver2[0].append(str(streaksOver1[0])+ "/" +str(streaksOver1[1]))
     HomefullOver2[1].append(len(rfdA))
     HomefullOver2[2].append(t)
     HomefullOver2[3].append("AwayOver1")
     HomefullOver2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Over 2.5 Streaks
            
     HomefullOver3[0].append(str(streaksOver2[0])+ "/" +str(streaksOver2[1]))
     HomefullOver3[1].append(len(rfdA))
     HomefullOver3[2].append(t)
     HomefullOver3[3].append("AwayOver2")
     HomefullOver3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Over 3.5 Streaks
            
     HomefullOver4[0].append(str(streaksOver3[0])+ "/" +str(streaksOver3[1]))
     HomefullOver4[1].append(len(rfdA))
     HomefullOver4[2].append(t)
     HomefullOver4[3].append("AwayOver3")
     HomefullOver4[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Conceed 0.5 Streaks
            
     HomefullConceed1[0].append(str(streaksOver4[0])+ "/" +str(streaksOver4[1]))
     HomefullConceed1[1].append(len(rfdA))
     HomefullConceed1[2].append(t)
     HomefullConceed1[3].append("AwayConceed1")
     HomefullConceed1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Conceed 1.5 Streaks
            
     HomefullConceed2[0].append(str(streaksOver5[0])+ "/" +str(streaksOver5[1]))
     HomefullConceed2[1].append(len(rfdA))
     HomefullConceed2[2].append(t)
     HomefullConceed2[3].append("AwayConceed2")
     HomefullConceed2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Conceed 2.5 Streaks
            
     HomefullConceed3[0].append(str(streaksOver6[0])+ "/" +str(streaksOver6[1]))
     HomefullConceed3[1].append(len(rfdA))
     HomefullConceed3[2].append(t)
     HomefullConceed3[3].append("AwayConceed3")
     HomefullConceed3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Conceed 3.5 Streaks
            
     HomefullConceed4[0].append(str(streaksOver7[0])+ "/" +str(streaksOver7[1]))
     HomefullConceed4[1].append(len(rfdA))
     HomefullConceed4[2].append(t)
     HomefullConceed4[3].append("AwayConceed4")
     HomefullConceed4[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture over 0.5 Streaks
            
     HomefullFixOver0[0].append(str(streaksOver8[0])+ "/" +str(streaksOver8[1]))
     HomefullFixOver0[1].append(len(rfdA))
     HomefullFixOver0[2].append(t)
     HomefullFixOver0[3].append("AwayFixtureFulltimeOverZ")
     HomefullFixOver0[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture over 1.5 Streaks
            
     HomefullFixOver1[0].append(str(streaksOver9[0])+ "/" +str(streaksOver9[1]))
     HomefullFixOver1[1].append(len(rfdA))
     HomefullFixOver1[2].append(t)
     HomefullFixOver1[3].append("AwayFixtureFulltimeOver1")
     HomefullFixOver1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture over 2.5 Streaks
            
     HomefullFixOver2[0].append(str(streaksOver10[0])+ "/" +str(streaksOver10[1]))
     HomefullFixOver2[1].append(len(rfdA))
     HomefullFixOver2[2].append(t)
     HomefullFixOver2[3].append("AwayFixtureFulltimeOver2")
     HomefullFixOver2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture over 3.5 Streaks
            
     HomefullFixOver3[0].append(str(streaksOver11[0])+ "/" +str(streaksOver11[1]))
     HomefullFixOver3[1].append(len(rfdA))
     HomefullFixOver3[2].append(t)
     HomefullFixOver3[3].append("AwayFixtureFulltimeOver3")
     HomefullFixOver3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture over 4.5 Streaks
            
     HomefullFixOver4[0].append(str(streaksOver12[0])+ "/" +str(streaksOver12[1]))
     HomefullFixOver4[1].append(len(rfdA))
     HomefullFixOver4[2].append(t)
     HomefullFixOver4[3].append("AwayFixtureFulltimeOver4")
     HomefullFixOver4[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture Win
            
     HomefullFixWin[0].append(str(streaksOver13[0])+ "/" +str(streaksOver13[1]))
     HomefullFixWin[1].append(len(rfdA))
     HomefullFixWin[2].append(t)
     HomefullFixWin[3].append("AwayFixtureFulltimeWin")
     HomefullFixWin[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture WinDraw
            
     HomefullFixWinD[0].append(str(streaksOver14[0])+ "/" +str(streaksOver14[1]))
     HomefullFixWinD[1].append(len(rfdA))
     HomefullFixWinD[2].append(t)
     HomefullFixWinD[3].append("AwayFixtureFullWinDraw")
     HomefullFixWinD[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fulltime Fixture LoseDraw
            
     HomefullFixLoseD[0].append(str(streaksOver15[0])+ "/" +str(streaksOver15[1]))
     HomefullFixLoseD[1].append(len(rfdA))
     HomefullFixLoseD[2].append(t)
     HomefullFixLoseD[3].append("AwayFixtureFullLoseDraw")
     HomefullFixLoseD[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Halftime Win
            
     HomefullHalfWin[0].append(str(streaksOver16[0])+ "/" +str(streaksOver16[1]))
     HomefullHalfWin[1].append(len(rfdA))
     HomefullHalfWin[2].append(t)
     HomefullHalfWin[3].append("AwayFixtureHalftimeWin")
     HomefullHalfWin[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Halftime Win Draw
            
     HomefullHalfWinD[0].append(str(streaksOver17[0])+ "/" +str(streaksOver17[1]))
     HomefullHalfWinD[1].append(len(rfdA))
     HomefullHalfWinD[2].append(t)
     HomefullHalfWinD[3].append("AwayFixtureHalftimeWinDraw")
     HomefullHalfWinD[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Second Half Win Draw
            
     HomefullSecHalfWinD[0].append(str(streaksOver18[0])+ "/" +str(streaksOver18[1]))
     HomefullSecHalfWinD[1].append(len(rfdA))
     HomefullSecHalfWinD[2].append(t)
     HomefullSecHalfWinD[3].append("AwayFixtureSecHalfWinDraw")
     HomefullSecHalfWinD[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Second Half Win
            
     HomefullSecHalfWin[0].append(str(streaksOver19[0])+ "/" +str(streaksOver19[1]))
     HomefullSecHalfWin[1].append(len(rfdA))
     HomefullSecHalfWin[2].append(t)
     HomefullSecHalfWin[3].append("AwayFixtureSecHalfWin")
     HomefullSecHalfWin[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away First Half Over 0.5
            
     HomefullFirstHalfOverZ[0].append(str(streaksOver20[0])+ "/" +str(streaksOver20[1]))
     HomefullFirstHalfOverZ[1].append(len(rfdA))
     HomefullFirstHalfOverZ[2].append(t)
     HomefullFirstHalfOverZ[3].append("AwayFirstHalfOverZ")
     HomefullFirstHalfOverZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away First Half Over 1.5
            
     HomefullFirstHalfOver1[0].append(str(streaksOver21[0])+ "/" +str(streaksOver21[1]))
     HomefullFirstHalfOver1[1].append(len(rfdA))
     HomefullFirstHalfOver1[2].append(t)
     HomefullFirstHalfOver1[3].append("AwayFirstHalfOver1")
     HomefullFirstHalfOver1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away First Half Over 2.5
            
     HomefullFirstHalfOver2[0].append(str(streaksOver22[0])+ "/" +str(streaksOver22[1]))
     HomefullFirstHalfOver2[1].append(len(rfdA))
     HomefullFirstHalfOver2[2].append(t)
     HomefullFirstHalfOver2[3].append("AwayFirstHalfOver2")
     HomefullFirstHalfOver2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Second Half Over 0.5
            
     HomefullSecHalfOverZ[0].append(str(streaksOver23[0])+ "/" +str(streaksOver23[1]))
     HomefullSecHalfOverZ[1].append(len(rfdA))
     HomefullSecHalfOverZ[2].append(t)
     HomefullSecHalfOverZ[3].append("AwaySecondHalfOverZ")
     HomefullSecHalfOverZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  Second Half Over 1.5
            
     HomefullSecHalfOver1[0].append(str(streaksOver24[0])+ "/" +str(streaksOver24[1]))
     HomefullSecHalfOver1[1].append(len(rfdA))
     HomefullSecHalfOver1[2].append(t)
     HomefullSecHalfOver1[3].append("AwaySecondHalfOver1")
     HomefullSecHalfOver1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  Second Half Over 2.5
            
     HomefullSecHalfOver2[0].append(str(streaksOver25[0])+ "/" +str(streaksOver25[1]))
     HomefullSecHalfOver2[1].append(len(rfdA))
     HomefullSecHalfOver2[2].append(t)
     HomefullSecHalfOver2[3].append("AwaySecondHalfOver2")
     HomefullSecHalfOver2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  First Half Conceed Over 0.5
            
     HomefullFirstHalfConceedOVZ[0].append(str(streaksOver26[0])+ "/" +str(streaksOver26[1]))
     HomefullFirstHalfConceedOVZ[1].append(len(rfdA))
     HomefullFirstHalfConceedOVZ[2].append(t)
     HomefullFirstHalfConceedOVZ[3].append("AwayFirstHalfConceed1")
     HomefullFirstHalfConceedOVZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  First Half Conceed Over 1.5
            
     HomefullFirstHalfConceedOV1[0].append(str(streaksOver27[0])+ "/" +str(streaksOver27[1]))
     HomefullFirstHalfConceedOV1[1].append(len(rfdA))
     HomefullFirstHalfConceedOV1[2].append(t)
     HomefullFirstHalfConceedOV1[3].append("AwayFirstHalfConceed2")
     HomefullFirstHalfConceedOV1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  First Half Conceed Over 2.5
            
     HomefullFirstHalfConceedOV2[0].append(str(streaksOver28[0])+ "/" +str(streaksOver28[1]))
     HomefullFirstHalfConceedOV2[1].append(len(rfdA))
     HomefullFirstHalfConceedOV2[2].append(t)
     HomefullFirstHalfConceedOV2[3].append("AwayFirstHalfConceed3")
     HomefullFirstHalfConceedOV2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  Second Half Conceed Over 2.5
            
     HomefullSecHalfConceedOV2[0].append(str(streaksOver29[0])+ "/" +str(streaksOver29[1]))
     HomefullSecHalfConceedOV2[1].append(len(rfdA))
     HomefullSecHalfConceedOV2[2].append(t)
     HomefullSecHalfConceedOV2[3].append("AwaySecondHalfConceed3")
     HomefullSecHalfConceedOV2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away  Second Half Conceed Over 1.5
            
     HomefullSecHalfConceedOV1[0].append(str(streaksOver30[0])+ "/" +str(streaksOver30[1]))
     HomefullSecHalfConceedOV1[1].append(len(rfdA))
     HomefullSecHalfConceedOV1[2].append(t)
     HomefullSecHalfConceedOV1[3].append("AwaySecondHalfConceed2")
     HomefullSecHalfConceedOV1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Second Half Conceed Over 0.5
            
     HomefullSecHalfConceedOVZ[0].append(str(streaksOver31[0])+ "/" +str(streaksOver31[1]))
     HomefullSecHalfConceedOVZ[1].append(len(rfdA))
     HomefullSecHalfConceedOVZ[2].append(t)
     HomefullSecHalfConceedOVZ[3].append("AwaySecondHalfConceed1")
     HomefullSecHalfConceedOVZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Second Half Over 0.5
            
     HomefullSecHalfFixtureOVZ[0].append(str(streaksOver32[0])+ "/" +str(streaksOver32[1]))
     HomefullSecHalfFixtureOVZ[1].append(len(rfdA))
     HomefullSecHalfFixtureOVZ[2].append(t)
     HomefullSecHalfFixtureOVZ[3].append("AwayFixtureSecondHalfOverZ")
     HomefullSecHalfFixtureOVZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Second Half Over 1.5
            
     HomefullSecHalfFixtureOV1[0].append(str(streaksOver33[0])+ "/" +str(streaksOver33[1]))
     HomefullSecHalfFixtureOV1[1].append(len(rfdA))
     HomefullSecHalfFixtureOV1[2].append(t)
     HomefullSecHalfFixtureOV1[3].append("AwayFixtureSecondHalfOver1")
     HomefullSecHalfFixtureOV1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture Second Half Over 2.5
            
     HomefullSecHalfFixtureOV2[0].append(str(streaksOver34[0])+ "/" +str(streaksOver34[1]))
     HomefullSecHalfFixtureOV2[1].append(len(rfdA))
     HomefullSecHalfFixtureOV2[2].append(t)
     HomefullSecHalfFixtureOV2[3].append("AwayFixtureSecondHalfOver2")
     HomefullSecHalfFixtureOV2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture First Half Over 0.5
            
     HomefullFirstHalfFixtureOVZ[0].append(str(streaksOver35[0])+ "/" +str(streaksOver35[1]))
     HomefullFirstHalfFixtureOVZ[1].append(len(rfdA))
     HomefullFirstHalfFixtureOVZ[2].append(t)
     HomefullFirstHalfFixtureOVZ[3].append("AwayFixtureFirstHalfOverZ")
     HomefullFirstHalfFixtureOVZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture First Half Over 1.5
            
     HomefullFirstHalfFixtureOV1[0].append(str(streaksOver36[0])+ "/" +str(streaksOver36[1]))
     HomefullFirstHalfFixtureOV1[1].append(len(rfdA))
     HomefullFirstHalfFixtureOV1[2].append(t)
     HomefullFirstHalfFixtureOV1[3].append("AwayFixtureFirstHalfOver1")
     HomefullFirstHalfFixtureOV1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away Fixture First Half Over 2.5
            
     HomefullFirstHalfFixtureOV2[0].append(str(streaksOver37[0])+ "/" +str(streaksOver37[1]))
     HomefullFirstHalfFixtureOV2[1].append(len(rfdA))
     HomefullFirstHalfFixtureOV2[2].append(t)
     HomefullFirstHalfFixtureOV2[3].append("AwayFixtureFirstHalfOver2")
     HomefullFirstHalfFixtureOV2[4].append("AwayGamesPlayed")
homeFilter(sql_data)
Info=(HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullConceed1,HomefullConceed2,HomefullConceed3,HomefullConceed4,HomefullFixOver0,HomefullFixOver1,HomefullFixOver2,HomefullFixOver3,HomefullFixOver4,HomefullFixWin,HomefullFixWinD,HomefullFixLoseD,HomefullHalfWin,HomefullHalfWinD,HomefullSecHalfWinD,HomefullSecHalfWin,HomefullFirstHalfOverZ,HomefullFirstHalfOver1,HomefullFirstHalfOver2,HomefullSecHalfOverZ,HomefullSecHalfOver1,HomefullSecHalfOver2,HomefullFirstHalfConceedOVZ,HomefullFirstHalfConceedOV1,HomefullFirstHalfConceedOV2,HomefullSecHalfConceedOV2,HomefullSecHalfConceedOV1,HomefullSecHalfConceedOVZ,HomefullSecHalfFixtureOVZ,HomefullSecHalfFixtureOV1,HomefullSecHalfFixtureOV2,HomefullFirstHalfFixtureOVZ,HomefullFirstHalfFixtureOV1,HomefullFirstHalfFixtureOV2)
createReport(Info,pd)