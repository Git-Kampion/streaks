import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
from multiLayerPerceptron import mlp
import seaborn as sb
from SecLPAnylaysis import SlPA


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from ScotlandA24 UNION select * from SwitzerA24 UNION select * from Turk24 UNION select * from Turk22024 UNION select * from SerieA24 UNION select * from SerbiaA UNION select * from SaudiPrem UNION select * from RomaniA UNION select * from PolandB UNION select * from PolandA UNION select * from Ligue2Fr UNION select * from Ligue1FrNat UNION select * from Ligue1Fr24 UNION select * from Laliga24 UNION select * from GreeceA24 UNION select * from Eredevisie24 UNION select * from EplChampionShip24 UNION select * from Epl24 UNION select * from DenmarkB UNION select * from DenmarkA UNION select * from CzechB UNION select * from CzechA24 UNION select * from BundasLiga24 UNION select * from Bundas2Liga24 UNION select * from BulgariaPrem UNION select * from Austria order by Round ASC"

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

HomefullOver1 = ([],[],[],[],[])
HomefullOver2= ([],[],[],[],[])
HomefullOver3= ([],[],[],[],[])
HomefullOver4= ([],[],[],[],[])
HomefullOver5 = ([],[],[],[],[])
HWins = ([],[],[],[],[])
HHWinsDraw = ([],[],[],[],[])
HWinsDraw = ([],[],[],[],[])
HHalftimeWins = ([],[],[],[],[])
HSWinsDraw= ([],[],[],[],[])
H2ndHWins = ([],[],[],[],[])
HomeHalftimeOverZ = ([],[],[],[],[])
HomefrstOver1 = ([],[],[],[],[])
HomefrstOver2= ([],[],[],[],[])
HomefrstOver3= ([],[],[],[],[])
HomeSOvs= ([],[],[],[],[])
HomeSOvs1= ([],[],[],[],[])
HomeSOvs2= ([],[],[],[],[])
HomeFFOvs = ([],[],[],[],[])
HomeFFOvs2= ([],[],[],[],[])
HomeFFOvs3= ([],[],[],[],[])
HomeHalftimeConceedOverZ = ([],[],[],[],[])
HomeHalftimeConceedOverZ2 = ([],[],[],[],[])
HomeHalftimeConceedOverZ3 = ([],[],[],[],[])
HomeSectimeConceedOverZ = ([],[],[],[],[])
HomeSectimeConceedOverZ2 = ([],[],[],[],[])
HomeSectimeConceedOverZ3 = ([],[],[],[],[])
HomeSFOvs3 = ([],[],[],[],[])
HomeSFOvs2 = ([],[],[],[],[])
HomeSFOvs = ([],[],[],[],[])
HomeFrstunder = ([],[],[],[],[])
HomeFrstunder1= ([],[],[],[],[])
HomeFrstunder2= ([],[],[],[],[])
HomeallBTS = ([],[],[],[],[])
HomeFrstHBTS = ([],[],[],[],[])
HomeSecndHBTS = ([],[],[],[],[])
HomeSConceedOvs = ([],[],[],[],[])
HomeSConceedOvs2= ([],[],[],[],[])
HomeSConceedOvs3= ([],[],[],[],[])
HomeSfailtToConceedOvs= ([],[],[],[],[])
HomeSfailtToConceedOvs2= ([],[],[],[],[])
HomeSfailtToConceedOvs3= ([],[],[],[],[])
HomeFConceedOvs = ([],[],[],[],[])
HomeFConceedOvs2 = ([],[],[],[],[])
HomeFConceedOvs3 = ([],[],[],[],[])
HomeFConceedOvs4 = ([],[],[],[],[])
HomeFConceedOvs5 = ([],[],[],[],[])
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
ConceedFSoutcome = ([],[],[],[],[])
ConceedFSoutcomeOne = ([],[],[],[],[])
ConceedFSoutcomeTwo= ([],[],[],[],[])
ScoreFSoutcome = ([],[],[],[],[])
ScoreFSoutcomeOne = ([],[],[],[],[])
ScoreFSoutcomeTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOutput = ([],[],[],[],[])
ScoreFSoutcomeAny = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTT = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTThree = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderT = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTThree = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderO = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOThree = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZ = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZThree = ([],[],[],[],[])
FirstHalfAwayWinSecondHalfLose= ([],[],[],[],[])
FirstHalfAwayWinSecondHalfHomeWindraw= ([],[],[],[],[])
FirstHalfAwayWinSecondHalfHomeScore= ([],[],[],[],[])
FirstHAwayWinSecHAwayScore3= ([],[],[],[],[])
FirstHAwayWinSecHAwayScore2= ([],[],[],[],[])
FirstHAwayWinSecHAwayScore1= ([],[],[],[],[])
FirstHAwayWinSecHHomeScore1= ([],[],[],[],[])
FirstHAwayWinSecHHomeScore2= ([],[],[],[],[])
FirstHAwayWinSecHHomeScore3= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv2= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv3= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv4= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv7= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv8= ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv14 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv15 = ([],[],[],[],[])
awayConceedOvUvHomeConceedOvUv16 = ([],[],[],[],[])

awayScorOvUvHomeConceedOvUv = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv2= ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv3= ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv4= ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv5 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv6 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv7= ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv8= ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv9 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv10 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv11 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv12 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv13 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv14 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv15 = ([],[],[],[],[])
awayScorOvUvHomeConceedOvUv16 = ([],[],[],[],[])

awayScorOvUvHomeScorOvUv = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv2= ([],[],[],[],[])
awayScorOvUvHomeScorOvUv3= ([],[],[],[],[])
awayScorOvUvHomeScorOvUv4= ([],[],[],[],[])
awayScorOvUvHomeScorOvUv5 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv6 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv7= ([],[],[],[],[])
awayScorOvUvHomeScorOvUv8= ([],[],[],[],[])
awayScorOvUvHomeScorOvUv9 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv10 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv11 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv12 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv13 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv14 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv15 = ([],[],[],[],[])
awayScorOvUvHomeScorOvUv16 = ([],[],[],[],[])

awayConHomeConceed = ([],[],[],[],[])
awayConHomeConceed2= ([],[],[],[],[])
awayConHomeConceed3= ([],[],[],[],[])
awayConHomeConceed4= ([],[],[],[],[])
awayConHomeConceed5 = ([],[],[],[],[])
awayConHomeConceed6 = ([],[],[],[],[])
awayConHomeConceed7= ([],[],[],[],[])
awayConHomeConceed8= ([],[],[],[],[])
awayConHomeConceed9 = ([],[],[],[],[])
awayConHomeConceed10 = ([],[],[],[],[])
awayConHomeConceed11 = ([],[],[],[],[])
awayConHomeConceed12 = ([],[],[],[],[])
awayConHomeConceed13 = ([],[],[],[],[])
awayConHomeConceed14 = ([],[],[],[],[])
awayConHomeConceed15 = ([],[],[],[],[])
awayConHomeConceed16 = ([],[],[],[],[])

awayConOvUvHomeConceedOvUv = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv2= ([],[],[],[],[])
awayConOvUvHomeConceedOvUv3= ([],[],[],[],[])
awayConOvUvHomeConceedOvUv4= ([],[],[],[],[])
awayConOvUvHomeConceedOvUv5 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv6 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv7= ([],[],[],[],[])
awayConOvUvHomeConceedOvUv8= ([],[],[],[],[])
awayConOvUvHomeConceedOvUv9 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv10 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv11 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv12 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv13 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv14 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv15 = ([],[],[],[],[])
awayConOvUvHomeConceedOvUv16 = ([],[],[],[],[])






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
  df.to_excel('hominfo.xlsx', sheet_name="Home", index=False)
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
     HWinLose = BtOr.MatchRes(t,rfdA,"k",5)
     AwOvers = BtOr.OverUnderSeaon(t,rfdA,"k",5)
     HfullTimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"over")
     HHalfimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"first")
     HsecHaTimeOver = BtOr.FixOverUnders(t,rfdA,"k",5,"sec")
     hFBTS  = BtOr.Bts(t,rfdA,"k",5,"over")
     hfirstBTS = BtOr.Bts(t,rfdA,"k",5,"first")
     hSecndBTS = BtOr.Bts(t,rfdA,"k",5,"sec")
     HmeConceedFulltime = BtOr.ConcededWholeSeaon(t,rfdA,"k",6)
     
     
#=====================================================================================================#
#Home Fix fulltime over 0.5
            
     HomefullOver1[0].append(str(HfullTimeOver[0][0])+ "/" +str(HfullTimeOver[1][0]))
     HomefullOver1[1].append(len(rfdA))
     HomefullOver1[2].append(t)
     HomefullOver1[3].append("HomeFixtureFulltimeOverZ")
     HomefullOver1[4].append("HomeGamesPlayed")
#Home Fix fulltime over 1.5
           
     HomefullOver2[0].append(str(HfullTimeOver[0][1])+ "/" +str(HfullTimeOver[1][1]))
     HomefullOver2[1].append(len(rfdA))
     HomefullOver2[2].append(t)
     HomefullOver2[3].append("HomeFixtureFulltimeOver1")
     HomefullOver2[4].append("HomeGamesPlayed")
#Home Fix fulltime over 2.5
          
     HomefullOver3[0].append(str(HfullTimeOver[0][2])+ "/" +str(HfullTimeOver[1][2]))
     HomefullOver3[1].append(len(rfdA))
     HomefullOver3[2].append(t)
     HomefullOver3[3].append("HomeFixtureFulltimeOver2")
     HomefullOver3[4].append("HomeGamesPlayed")    
#Home Fix  fulltime over 3.5
           
     HomefullOver4[0].append(str(HfullTimeOver[0][3])+ "/" +str(HfullTimeOver[1][3]))
     HomefullOver4[1].append(len(rfdA))
     HomefullOver4[2].append(t)
     HomefullOver4[3].append("HomeFixtureFulltimeOver3")
     HomefullOver4[4].append("HomeGamesPlayed")
#Home Fix  fulltime over 4.5
            
     HomefullOver5[0].append(str(HfullTimeOver[0][4])+ "/" +str(HfullTimeOver[1][4]))
     HomefullOver5[1].append(len(rfdA))
     HomefullOver5[2].append(t)
     HomefullOver5[3].append("HomeFixtureFulltimeOver4")
     HomefullOver5[4].append("HomeGamesPlayed") 
#=============================================================================#
#Home wins
             
     HWins[0].append(str(HWinLose[0]) + "/" + str(HWinLose[15]))
     HWins[1].append(len(rfdA))
     HWins[2].append(t)
     HWins[3].append("HomeFulltimeWins")
     HWins[4].append("HomeGamesPlayed")
#=============================================================================#
#Home Faulure to Lose/Win Draw
            
     HWinsDraw[0].append(str(HWinLose[14]) + "/" + str(HWinLose[2]))
     HWinsDraw[1].append(len(rfdA))
     HWinsDraw[2].append(t)
     HWinsDraw[3].append("HomeFulltimeWinDraw")
     HWinsDraw[4].append("HomeGamesPlayed")   
#========================================================================#
#Home halftime wins
          
     HHalftimeWins[0].append(str(HWinLose[4])+ "/" +str(HWinLose[7]))
     HHalftimeWins[1].append(len(rfdA))
     HHalftimeWins[2].append(t)
     HHalftimeWins[3].append("HomeHalfTimeWins")
     HHalftimeWins[4].append("HomeGamesPlayed") 
#========================================================================#
#Home halftime  Win Draw/Faulure to Lose
            
     HHWinsDraw[0].append(str(HWinLose[8]) + "/" + str(HWinLose[6]))
     HHWinsDraw[1].append(len(rfdA))
     HHWinsDraw[2].append(t)
     HHWinsDraw[3].append("HomeHalftimeWinDraw")
     HHWinsDraw[4].append("HomeGamesPlayed")
#========================================================================#
#Home Secondhalf Win Draw/Faulure to Lose
           
     HSWinsDraw[0].append(str(HWinLose[9]) + "/" + str(HWinLose[13]))
     HSWinsDraw[1].append(len(rfdA))
     HSWinsDraw[2].append(t)
     HSWinsDraw[3].append("HomeSecondHalfWinDraw")
     HSWinsDraw[4].append("HomeGamesPlayed") 
#========================================================================#
#Home Secondhalf Win 
          
     H2ndHWins[0].append(str(HWinLose[12])+ "/" +str(HWinLose[17]))
     H2ndHWins[1].append(len(rfdA))
     H2ndHWins[2].append(t)
     H2ndHWins[3].append("HomeSecondHalfWin")
     H2ndHWins[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home First Half over 0.5
            
     HomeHalftimeOverZ[0].append(str(AwOvers[17][0])+ "/" +str(AwOvers[16][0]))
     HomeHalftimeOverZ[1].append(len(rfdA))
     HomeHalftimeOverZ[2].append(t)
     HomeHalftimeOverZ[3].append("HomeFirstHalfOverZ")
     HomeHalftimeOverZ[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half over 1.5
           
     HomefrstOver1[0].append(str(AwOvers[17][1])+ "/" +str(AwOvers[16][1]))
     HomefrstOver1[1].append(len(rfdA))
     HomefrstOver1[2].append(t)
     HomefrstOver1[3].append("HomeFirstHalfOver1")
     HomefrstOver1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half over 2.5
            
     HomefrstOver2[0].append(str(AwOvers[17][2])+ "/" + str(AwOvers[16][2]))
     HomefrstOver2[1].append(len(rfdA))
     HomefrstOver2[2].append(t)
     HomefrstOver2[3].append("HomeFirstHalfOver2")
     HomefrstOver2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 0.5
          
     HomeSOvs[0].append(str(AwOvers[14][0])+ "/" +str(AwOvers[15][0]))
     HomeSOvs[1].append(len(rfdA))
     HomeSOvs[2].append(t)
     HomeSOvs[3].append("HomeSecHalfOverZ")
     HomeSOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 1.5
             
     HomeSOvs1[0].append(str(AwOvers[14][1])+ "/" +str(AwOvers[15][1]))
     HomeSOvs1[1].append(len(rfdA))
     HomeSOvs1[2].append(t)
     HomeSOvs1[3].append("HomeSecHalfOver1")
     HomeSOvs1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half over 2.5
            
     HomeSOvs2[0].append(str(AwOvers[14][2]) + "/" + str(AwOvers[15][2]))
     HomeSOvs2[1].append(len(rfdA))
     HomeSOvs2[2].append(t)
     HomeSOvs2[3].append("HomeSecHalfOver2")
     HomeSOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 0.5
            
     HomeFFOvs[0].append(str(HHalfimeOver[0][0]) + "/" +str(HHalfimeOver[1][0]))
     HomeFFOvs[1].append(len(rfdA))
     HomeFFOvs[2].append(t)
     HomeFFOvs[3].append("HomeFixtureFirstHalfOverZ")
     HomeFFOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 1.5
            
     HomeFFOvs2[0].append(str(HHalfimeOver[0][1]) + "/" + str(HHalfimeOver[1][1]))
     HomeFFOvs2[1].append(len(rfdA))
     HomeFFOvs2[2].append(t)
     HomeFFOvs2[3].append("HomeFixtureFirstHalfOver1")
     HomeFFOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half Fixture over 2.5
           
     HomeFFOvs3[0].append(str(HHalfimeOver[0][2]) + "/" + str(HHalfimeOver[1][2]))
     HomeFFOvs3[1].append(len(rfdA))
     HomeFFOvs3[2].append(t)
     HomeFFOvs3[3].append("HomeFixtureFirstHalfOver2" )
     HomeFFOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 0.5
             
     HomeSFOvs[0].append(str(HsecHaTimeOver[0][0]) + "/" + str(HsecHaTimeOver[1][0]))
     HomeSFOvs[1].append(len(rfdA))
     HomeSFOvs[2].append(t)
     HomeSFOvs[3].append("HomeFixtureSecondHalfOverZ")
     HomeSFOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 1.5
             
     HomeSFOvs2[0].append(str(HsecHaTimeOver[0][1]) + "/" + str(HsecHaTimeOver[1][1]))
     HomeSFOvs2[1].append(len(rfdA))
     HomeSFOvs2[2].append(t)
     HomeSFOvs2[3].append("HomeFixtureSecondHalfOver1")
     HomeSFOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half Fixture over 2.5
           
     HomeSFOvs3[0].append(str(HsecHaTimeOver[0][2])  + "/" + str(HsecHaTimeOver[1][2]))
     HomeSFOvs3[1].append(len(rfdA))
     HomeSFOvs3[2].append(t)
     HomeSFOvs3[3].append("HomeFixtureSecondHalfOver2")
     HomeSFOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Overall Fixture BTS
            
     HomeallBTS[0].append(str(hFBTS[0]) + "/" + str(hFBTS[1]))
     HomeallBTS[1].append(len(rfdA))
     HomeallBTS[2].append(t)
     HomeallBTS[3].append("HomeFixtureBTS")
     HomeallBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home First Half BTS
            
     HomeFrstHBTS[0].append(str(hfirstBTS[0]) + "/" + str(hfirstBTS[1]))
     HomeFrstHBTS[1].append(len(rfdA))
     HomeFrstHBTS[2].append(t)
     HomeFrstHBTS[3].append("HomeFirstHalfBTS")
     HomeFrstHBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Second Half BTS
             
     HomeSecndHBTS[0].append(str(hSecndBTS[0]) + "/" + str(hSecndBTS[1]))
     HomeSecndHBTS[1].append(len(rfdA))
     HomeSecndHBTS[2].append(t)
     HomeSecndHBTS[3].append("HomeSecondHalfBTS")
     HomeSecndHBTS[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 1 Fulltime
          
     HomeFConceedOvs[0].append(str(HmeConceedFulltime[0]) + "/" + str(HmeConceedFulltime[1]))
     HomeFConceedOvs[1].append(len(rfdA))
     HomeFConceedOvs[2].append(t)
     HomeFConceedOvs[3].append("HomeConceedFulltime1")
     HomeFConceedOvs[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 2 Fulltime
             
     HomeFConceedOvs2[0].append(str(HmeConceedFulltime[2]) + "/" + str(HmeConceedFulltime[3]))
     HomeFConceedOvs2[1].append(len(rfdA))
     HomeFConceedOvs2[2].append(t)
     HomeFConceedOvs2[3].append("HomeConceedFulltime2")
     HomeFConceedOvs2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 3 Fulltime
           
     HomeFConceedOvs3[0].append(str(HmeConceedFulltime[4]) + "/" + str(HmeConceedFulltime[5]))
     HomeFConceedOvs3[1].append(len(rfdA))
     HomeFConceedOvs3[2].append(t)
     HomeFConceedOvs3[3].append("HomeConceedFulltime3")
     HomeFConceedOvs3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 4 Fulltime
            
     HomeFConceedOvs4[0].append(str(HmeConceedFulltime[6]) + "/" + str(HmeConceedFulltime[7]))
     HomeFConceedOvs4[1].append(len(rfdA))
     HomeFConceedOvs4[2].append(t)
     HomeFConceedOvs4[3].append("HomeConceedFulltime4")
     HomeFConceedOvs4[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed 5 Fulltime
           
     HomeFConceedOvs5[0].append(str(HmeConceedFulltime[8]) + "/" + str(HmeConceedFulltime[9]))
     HomeFConceedOvs5[1].append(len(rfdA))
     HomeFConceedOvs5[2].append(t)
     HomeFConceedOvs5[3].append("HomeConceedFulltime5")
     HomeFConceedOvs5[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 1 
           
     HomeFixOver1[0].append(str(AwOvers[0][0]) + "/" + str(AwOvers[1][0]))
     HomeFixOver1[1].append(len(rfdA))
     HomeFixOver1[2].append(t)
     HomeFixOver1[3].append("HomeOverZero")
     HomeFixOver1[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 2 
              
     HomeFixOver2[0].append(str(AwOvers[0][1]) + "/" + str(AwOvers[1][1]))
     HomeFixOver2[1].append(len(rfdA))
     HomeFixOver2[2].append(t)
     HomeFixOver2[3].append("HomeOver1")
     HomeFixOver2[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 3 
              
     HomeFixOver3[0].append(str(AwOvers[0][2]) + "/" + str(AwOvers[1][2]))
     HomeFixOver3[1].append(len(rfdA))
     HomeFixOver3[2].append(t)
     HomeFixOver3[3].append("HomeOver2")
     HomeFixOver3[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 4 
            
     HomeFixOver4[0].append(str(AwOvers[0][3]) + "/" + str(AwOvers[1][3]))
     HomeFixOver4[1].append(len(rfdA))
     HomeFixOver4[2].append(t)
     HomeFixOver4[3].append("HomeOver3")
     HomeFixOver4[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Score 5 
              
     HomeFixOver5[0].append(str(AwOvers[0][4]) + "/" + str(AwOvers[1][4]))
     HomeFixOver5[1].append(len(rfdA))
     HomeFixOver5[2].append(t)
     HomeFixOver5[3].append("HomeOver4")
     HomeFixOver5[4].append("HomeGamesPlayed")
#===============================================================================#
#Home Conceed First Half over 0.5
             
     HomeHalftimeConceedOverZ[0].append(str(AwOvers[2][0])+ "/" +str(AwOvers[3][0]))
     HomeHalftimeConceedOverZ[1].append(len(rfdA))
     HomeHalftimeConceedOverZ[2].append(t)
     HomeHalftimeConceedOverZ[3].append("HomeFirstHalfConceedOverZ")
     HomeHalftimeConceedOverZ[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed First Half over 1.5
              
     HomeHalftimeConceedOverZ2[0].append(str(AwOvers[2][1])+ "/" +str(AwOvers[3][1]))
     HomeHalftimeConceedOverZ2[1].append(len(rfdA))
     HomeHalftimeConceedOverZ2[2].append(t)
     HomeHalftimeConceedOverZ2[3].append("HomeFirstHalfConceedOver1")
     HomeHalftimeConceedOverZ2[4].append("AwayGamesPlayed") 
#===============================================================================#
#Home Conceed First Half over 2.5
               
     HomeHalftimeConceedOverZ3[0].append(str(AwOvers[2][2])+ "/" +str(AwOvers[3][2]))
     HomeHalftimeConceedOverZ3[1].append(len(rfdA))
     HomeHalftimeConceedOverZ3[2].append(t)
     HomeHalftimeConceedOverZ3[3].append("HomeFirstHalfConceedOver2")
     HomeHalftimeConceedOverZ3[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 0.5
              
     HomeSectimeConceedOverZ[0].append(str(AwOvers[4][0])+ "/" +str(AwOvers[5][0]))
     HomeSectimeConceedOverZ[1].append(len(rfdA))
     HomeSectimeConceedOverZ[2].append(t)
     HomeSectimeConceedOverZ[3].append("HomeSecondHalfConceedOverZ")
     HomeSectimeConceedOverZ[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 1.5
              
     HomeSectimeConceedOverZ2[0].append(str(AwOvers[4][1])+ "/" +str(AwOvers[5][1]))
     HomeSectimeConceedOverZ2[1].append(len(rfdA))
     HomeSectimeConceedOverZ2[2].append(t)
     HomeSectimeConceedOverZ2[3].append("HomeSecondHalfConceedOver1")
     HomeSectimeConceedOverZ2[4].append("HomeGamesPlayed") 
#===============================================================================#
#Home Conceed Second Half over 2.5
              
     HomeSectimeConceedOverZ3[0].append(str(AwOvers[4][2])+ "/" +str(AwOvers[5][2]))
     HomeSectimeConceedOverZ3[1].append(len(rfdA))
     HomeSectimeConceedOverZ3[2].append(t)
     HomeSectimeConceedOverZ3[3].append("HomeSecondHalfConceedOver2")
     HomeSectimeConceedOverZ3[4].append("HomeGamesPlayed") 


homeFilter(sql_data)
          #1             #2          #3           #4           #5               #6             #7             #8                #9               #10            #11          #12           #13             #14          #15       #16     #17        #18          #19         #20       #21           #22            #23           #24         #25       #26        #27      #28         #29        #30       #31      #32        #33        #34           #35          #36               #37                      #38                     #39                      #40                        #41                         #42                #43                #44                  #45           #46               #47               #47               #48                  #49                                    #50                                #51                                     #52                                     #53                                #54                                #55                                     #56                                     #57                                #58                                     #59                                #60                                    #61                                 #62                                #63                                     #64                           #65                      #66                           #67                           #68                      #69                   #70                              #71                           #72                                #73                           #74                           #75                                #76                                #77                           #78                           #79                                #80                                #81                            #82                               #83                            #84                               #85                            #86                       #87                           #88                      89                          90                            91                              92                     93                       94                            95                            96                            97                            98                           99                             100                       101                          102                        103                              104                      105                           106                      107                           108                           109                           110                           111                           112                           113                           114                           115                           116                           117                           118                      119                      120                      121                           122                      123                       124                          125                   126                         127                      128                           129                      130                         131                        132                      133                                    

Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ)

createReport(Info,pd)
 