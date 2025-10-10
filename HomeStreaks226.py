import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import numpy as np
from multiLayerPerceptron import mlp
from SecLPAnylaysis import SlPA

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\results2026.accdb')
cursor = conn.cursor()
         
#insert_stmt2 = "select * from EngLeagua125 ORDER BY Tframe Desc"
insert_stmt2 = "Select * FROM portLeag25 union Select * FROM SwissChalleng25 union select * from CzechA25 union select * from Ligue1FrNat25 union select * from IsraelB25 union select * from UkraineA25  union select * from UkrainePresha25 union Select * FROM SwitzerA25 union Select * FROM Turk25 union Select * FROM Turk225 union Select * FROM SloveniaA2025 union Select * FROM skLeague125  union Select * FROM BelgiumChall25 union Select * FROM SwedenB25 union Select * FROM BrazilA25 union Select * FROM SwedenA25 union Select * FROM SloveniaB25 union Select * FROM MalaysiaPrem25 union Select * FROM Eredevisie25 union Select * FROM CroatiaB25 union Select * FROM  portLeag225 union Select * FROM  pslA2025 union Select * FROM  RomaniA25 union Select * FROM  RomaniB25 union Select * FROM  ScotlandA25  union Select * FROM  SerbiaA25 union Select * FROM  SerieA25 union Select * FROM  SerieBB25 union Select * FROM  SingPorePrem25 union Select * FROM  skleague125 union Select * FROM  SlovakiaAA25 union Select * FROM  SlovakiaB25 union select * from SerbiaB25 union select * from AzerBaijan2025"

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
  df.to_excel('Streakshominfo226.xlsx', sheet_name="Home", index=False)
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
     streaksOver2 = BtOr.StreaksOverUnder2(t,rfdA,"k",5,"over")
     streaksOver3 = BtOr.StreaksOverUnder3(t,rfdA,"k",5,"over")
     streaksOver4 = BtOr.StreaksConceed1(t,rfdA,"k",6,"over")
     streaksOver5 = BtOr.StreaksConceed2(t,rfdA,"k",6,"over")
     streaksOver6 = BtOr.StreaksConceed3(t,rfdA,"k",6,"over")
     streaksOver7 = BtOr.StreaksConceed4(t,rfdA,"k",6,"over")
     streaksOver8 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,0)
     streaksOver9 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,1)
     streaksOver10 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,2)
     streaksOver11 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,3)
     streaksOver12 = BtOr.StreaksHomeFullOver0(t,rfdA,"k",5,4)
     streaksOver13 = BtOr.StreaksHomeFullWinLose(t,rfdA,"k",5,"over")
     streaksOver14 = BtOr.StreaksHomeFullWinDraw(t,rfdA,"k",5,"over")
     streaksOver15 = BtOr.StreaksHomeFullLoseDraw(t,rfdA,"k",5,"over")
     streaksOver16 = BtOr.StreaksHomeFullHalfWin(t,rfdA,"k",5,"over")
     streaksOver17 = BtOr.StreaksHomeFullHalfWinD(t,rfdA,"k",5,"over")
     streaksOver18 = BtOr.StreaksHomeSeconHalfWinD(t,rfdA,"k",5,"over")
     streaksOver19 = BtOr.StreaksHomeSeconHalfWin(t,rfdA,"k",5,"over")
     streaksOver20 = BtOr.StreaksHomeFirstHalf(t,rfdA,"k",5,0)
     streaksOver21 = BtOr.StreaksHomeFirstHalf(t,rfdA,"k",5,1)
     streaksOver22 = BtOr.StreaksHomeFirstHalf(t,rfdA,"k",5,2)
     streaksOver23 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",5,0)
     streaksOver24 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",5,1)
     streaksOver25 = BtOr.StreaksHomeSecHalf(t,rfdA,"k",5,2)
     streaksOver26 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",8,0)
     streaksOver27 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",8,1)
     streaksOver28 = BtOr.StreaksHomeFirstHalfConceed1(t,rfdA,"k",8,2)
     streaksOver29 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",8,2)
     streaksOver30 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",8,1)
     streaksOver31 = BtOr.StreaksHomeSecondHalfConceed1(t,rfdA,"k",8,0)
     streaksOver32 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"k",5,0)
     streaksOver33 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"k",5,1)
     streaksOver34 = BtOr.StreaksFixHomeSecondHalfOvZ(t,rfdA,"k",5,2)
     streaksOver35 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"k",5,0)
     streaksOver36 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"k",5,1)
     streaksOver37 = BtOr.StreaksFixHomeFirstHalfOvZ(t,rfdA,"k",5,2)
     
    
     
#=====================================================================================================#
#Home Over  0.5 Streaks
            
     HomefullOver1[0].append(str(streaksOver[0])+ "/" +str(streaksOver[1]))
     HomefullOver1[1].append(len(rfdA))
     HomefullOver1[2].append(t)
     HomefullOver1[3].append("HomeOverZ")
     HomefullOver1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Over 1.5 Streaks
            
     HomefullOver2[0].append(str(streaksOver1[0])+ "/" +str(streaksOver1[1]))
     HomefullOver2[1].append(len(rfdA))
     HomefullOver2[2].append(t)
     HomefullOver2[3].append("HomeOver1")
     HomefullOver2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Over 2.5 Streaks
            
     HomefullOver3[0].append(str(streaksOver2[0])+ "/" +str(streaksOver2[1]))
     HomefullOver3[1].append(len(rfdA))
     HomefullOver3[2].append(t)
     HomefullOver3[3].append("HomeOver2")
     HomefullOver3[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Over 3.5 Streaks
            
     HomefullOver4[0].append(str(streaksOver3[0])+ "/" +str(streaksOver3[1]))
     HomefullOver4[1].append(len(rfdA))
     HomefullOver4[2].append(t)
     HomefullOver4[3].append("HomeOver3")
     HomefullOver4[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed 0.5 Streaks
            
     HomefullConceed1[0].append(str(streaksOver4[0])+ "/" +str(streaksOver4[1]))
     HomefullConceed1[1].append(len(rfdA))
     HomefullConceed1[2].append(t)
     HomefullConceed1[3].append("HomeConceed1")
     HomefullConceed1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed 1.5 Streaks
            
     HomefullConceed2[0].append(str(streaksOver5[0])+ "/" +str(streaksOver5[1]))
     HomefullConceed2[1].append(len(rfdA))
     HomefullConceed2[2].append(t)
     HomefullConceed2[3].append("HomeConceed2")
     HomefullConceed2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed 2.5 Streaks
            
     HomefullConceed3[0].append(str(streaksOver6[0])+ "/" +str(streaksOver6[1]))
     HomefullConceed3[1].append(len(rfdA))
     HomefullConceed3[2].append(t)
     HomefullConceed3[3].append("HomeConceed3")
     HomefullConceed3[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed 3.5 Streaks
            
     HomefullConceed4[0].append(str(streaksOver7[0])+ "/" +str(streaksOver7[1]))
     HomefullConceed4[1].append(len(rfdA))
     HomefullConceed4[2].append(t)
     HomefullConceed4[3].append("HomeConceed4")
     HomefullConceed4[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture over 0.5 Streaks
            
     HomefullFixOver0[0].append(str(streaksOver8[0])+ "/" +str(streaksOver8[1]))
     HomefullFixOver0[1].append(len(rfdA))
     HomefullFixOver0[2].append(t)
     HomefullFixOver0[3].append("HomeFixtureFulltimeOverZ")
     HomefullFixOver0[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture over 1.5 Streaks
            
     HomefullFixOver1[0].append(str(streaksOver9[0])+ "/" +str(streaksOver9[1]))
     HomefullFixOver1[1].append(len(rfdA))
     HomefullFixOver1[2].append(t)
     HomefullFixOver1[3].append("HomeFixtureFulltimeOver1")
     HomefullFixOver1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture over 2.5 Streaks
            
     HomefullFixOver2[0].append(str(streaksOver10[0])+ "/" +str(streaksOver10[1]))
     HomefullFixOver2[1].append(len(rfdA))
     HomefullFixOver2[2].append(t)
     HomefullFixOver2[3].append("HomeFixtureFulltimeOver2")
     HomefullFixOver2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture over 3.5 Streaks
            
     HomefullFixOver3[0].append(str(streaksOver11[0])+ "/" +str(streaksOver11[1]))
     HomefullFixOver3[1].append(len(rfdA))
     HomefullFixOver3[2].append(t)
     HomefullFixOver3[3].append("HomeFixtureFulltimeOver3")
     HomefullFixOver3[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture over 4.5 Streaks
            
     HomefullFixOver4[0].append(str(streaksOver12[0])+ "/" +str(streaksOver12[1]))
     HomefullFixOver4[1].append(len(rfdA))
     HomefullFixOver4[2].append(t)
     HomefullFixOver4[3].append("HomeFixtureFulltimeOver4")
     HomefullFixOver4[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture Win
            
     HomefullFixWin[0].append(str(streaksOver13[0])+ "/" +str(streaksOver13[1]))
     HomefullFixWin[1].append(len(rfdA))
     HomefullFixWin[2].append(t)
     HomefullFixWin[3].append("HomeFixtureFulltimeWin")
     HomefullFixWin[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture WinDraw
            
     HomefullFixWinD[0].append(str(streaksOver14[0])+ "/" +str(streaksOver14[1]))
     HomefullFixWinD[1].append(len(rfdA))
     HomefullFixWinD[2].append(t)
     HomefullFixWinD[3].append("HomeFixtureFullWinDraw")
     HomefullFixWinD[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fulltime Fixture LoseDraw
            
     HomefullFixLoseD[0].append(str(streaksOver15[0])+ "/" +str(streaksOver15[1]))
     HomefullFixLoseD[1].append(len(rfdA))
     HomefullFixLoseD[2].append(t)
     HomefullFixLoseD[3].append("HomeFixtureFullLoseDraw")
     HomefullFixLoseD[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Halftime Win
            
     HomefullHalfWin[0].append(str(streaksOver16[0])+ "/" +str(streaksOver16[1]))
     HomefullHalfWin[1].append(len(rfdA))
     HomefullHalfWin[2].append(t)
     HomefullHalfWin[3].append("HomeFixtureHalftimeWin")
     HomefullHalfWin[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Halftime Win Draw
            
     HomefullHalfWinD[0].append(str(streaksOver17[0])+ "/" +str(streaksOver17[1]))
     HomefullHalfWinD[1].append(len(rfdA))
     HomefullHalfWinD[2].append(t)
     HomefullHalfWinD[3].append("HomeFixtureHalftimeWinDraw")
     HomefullHalfWinD[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Second Half Win Draw
            
     HomefullSecHalfWinD[0].append(str(streaksOver18[0])+ "/" +str(streaksOver18[1]))
     HomefullSecHalfWinD[1].append(len(rfdA))
     HomefullSecHalfWinD[2].append(t)
     HomefullSecHalfWinD[3].append("HomeFixtureSecHalfWinDraw")
     HomefullSecHalfWinD[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Second Half Win
            
     HomefullSecHalfWin[0].append(str(streaksOver19[0])+ "/" +str(streaksOver19[1]))
     HomefullSecHalfWin[1].append(len(rfdA))
     HomefullSecHalfWin[2].append(t)
     HomefullSecHalfWin[3].append("HomeFixtureSecHalfWin")
     HomefullSecHalfWin[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home First Half Over 0.5
            
     HomefullFirstHalfOverZ[0].append(str(streaksOver20[0])+ "/" +str(streaksOver20[1]))
     HomefullFirstHalfOverZ[1].append(len(rfdA))
     HomefullFirstHalfOverZ[2].append(t)
     HomefullFirstHalfOverZ[3].append("HomeFirstHalfOverZ")
     HomefullFirstHalfOverZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home First Half Over 1.5
            
     HomefullFirstHalfOver1[0].append(str(streaksOver21[0])+ "/" +str(streaksOver21[1]))
     HomefullFirstHalfOver1[1].append(len(rfdA))
     HomefullFirstHalfOver1[2].append(t)
     HomefullFirstHalfOver1[3].append("HomeFirstHalfOver1")
     HomefullFirstHalfOver1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Hom First Half Over 2.5
            
     HomefullFirstHalfOver2[0].append(str(streaksOver22[0])+ "/" +str(streaksOver22[1]))
     HomefullFirstHalfOver2[1].append(len(rfdA))
     HomefullFirstHalfOver2[2].append(t)
     HomefullFirstHalfOver2[3].append("HomeFirstHalfOver2")
     HomefullFirstHalfOver2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Second Half Over 0.5
            
     HomefullSecHalfOverZ[0].append(str(streaksOver23[0])+ "/" +str(streaksOver23[1]))
     HomefullSecHalfOverZ[1].append(len(rfdA))
     HomefullSecHalfOverZ[2].append(t)
     HomefullSecHalfOverZ[3].append("HomeSecondHalfOverZ")
     HomefullSecHalfOverZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  Second Half Over 1.5
            
     HomefullSecHalfOver1[0].append(str(streaksOver24[0])+ "/" +str(streaksOver24[1]))
     HomefullSecHalfOver1[1].append(len(rfdA))
     HomefullSecHalfOver1[2].append(t)
     HomefullSecHalfOver1[3].append("HomeSecondHalfOver1")
     HomefullSecHalfOver1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  Second Half Over 2.5
            
     HomefullSecHalfOver2[0].append(str(streaksOver25[0])+ "/" +str(streaksOver25[1]))
     HomefullSecHalfOver2[1].append(len(rfdA))
     HomefullSecHalfOver2[2].append(t)
     HomefullSecHalfOver2[3].append("HomeSecondHalfOver2")
     HomefullSecHalfOver2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  First Half Conceed Over 0.5
            
     HomefullFirstHalfConceedOVZ[0].append(str(streaksOver26[0])+ "/" +str(streaksOver26[1]))
     HomefullFirstHalfConceedOVZ[1].append(len(rfdA))
     HomefullFirstHalfConceedOVZ[2].append(t)
     HomefullFirstHalfConceedOVZ[3].append("HomeFirstHalfConceed1")
     HomefullFirstHalfConceedOVZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  First Half Conceed Over 1.5
            
     HomefullFirstHalfConceedOV1[0].append(str(streaksOver27[0])+ "/" +str(streaksOver27[1]))
     HomefullFirstHalfConceedOV1[1].append(len(rfdA))
     HomefullFirstHalfConceedOV1[2].append(t)
     HomefullFirstHalfConceedOV1[3].append("HomeeFirstHalfConceed2")
     HomefullFirstHalfConceedOV1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  First Half Conceed Over 2.5
            
     HomefullFirstHalfConceedOV2[0].append(str(streaksOver28[0])+ "/" +str(streaksOver28[1]))
     HomefullFirstHalfConceedOV2[1].append(len(rfdA))
     HomefullFirstHalfConceedOV2[2].append(t)
     HomefullFirstHalfConceedOV2[3].append("HomeFirstHalfConceed3")
     HomefullFirstHalfConceedOV2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  Second Half Conceed Over 2.5
            
     HomefullSecHalfConceedOV2[0].append(str(streaksOver29[0])+ "/" +str(streaksOver29[1]))
     HomefullSecHalfConceedOV2[1].append(len(rfdA))
     HomefullSecHalfConceedOV2[2].append(t)
     HomefullSecHalfConceedOV2[3].append("HomeSecondHalfConceed3")
     HomefullSecHalfConceedOV2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home  Second Half Conceed Over 1.5
            
     HomefullSecHalfConceedOV1[0].append(str(streaksOver30[0])+ "/" +str(streaksOver30[1]))
     HomefullSecHalfConceedOV1[1].append(len(rfdA))
     HomefullSecHalfConceedOV1[2].append(t)
     HomefullSecHalfConceedOV1[3].append("HomeSecondHalfConceed2")
     HomefullSecHalfConceedOV1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Second Half Conceed Over 0.5
            
     HomefullSecHalfConceedOVZ[0].append(str(streaksOver31[0])+ "/" +str(streaksOver31[1]))
     HomefullSecHalfConceedOVZ[1].append(len(rfdA))
     HomefullSecHalfConceedOVZ[2].append(t)
     HomefullSecHalfConceedOVZ[3].append("HomeSecondHalfConceed1")
     HomefullSecHalfConceedOVZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Second Half Over 0.5
            
     HomefullSecHalfFixtureOVZ[0].append(str(streaksOver32[0])+ "/" +str(streaksOver32[1]))
     HomefullSecHalfFixtureOVZ[1].append(len(rfdA))
     HomefullSecHalfFixtureOVZ[2].append(t)
     HomefullSecHalfFixtureOVZ[3].append("HomeFixtureSecondHalfOverZ")
     HomefullSecHalfFixtureOVZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Second Half Over 1.5
            
     HomefullSecHalfFixtureOV1[0].append(str(streaksOver33[0])+ "/" +str(streaksOver33[1]))
     HomefullSecHalfFixtureOV1[1].append(len(rfdA))
     HomefullSecHalfFixtureOV1[2].append(t)
     HomefullSecHalfFixtureOV1[3].append("HomeFixtureSecondHalfOver1")
     HomefullSecHalfFixtureOV1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture Second Half Over 2.5
            
     HomefullSecHalfFixtureOV2[0].append(str(streaksOver34[0])+ "/" +str(streaksOver34[1]))
     HomefullSecHalfFixtureOV2[1].append(len(rfdA))
     HomefullSecHalfFixtureOV2[2].append(t)
     HomefullSecHalfFixtureOV2[3].append("HomeFixtureSecondHalfOver2")
     HomefullSecHalfFixtureOV2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture First Half Over 0.5
            
     HomefullFirstHalfFixtureOVZ[0].append(str(streaksOver35[0])+ "/" +str(streaksOver35[1]))
     HomefullFirstHalfFixtureOVZ[1].append(len(rfdA))
     HomefullFirstHalfFixtureOVZ[2].append(t)
     HomefullFirstHalfFixtureOVZ[3].append("HomeFixtureFirstHalfOverZ")
     HomefullFirstHalfFixtureOVZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture First Half Over 1.5
            
     HomefullFirstHalfFixtureOV1[0].append(str(streaksOver36[0])+ "/" +str(streaksOver36[1]))
     HomefullFirstHalfFixtureOV1[1].append(len(rfdA))
     HomefullFirstHalfFixtureOV1[2].append(t)
     HomefullFirstHalfFixtureOV1[3].append("HomeFixtureFirstHalfOver1")
     HomefullFirstHalfFixtureOV1[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Fixture First Half Over 2.5
            
     HomefullFirstHalfFixtureOV2[0].append(str(streaksOver37[0])+ "/" +str(streaksOver37[1]))
     HomefullFirstHalfFixtureOV2[1].append(len(rfdA))
     HomefullFirstHalfFixtureOV2[2].append(t)
     HomefullFirstHalfFixtureOV2[3].append("HomeFixtureFirstHalfOver2")
     HomefullFirstHalfFixtureOV2[4].append("HomeGamesPlayed")
homeFilter(sql_data)
Info=(HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullConceed1,HomefullConceed2,HomefullConceed3,HomefullConceed4,HomefullFixOver0,HomefullFixOver1,HomefullFixOver2,HomefullFixOver3,HomefullFixOver4,HomefullFixWin,HomefullFixWinD,HomefullFixLoseD,HomefullHalfWin,HomefullHalfWinD,HomefullSecHalfWinD,HomefullSecHalfWin,HomefullFirstHalfOverZ,HomefullFirstHalfOver1,HomefullFirstHalfOver2,HomefullSecHalfOverZ,HomefullSecHalfOver1,HomefullSecHalfOver2,HomefullFirstHalfConceedOVZ,HomefullFirstHalfConceedOV1,HomefullFirstHalfConceedOV2,HomefullSecHalfConceedOV2,HomefullSecHalfConceedOV1,HomefullSecHalfConceedOVZ,HomefullSecHalfFixtureOVZ,HomefullSecHalfFixtureOV1,HomefullSecHalfFixtureOV2,HomefullFirstHalfFixtureOVZ,HomefullFirstHalfFixtureOV1,HomefullFirstHalfFixtureOV2)
createReport(Info,pd)