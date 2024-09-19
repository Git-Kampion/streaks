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

insert_stmt2 = "select * from RomaniB order by Round ASC"
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
     ConceedXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"c",5)
     ScoreXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"d",5)
     ScoreFrstHalf = SlPA.ScoreFirstHConceedSecondLayerPerceptron(t,rfdA,"k",5)
     ActionOutpFrstHalf = SlPA.HaltimeFultimeActionOutput(t,rfdA,"k",5)
     ActionOutpFrstHalfOverUnder = SlPA.HaltimeFultimeActionOutputOverUnder(t,rfdA,"k",5)
     FirstHalfTrailSecOutput = SlPA.FirstHalfWinSecHalfOut(t,rfdA,"k",5)
     teamScOneAwayOneHome = mlp.aFHFsc(t,data,"k",5)
     awayTConGoHomeFull = mlp.aConHFsc(t,data,"k",5)
     awayTScorGoHomeFull = mlp.aScorHFsc(t,data,"k",5)
     awayTScorGoHomeScor = mlp.aScorHScor(t,data,"k",5)
     awayTConGoHomeCon = mlp.aConHCon(t,data,"k",5)
     #hBTS = BtOr.Bts(t,rfdA,"k",5)
#================================================================================================================
# Team A/Away Conceed Fulltime 3 Goal, Team A goes home Conceed Fulltime 1 Goal    
#    if len(rfdA) - AwOvers[13][1] <= 1:  
     awayConHomeConceed13[0].append(str(awayTConGoHomeCon[24]) + "/" + str(awayTConGoHomeCon[25]))
     awayConHomeConceed13[1].append(len(rfdA))
     awayConHomeConceed13[2].append(t)        
     awayConHomeConceed13[3].append("TACConc3TeamHConcFull1+")
     awayConHomeConceed13[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Conceed Fulltime 2 Goal       
     awayConHomeConceed14[0].append(str(awayTConGoHomeCon[26]) + "/" + str(awayTConGoHomeCon[27]))
     awayConHomeConceed14[1].append(len(rfdA))
     awayConHomeConceed14[2].append(t)       
     awayConHomeConceed14[3].append("TACConc3TeamHConcFull2+")
     awayConHomeConceed14[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Conceed Fulltime 3 Goal       
     awayConHomeConceed15[0].append(str(awayTConGoHomeCon[28]) + "/" + str(awayTConGoHomeCon[29]))
     awayConHomeConceed15[1].append(len(rfdA))
     awayConHomeConceed15[2].append(t)       
     awayConHomeConceed15[3].append("TACConc3TeamHConcFull3+")
     awayConHomeConceed15[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes Conceed Fulltime 4 Goal       
     awayConHomeConceed16[0].append(str(awayTConGoHomeCon[30]) + "/" + str(awayTConGoHomeCon[31]))
     awayConHomeConceed16[1].append(len(rfdA))
     awayConHomeConceed16[2].append(t)       
     awayConHomeConceed16[3].append("TACConc3TeamHConcFull4+")
     awayConHomeConceed16[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 1 Goal, Team A goes home Conceed Fulltime 1 Goal     
     awayConHomeConceed[0].append(str(awayTConGoHomeCon[0]) + "/" + str(awayTConGoHomeCon[1]))
     awayConHomeConceed[1].append(len(rfdA))
     awayConHomeConceed[2].append(t)        
     awayConHomeConceed[3].append("TACConc1TeamHConcFull1+")
     awayConHomeConceed[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes home Conceed Fulltime 2 Goal       
     awayConHomeConceed2[0].append(str(awayTConGoHomeCon[2]) + "/" + str(awayTConGoHomeCon[3]))
     awayConHomeConceed2[1].append(len(rfdA))
     awayConHomeConceed2[2].append(t)       
     awayConHomeConceed2[3].append("TACConc1TeamHConcFull2+")
     awayConHomeConceed2[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes home Conceed Fulltime 3 Goal       
     awayConHomeConceed3[0].append(str(awayTConGoHomeCon[4]) + "/" + str(awayTConGoHomeCon[5]))
     awayConHomeConceed3[1].append(len(rfdA))
     awayConHomeConceed3[2].append(t)       
     awayConHomeConceed3[3].append("TACConc1TeamHConcFull3+")
     awayConHomeConceed3[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes Conceed Fulltime 4 Goal       
     awayConHomeConceed4[0].append(str(awayTConGoHomeCon[6]) + "/" + str(awayTConGoHomeCon[7]))
     awayConHomeConceed4[1].append(len(rfdA))
     awayConHomeConceed4[2].append(t)       
     awayConHomeConceed4[3].append("TACConc1TeamHConcFull4+")
     awayConHomeConceed4[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 2 Goal, Team A goes home Conceed Fulltime 1 Goal     
     awayConHomeConceed5[0].append(str(awayTConGoHomeCon[8]) + "/" + str(awayTConGoHomeCon[9]))
     awayConHomeConceed5[1].append(len(rfdA))
     awayConHomeConceed5[2].append(t)        
     awayConHomeConceed5[3].append("TACConc2TeamHConcFull1+")
     awayConHomeConceed5[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes home Conceed Fulltime 2 Goal       
     awayConHomeConceed6[0].append(str(awayTConGoHomeCon[10]) + "/" + str(awayTConGoHomeCon[11]))
     awayConHomeConceed6[1].append(len(rfdA))
     awayConHomeConceed6[2].append(t)       
     awayConHomeConceed6[3].append("TACConc2TeamHConcFull2+")
     awayConHomeConceed6[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes home Conceed Fulltime 3 Goal       
     awayConHomeConceed7[0].append(str(awayTConGoHomeCon[12]) + "/" + str(awayTConGoHomeCon[13]))
     awayConHomeConceed7[1].append(len(rfdA))
     awayConHomeConceed7[2].append(t)       
     awayConHomeConceed7[3].append("TACConc2TeamHConcFull3+")
     awayConHomeConceed7[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes Conceed Fulltime 4 Goal       
     awayConHomeConceed8[0].append(str(awayTConGoHomeCon[14]) + "/" + str(awayTConGoHomeCon[15]))
     awayConHomeConceed8[1].append(len(rfdA))
     awayConHomeConceed8[2].append(t)       
     awayConHomeConceed8[3].append("TACConc2TeamHConcFull4+")
     awayConHomeConceed8[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 3 Goal, Team A goes home Conceed Fulltime 1 Goal     
     awayConHomeConceed9[0].append(str(awayTConGoHomeCon[16]) + "/" + str(awayTConGoHomeCon[17]))
     awayConHomeConceed9[1].append(len(rfdA))
     awayConHomeConceed9[2].append(t)        
     awayConHomeConceed9[3].append("TACConc3TeamHConcFull1+")
     awayConHomeConceed9[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Conceed Fulltime 2 Goal       
     awayConHomeConceed10[0].append(str(awayTConGoHomeCon[18]) + "/" + str(awayTConGoHomeCon[19]))
     awayConHomeConceed10[1].append(len(rfdA))
     awayConHomeConceed10[2].append(t)       
     awayConHomeConceed10[3].append("TACConc3TeamHConcFull2+")
     awayConHomeConceed10[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Conceed Fulltime 3 Goal       
     awayConHomeConceed11[0].append(str(awayTConGoHomeCon[20]) + "/" + str(awayTConGoHomeCon[21]))
     awayConHomeConceed11[1].append(len(rfdA))
     awayConHomeConceed11[2].append(t)       
     awayConHomeConceed11[3].append("TACConc3TeamHConcFull3+")
     awayConHomeConceed11[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes Conceed Fulltime 4 Goal       
     awayConHomeConceed12[0].append(str(awayTConGoHomeCon[22]) + "/" + str(awayTConGoHomeCon[23]))
     awayConHomeConceed12[1].append(len(rfdA))
     awayConHomeConceed12[2].append(t)       
     awayConHomeConceed12[3].append("TACConc3TeamHConcFull4+")
     awayConHomeConceed12[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 4 Goal, Team A goes home Conceed Fulltime 1 Goal     
     awayConHomeConceed13[0].append(str(awayTConGoHomeCon[24]) + "/" + str(awayTConGoHomeCon[25]))
     awayConHomeConceed13[1].append(len(rfdA))
     awayConHomeConceed13[2].append(t)        
     awayConHomeConceed13[3].append("TACConc4TeamHConcFull1+")
     awayConHomeConceed13[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes home Conceed Fulltime 2 Goal       
     awayConHomeConceed14[0].append(str(awayTConGoHomeCon[26]) + "/" + str(awayTConGoHomeCon[27]))
     awayConHomeConceed14[1].append(len(rfdA))
     awayConHomeConceed14[2].append(t)       
     awayConHomeConceed14[3].append("TACConc4TeamHConcFull2+")
     awayConHomeConceed14[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes home Conceed Fulltime 3 Goal       
     awayConHomeConceed15[0].append(str(awayTConGoHomeCon[28]) + "/" + str(awayTConGoHomeCon[29]))
     awayConHomeConceed15[1].append(len(rfdA))
     awayConHomeConceed15[2].append(t)       
     awayConHomeConceed15[3].append("TACConc4TeamHConcFull3+")
     awayConHomeConceed15[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes Conceed Fulltime 4 Goal       
     awayConHomeConceed16[0].append(str(awayTConGoHomeCon[30]) + "/" + str(awayTConGoHomeCon[31]))
     awayConHomeConceed16[1].append(len(rfdA))
     awayConHomeConceed16[2].append(t)       
     awayConHomeConceed16[3].append("TACConc4TeamHConcFull4+")
     awayConHomeConceed16[4].append("HomeGamesPatt")

 #================================================================================================================
# Team A/Away Score Fulltime 1 Goal, Team A goes home Score Fulltime 1 Goal     
     awayScorOvUvHomeScorOvUv[0].append(str(awayTScorGoHomeScor[0]) + "/" + str(awayTScorGoHomeScor[1]))
     awayScorOvUvHomeScorOvUv[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv[2].append(t)        
     awayScorOvUvHomeScorOvUv[3].append("TACScor1TeamHScoreFull1+")
     awayScorOvUvHomeScorOvUv[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes home Score Fulltime 2 Goal       
     awayScorOvUvHomeScorOvUv2[0].append(str(awayTScorGoHomeScor[2]) + "/" + str(awayTScorGoHomeScor[3]))
     awayScorOvUvHomeScorOvUv2[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv2[2].append(t)       
     awayScorOvUvHomeScorOvUv2[3].append("TACScor1TeamHScoreFull2+")
     awayScorOvUvHomeScorOvUv2[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes home Score Fulltime 3 Goal       
     awayScorOvUvHomeScorOvUv3[0].append(str(awayTScorGoHomeScor[4]) + "/" + str(awayTScorGoHomeScor[5]))
     awayScorOvUvHomeScorOvUv3[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv3[2].append(t)       
     awayScorOvUvHomeScorOvUv3[3].append("TACScor1TeamHScoreFull3+")
     awayScorOvUvHomeScorOvUv3[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes Score Fulltime 4 Goal       
     awayScorOvUvHomeScorOvUv4[0].append(str(awayTScorGoHomeScor[6]) + "/" + str(awayTScorGoHomeScor[7]))
     awayScorOvUvHomeScorOvUv4[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv4[2].append(t)       
     awayScorOvUvHomeScorOvUv4[3].append("TACScor1TeamHScoreFull4+")
     awayScorOvUvHomeScorOvUv4[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 2 Goal, Team A goes home Score Fulltime 1 Goal     
     awayScorOvUvHomeScorOvUv5[0].append(str(awayTScorGoHomeScor[8]) + "/" + str(awayTScorGoHomeScor[9]))
     awayScorOvUvHomeScorOvUv5[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv5[2].append(t)        
     awayScorOvUvHomeScorOvUv5[3].append("TACScor2TeamHScoreFull1+")
     awayScorOvUvHomeScorOvUv5[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes home Score Fulltime 2 Goal       
     awayScorOvUvHomeScorOvUv6[0].append(str(awayTScorGoHomeScor[10]) + "/" + str(awayTScorGoHomeScor[11]))
     awayScorOvUvHomeScorOvUv6[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv6[2].append(t)       
     awayScorOvUvHomeScorOvUv6[3].append("TACScor2TeamHScoreFull2+")
     awayScorOvUvHomeScorOvUv6[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes home Score Fulltime 3 Goal       
     awayScorOvUvHomeScorOvUv7[0].append(str(awayTScorGoHomeScor[12]) + "/" + str(awayTScorGoHomeScor[13]))
     awayScorOvUvHomeScorOvUv7[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv7[2].append(t)       
     awayScorOvUvHomeScorOvUv7[3].append("TACScor2TeamHScoreFull3+")
     awayScorOvUvHomeScorOvUv7[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes Score Fulltime 4 Goal       
     awayScorOvUvHomeScorOvUv8[0].append(str(awayTScorGoHomeScor[14]) + "/" + str(awayTScorGoHomeScor[15]))
     awayScorOvUvHomeScorOvUv8[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv8[2].append(t)       
     awayScorOvUvHomeScorOvUv8[3].append("TACScor2TeamHScoreFull4+")
     awayScorOvUvHomeScorOvUv8[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 3 Goal, Team A goes home Score Fulltime 1 Goal     
     awayScorOvUvHomeScorOvUv9[0].append(str(awayTScorGoHomeScor[16]) + "/" + str(awayTScorGoHomeScor[17]))
     awayScorOvUvHomeScorOvUv9[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv9[2].append(t)        
     awayScorOvUvHomeScorOvUv9[3].append("TACScor3TeamHScoreFull1+")
     awayScorOvUvHomeScorOvUv9[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes home Score Fulltime 2 Goal       
     awayScorOvUvHomeScorOvUv10[0].append(str(awayTScorGoHomeScor[18]) + "/" + str(awayTScorGoHomeScor[19]))
     awayScorOvUvHomeScorOvUv10[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv10[2].append(t)       
     awayScorOvUvHomeScorOvUv10[3].append("TACScor3TeamHScoreFull2+")
     awayScorOvUvHomeScorOvUv10[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes home Score Fulltime 3 Goal       
     awayScorOvUvHomeScorOvUv11[0].append(str(awayTScorGoHomeScor[20]) + "/" + str(awayTScorGoHomeScor[21]))
     awayScorOvUvHomeScorOvUv11[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv11[2].append(t)       
     awayScorOvUvHomeScorOvUv11[3].append("TACScor3TeamHScoreFull3+")
     awayScorOvUvHomeScorOvUv11[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes Score Fulltime 4 Goal       
     awayScorOvUvHomeScorOvUv12[0].append(str(awayTScorGoHomeScor[22]) + "/" + str(awayTScorGoHomeScor[23]))
     awayScorOvUvHomeScorOvUv12[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv12[2].append(t)       
     awayScorOvUvHomeScorOvUv12[3].append("TACScor3TeamHScoreFull4+")
     awayScorOvUvHomeScorOvUv12[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 4 Goal, Team A goes home Score Fulltime 1 Goal     
     awayScorOvUvHomeScorOvUv13[0].append(str(awayTScorGoHomeScor[24]) + "/" + str(awayTScorGoHomeScor[25]))
     awayScorOvUvHomeScorOvUv13[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv13[2].append(t)        
     awayScorOvUvHomeScorOvUv13[3].append("TACScor4TeamHScoreFull1+")
     awayScorOvUvHomeScorOvUv13[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes home Score Fulltime 2 Goal       
     awayScorOvUvHomeScorOvUv14[0].append(str(awayTScorGoHomeScor[26]) + "/" + str(awayTScorGoHomeScor[27]))
     awayScorOvUvHomeScorOvUv14[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv14[2].append(t)       
     awayScorOvUvHomeScorOvUv14[3].append("TACScor4TeamHScoreFull2+")
     awayScorOvUvHomeScorOvUv14[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes home Score Fulltime 3 Goal       
     awayScorOvUvHomeScorOvUv15[0].append(str(awayTScorGoHomeScor[28]) + "/" + str(awayTScorGoHomeScor[29]))
     awayScorOvUvHomeScorOvUv15[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv15[2].append(t)       
     awayScorOvUvHomeScorOvUv15[3].append("TACScor4TeamHScoreFull3+")
     awayScorOvUvHomeScorOvUv15[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes Score Fulltime 4 Goal       
     awayScorOvUvHomeScorOvUv16[0].append(str(awayTScorGoHomeScor[30]) + "/" + str(awayTScorGoHomeScor[31]))
     awayScorOvUvHomeScorOvUv16[1].append(len(rfdA))
     awayScorOvUvHomeScorOvUv16[2].append(t)       
     awayScorOvUvHomeScorOvUv16[3].append("TACScor4TeamHScoreFull4+")
     awayScorOvUvHomeScorOvUv16[4].append("HomeGamesPatt")
     #================================================================================================================
# Team A/Away Score Fulltime 1 Goal, Team A goes home Fulltime Res     
     awayScorOvUvHomeConceedOvUv[0].append(str(awayTScorGoHomeFull[0]) + "/" + str(awayTScorGoHomeFull[1]))
     awayScorOvUvHomeConceedOvUv[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv[2].append(t)        
     awayScorOvUvHomeConceedOvUv[3].append("TACScor1TeamHFullTimeRes1+")
     awayScorOvUvHomeConceedOvUv[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv2[0].append(str(awayTScorGoHomeFull[2]) + "/" + str(awayTScorGoHomeFull[3]))
     awayScorOvUvHomeConceedOvUv2[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv2[2].append(t)       
     awayScorOvUvHomeConceedOvUv2[3].append("TACScor1TeamHFullTimeRes2+")
     awayScorOvUvHomeConceedOvUv2[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv3[0].append(str(awayTScorGoHomeFull[4]) + "/" + str(awayTScorGoHomeFull[5]))
     awayScorOvUvHomeConceedOvUv3[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv3[2].append(t)       
     awayScorOvUvHomeConceedOvUv3[3].append("TACScor1TeamHFullTimeRes3+")
     awayScorOvUvHomeConceedOvUv3[4].append("HomeGamesPatt")
# Team A/Away Score 1 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv4[0].append(str(awayTScorGoHomeFull[6]) + "/" + str(awayTScorGoHomeFull[7]))
     awayScorOvUvHomeConceedOvUv4[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv4[2].append(t)       
     awayScorOvUvHomeConceedOvUv4[3].append("TACScor1TeamHFullTimeRes4+")
     awayScorOvUvHomeConceedOvUv4[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 2 Goal, Team A goes home Fulltime Res     
     awayScorOvUvHomeConceedOvUv5[0].append(str(awayTScorGoHomeFull[8]) + "/" + str(awayTScorGoHomeFull[9]))
     awayScorOvUvHomeConceedOvUv5[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv5[2].append(t)        
     awayScorOvUvHomeConceedOvUv5[3].append("TACScor2TeamHFullTimeRes1+")
     awayScorOvUvHomeConceedOvUv5[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv6[0].append(str(awayTScorGoHomeFull[10]) + "/" + str(awayTScorGoHomeFull[11]))
     awayScorOvUvHomeConceedOvUv6[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv6[2].append(t)       
     awayScorOvUvHomeConceedOvUv6[3].append("TACScor2TeamHFullTimeRes2+")
     awayScorOvUvHomeConceedOvUv6[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv7[0].append(str(awayTScorGoHomeFull[12]) + "/" + str(awayTScorGoHomeFull[13]))
     awayScorOvUvHomeConceedOvUv7[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv7[2].append(t)       
     awayScorOvUvHomeConceedOvUv7[3].append("TACScor2TeamHFullTimeRes3+")
     awayScorOvUvHomeConceedOvUv7[4].append("HomeGamesPatt")
# Team A/Away Score 2 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv8[0].append(str(awayTScorGoHomeFull[14]) + "/" + str(awayTScorGoHomeFull[15]))
     awayScorOvUvHomeConceedOvUv8[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv8[2].append(t)       
     awayScorOvUvHomeConceedOvUv8[3].append("TACScor2TeamHFullTimeRes4+")
     awayScorOvUvHomeConceedOvUv8[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 3 Goal, Team A goes home Fulltime Res     
     awayScorOvUvHomeConceedOvUv9[0].append(str(awayTScorGoHomeFull[16]) + "/" + str(awayTScorGoHomeFull[17]))
     awayScorOvUvHomeConceedOvUv9[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv9[2].append(t)        
     awayScorOvUvHomeConceedOvUv9[3].append("TACScor3TeamHFullTimeRes1+")
     awayScorOvUvHomeConceedOvUv9[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv10[0].append(str(awayTScorGoHomeFull[18]) + "/" + str(awayTScorGoHomeFull[19]))
     awayScorOvUvHomeConceedOvUv10[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv10[2].append(t)       
     awayScorOvUvHomeConceedOvUv10[3].append("TACScor3TeamHFullTimeRes2+")
     awayScorOvUvHomeConceedOvUv10[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv11[0].append(str(awayTScorGoHomeFull[20]) + "/" + str(awayTScorGoHomeFull[21]))
     awayScorOvUvHomeConceedOvUv11[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv11[2].append(t)       
     awayScorOvUvHomeConceedOvUv11[3].append("TACScor3TeamHFullTimeRes3+")
     awayScorOvUvHomeConceedOvUv11[4].append("HomeGamesPatt")
# Team A/Away Score 3 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv12[0].append(str(awayTScorGoHomeFull[22]) + "/" + str(awayTScorGoHomeFull[23]))
     awayScorOvUvHomeConceedOvUv12[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv12[2].append(t)       
     awayScorOvUvHomeConceedOvUv12[3].append("TACScor3TeamHFullTimeRes4+")
     awayScorOvUvHomeConceedOvUv12[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Score Fulltime 4 Goal, Team A goes home Fulltime Res     
     awayScorOvUvHomeConceedOvUv13[0].append(str(awayTScorGoHomeFull[24]) + "/" + str(awayTScorGoHomeFull[25]))
     awayScorOvUvHomeConceedOvUv13[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv13[2].append(t)        
     awayScorOvUvHomeConceedOvUv13[3].append("TACScor4TeamHFullTimeRes1+")
     awayScorOvUvHomeConceedOvUv13[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv14[0].append(str(awayTScorGoHomeFull[26]) + "/" + str(awayTScorGoHomeFull[27]))
     awayScorOvUvHomeConceedOvUv14[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv14[2].append(t)       
     awayScorOvUvHomeConceedOvUv14[3].append("TACScor4TeamHFullTimeRes2+")
     awayScorOvUvHomeConceedOvUv14[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv15[0].append(str(awayTScorGoHomeFull[28]) + "/" + str(awayTScorGoHomeFull[29]))
     awayScorOvUvHomeConceedOvUv15[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv15[2].append(t)       
     awayScorOvUvHomeConceedOvUv15[3].append("TACScor4TeamHFullTimeRes3+")
     awayScorOvUvHomeConceedOvUv15[4].append("HomeGamesPatt")
# Team A/Away Score 4 Goal, Team A goes home Fulltime Res       
     awayScorOvUvHomeConceedOvUv16[0].append(str(awayTScorGoHomeFull[30]) + "/" + str(awayTScorGoHomeFull[31]))
     awayScorOvUvHomeConceedOvUv16[1].append(len(rfdA))
     awayScorOvUvHomeConceedOvUv16[2].append(t)       
     awayScorOvUvHomeConceedOvUv16[3].append("TACScor4TeamHFullTimeRes4+")
     awayScorOvUvHomeConceedOvUv16[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 1 Goal, Team A goes home Fulltime Res     
     awayConOvUvHomeConceedOvUv[0].append(str(awayTConGoHomeFull[0]) + "/" + str(awayTConGoHomeFull[1]))
     awayConOvUvHomeConceedOvUv[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv[2].append(t)        
     awayConOvUvHomeConceedOvUv[3].append("TACon1TeamHFullTimeRes1+")
     awayConOvUvHomeConceedOvUv[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv2[0].append(str(awayTConGoHomeFull[2]) + "/" + str(awayTConGoHomeFull[3]))
     awayConOvUvHomeConceedOvUv2[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv2[2].append(t)       
     awayConOvUvHomeConceedOvUv2[3].append("TACon1TeamHFullTimeRes2+")
     awayConOvUvHomeConceedOvUv2[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv3[0].append(str(awayTConGoHomeFull[4]) + "/" + str(awayTConGoHomeFull[5]))
     awayConOvUvHomeConceedOvUv3[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv3[2].append(t)       
     awayConOvUvHomeConceedOvUv3[3].append("TACon1TeamHFullTimeRes3+")
     awayConOvUvHomeConceedOvUv3[4].append("HomeGamesPatt")
# Team A/Away Conceed 1 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv4[0].append(str(awayTConGoHomeFull[6]) + "/" + str(awayTConGoHomeFull[7]))
     awayConOvUvHomeConceedOvUv4[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv4[2].append(t)       
     awayConOvUvHomeConceedOvUv4[3].append("TACon1TeamHFullTimeRes4+")
     awayConOvUvHomeConceedOvUv4[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 2 Goal, Team A goes home Fulltime Res     
     awayConOvUvHomeConceedOvUv5[0].append(str(awayTConGoHomeFull[8]) + "/" + str(awayTConGoHomeFull[9]))
     awayConOvUvHomeConceedOvUv5[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv5[2].append(t)        
     awayConOvUvHomeConceedOvUv5[3].append("TACon2TeamHFullTimeRes1+")
     awayConOvUvHomeConceedOvUv5[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv6[0].append(str(awayTConGoHomeFull[10]) + "/" + str(awayTConGoHomeFull[11]))
     awayConOvUvHomeConceedOvUv6[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv6[2].append(t)       
     awayConOvUvHomeConceedOvUv6[3].append("TACon2TeamHFullTimeRes2+")
     awayConOvUvHomeConceedOvUv6[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv7[0].append(str(awayTConGoHomeFull[12]) + "/" + str(awayTConGoHomeFull[13]))
     awayConOvUvHomeConceedOvUv7[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv7[2].append(t)       
     awayConOvUvHomeConceedOvUv7[3].append("TACon2TeamHFullTimeRes3+")
     awayConOvUvHomeConceedOvUv7[4].append("HomeGamesPatt")
# Team A/Away Conceed 2 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv8[0].append(str(awayTConGoHomeFull[14]) + "/" + str(awayTConGoHomeFull[15]))
     awayConOvUvHomeConceedOvUv8[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv8[2].append(t)       
     awayConOvUvHomeConceedOvUv8[3].append("TACon2TeamHFullTimeRes4+")
     awayConOvUvHomeConceedOvUv8[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 3 Goal, Team A goes home Fulltime Res     
     awayConOvUvHomeConceedOvUv9[0].append(str(awayTConGoHomeFull[16]) + "/" + str(awayTConGoHomeFull[17]))
     awayConOvUvHomeConceedOvUv9[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv9[2].append(t)        
     awayConOvUvHomeConceedOvUv9[3].append("TACon3TeamHFullTimeRes1+")
     awayConOvUvHomeConceedOvUv9[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv10[0].append(str(awayTConGoHomeFull[18]) + "/" + str(awayTConGoHomeFull[19]))
     awayConOvUvHomeConceedOvUv10[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv10[2].append(t)       
     awayConOvUvHomeConceedOvUv10[3].append("TACon3TeamHFullTimeRes2+")
     awayConOvUvHomeConceedOvUv10[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv11[0].append(str(awayTConGoHomeFull[20]) + "/" + str(awayTConGoHomeFull[21]))
     awayConOvUvHomeConceedOvUv11[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv11[2].append(t)       
     awayConOvUvHomeConceedOvUv11[3].append("TACon3TeamHFullTimeRes3+")
     awayConOvUvHomeConceedOvUv11[4].append("HomeGamesPatt")
# Team A/Away Conceed 3 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv12[0].append(str(awayTConGoHomeFull[22]) + "/" + str(awayTConGoHomeFull[23]))
     awayConOvUvHomeConceedOvUv12[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv12[2].append(t)       
     awayConOvUvHomeConceedOvUv12[3].append("TACon3TeamHFullTimeRes4+")
     awayConOvUvHomeConceedOvUv12[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Conceed Fulltime 4 Goal, Team A goes home Fulltime Res     
     awayConOvUvHomeConceedOvUv13[0].append(str(awayTConGoHomeFull[24]) + "/" + str(awayTConGoHomeFull[25]))
     awayConOvUvHomeConceedOvUv13[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv13[2].append(t)        
     awayConOvUvHomeConceedOvUv13[3].append("TACon4TeamHFullTimeRes1+")
     awayConOvUvHomeConceedOvUv13[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv14[0].append(str(awayTConGoHomeFull[26]) + "/" + str(awayTConGoHomeFull[27]))
     awayConOvUvHomeConceedOvUv14[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv14[2].append(t)       
     awayConOvUvHomeConceedOvUv14[3].append("TACon4TeamHFullTimeRes2+")
     awayConOvUvHomeConceedOvUv14[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv15[0].append(str(awayTConGoHomeFull[28]) + "/" + str(awayTConGoHomeFull[29]))
     awayConOvUvHomeConceedOvUv15[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv15[2].append(t)       
     awayConOvUvHomeConceedOvUv15[3].append("TACon4TeamHFullTimeRes3+")
     awayConOvUvHomeConceedOvUv15[4].append("HomeGamesPatt")
# Team A/Away Conceed 4 Goal, Team A goes home Fulltime Res       
     awayConOvUvHomeConceedOvUv16[0].append(str(awayTConGoHomeFull[30]) + "/" + str(awayTConGoHomeFull[31]))
     awayConOvUvHomeConceedOvUv16[1].append(len(rfdA))
     awayConOvUvHomeConceedOvUv16[2].append(t)       
     awayConOvUvHomeConceedOvUv16[3].append("TACon4TeamHFullTimeRes4+")
     awayConOvUvHomeConceedOvUv16[4].append("HomeGamesPatt")
#================================================================================================================
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv[0].append(str(teamScOneAwayOneHome[0]) + "/" + str(teamScOneAwayOneHome[1]))
     awayConceedOvUvHomeConceedOvUv[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv[2].append(t)        
     awayConceedOvUvHomeConceedOvUv[3].append("TAFTTeamHFullTimeRes1+")
     awayConceedOvUvHomeConceedOvUv[4].append("HomeGamesPlayed")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv2[0].append(str(teamScOneAwayOneHome[2]) + "/" + str(teamScOneAwayOneHome[3]))
     awayConceedOvUvHomeConceedOvUv2[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv2[2].append(t)       
     awayConceedOvUvHomeConceedOvUv2[3].append("TAFT1TeamHFullTimeRes2+")
     awayConceedOvUvHomeConceedOvUv2[4].append("HomeGamesPatt")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv3[0].append(str(teamScOneAwayOneHome[4]) + "/" + str(teamScOneAwayOneHome[5]))
     awayConceedOvUvHomeConceedOvUv3[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv3[2].append(t)       
     awayConceedOvUvHomeConceedOvUv3[3].append("TAFT1TeamHFullTimeRes3+")
     awayConceedOvUvHomeConceedOvUv3[4].append("HomeGamesPatt")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv4[0].append(str(teamScOneAwayOneHome[6]) + "/" + str(teamScOneAwayOneHome[7]))
     awayConceedOvUvHomeConceedOvUv4[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv4[2].append(t)       
     awayConceedOvUvHomeConceedOvUv4[3].append("TAFT1TeamHFullTimeRes4+")
     awayConceedOvUvHomeConceedOvUv4[4].append("HomeGamesPatt")
#============================================================================================
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv5[0].append(str(teamScOneAwayOneHome[8]) + "/" + str(teamScOneAwayOneHome[9]))
     awayConceedOvUvHomeConceedOvUv5[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv5[2].append(t)         
     awayConceedOvUvHomeConceedOvUv5[3].append("TAFT2TeamHFullTimeRes1+")
     awayConceedOvUvHomeConceedOvUv5[4].append("HomeGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res        
     awayConceedOvUvHomeConceedOvUv6[0].append(str(teamScOneAwayOneHome[10]) + "/" + str(teamScOneAwayOneHome[11]))
     awayConceedOvUvHomeConceedOvUv6[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv6[2].append(t)         
     awayConceedOvUvHomeConceedOvUv6[3].append("TAFT2TeamHFullTimeRes2+")
     awayConceedOvUvHomeConceedOvUv6[4].append("HomeGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv7[0].append(str(teamScOneAwayOneHome[12]) + "/" + str(teamScOneAwayOneHome[13]))
     awayConceedOvUvHomeConceedOvUv7[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv7[2].append(t)       
     awayConceedOvUvHomeConceedOvUv7[3].append("TAFT2TeamHFullTimeRes3+")
     awayConceedOvUvHomeConceedOvUv7[4].append("HomeGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res        
     awayConceedOvUvHomeConceedOvUv8[0].append(str(teamScOneAwayOneHome[14]) + "/" + str(teamScOneAwayOneHome[15]))
     awayConceedOvUvHomeConceedOvUv8[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv8[2].append(t)         
     awayConceedOvUvHomeConceedOvUv8[3].append("TAFT2TeamHFullTimeRes4+")
     awayConceedOvUvHomeConceedOvUv8[4].append("HomeGamesPatt")
     #============================================================================================
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv9[0].append(str(teamScOneAwayOneHome[16]) + "/" + str(teamScOneAwayOneHome[17]))
     awayConceedOvUvHomeConceedOvUv9[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv9[2].append(t)        
     awayConceedOvUvHomeConceedOvUv9[3].append("TAFT3TeamHFullTimeRes1+")
     awayConceedOvUvHomeConceedOvUv9[4].append("HomeGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv10[0].append(str(teamScOneAwayOneHome[18]) + "/" + str(teamScOneAwayOneHome[19]))
     awayConceedOvUvHomeConceedOvUv10[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv10[2].append(t)        
     awayConceedOvUvHomeConceedOvUv10[3].append("TAFT3TeamHFullTimeRes2+")
     awayConceedOvUvHomeConceedOvUv10[4].append("HomeGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res   
     awayConceedOvUvHomeConceedOvUv11[0].append(str(teamScOneAwayOneHome[20]) + "/" + str(teamScOneAwayOneHome[21]))    
     awayConceedOvUvHomeConceedOvUv11[1].append(len(rfdA))   
     awayConceedOvUvHomeConceedOvUv11[2].append(t)       
     awayConceedOvUvHomeConceedOvUv11[3].append("TAFT3TeamHFullTimeRes3+")
     awayConceedOvUvHomeConceedOvUv11[4].append("HomeGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res        
     awayConceedOvUvHomeConceedOvUv12[0].append(str(teamScOneAwayOneHome[22]) + "/" + str(teamScOneAwayOneHome[23])) 
     awayConceedOvUvHomeConceedOvUv12[1].append(len(rfdA)) 
     awayConceedOvUvHomeConceedOvUv12[2].append(t)         
     awayConceedOvUvHomeConceedOvUv12[3].append("TAFT3TeamHFullTimeRes4+")
     awayConceedOvUvHomeConceedOvUv12[4].append("HomeGamesPatt")
#============================================================================================
# Team A/Away Fulltime 4 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv13[0].append(str(teamScOneAwayOneHome[24]) + "/" + str(teamScOneAwayOneHome[25]))
     awayConceedOvUvHomeConceedOvUv13[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv13[2].append(t)        
     awayConceedOvUvHomeConceedOvUv13[3].append("TAFT4TeamHFullTimeRes1+")
     awayConceedOvUvHomeConceedOvUv13[4].append("HomeGamesPatt")
# Team A/Away Fulltime 4 Goal, Team A goes home Fulltime Res       
     awayConceedOvUvHomeConceedOvUv14[0].append(str(teamScOneAwayOneHome[26]) + "/" + str(teamScOneAwayOneHome[27]))
     awayConceedOvUvHomeConceedOvUv14[1].append(len(rfdA))
     awayConceedOvUvHomeConceedOvUv14[2].append(t)        
     awayConceedOvUvHomeConceedOvUv14[3].append("TAFT4TeamHFullTimeRes2+")
     awayConceedOvUvHomeConceedOvUv14[4].append("HomeGamesPatt")
# Team A/Away Fulltime 4 Goal, Team A goes home Fulltime Res   
     awayConceedOvUvHomeConceedOvUv15[0].append(str(teamScOneAwayOneHome[28]) + "/" + str(teamScOneAwayOneHome[29]))    
     awayConceedOvUvHomeConceedOvUv15[1].append(len(rfdA))   
     awayConceedOvUvHomeConceedOvUv15[2].append(t)       
     awayConceedOvUvHomeConceedOvUv15[3].append("TAFT4TeamHFullTimeRes3+")
     awayConceedOvUvHomeConceedOvUv15[4].append("HomeGamesPatt")
# Team A/Away Fulltime 4 Goal, Team A goes home Fulltime Res        
     awayConceedOvUvHomeConceedOvUv16[0].append(str(teamScOneAwayOneHome[30]) + "/" + str(teamScOneAwayOneHome[31])) 
     awayConceedOvUvHomeConceedOvUv16[1].append(len(rfdA)) 
     awayConceedOvUvHomeConceedOvUv16[2].append(t)         
     awayConceedOvUvHomeConceedOvUv16[3].append("TAFT4TeamHFullTimeRes4+")
     awayConceedOvUvHomeConceedOvUv16[4].append("HomeGamesPatt")
#=====================================================================================================#

#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Away Over Zero Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[14] :          
     FirstHAwayWinSecHHomeScore1[0].append(str(FirstHalfTrailSecOutput[6])+ "/" +str(FirstHalfTrailSecOutput[7]))
     FirstHAwayWinSecHHomeScore1[1].append(len(rfdA))
     FirstHAwayWinSecHHomeScore1[2].append(t)
     FirstHAwayWinSecHHomeScore1[3].append("FirstHHomeWinSecHAwayScore1")
     FirstHAwayWinSecHHomeScore1[4].append("HomeGamesPlayed")
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Away Over One Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[14] :          
     FirstHAwayWinSecHHomeScore2[0].append(str(FirstHalfTrailSecOutput[8])+ "/" +str(FirstHalfTrailSecOutput[9]))
     FirstHAwayWinSecHHomeScore2[1].append(len(rfdA))
     FirstHAwayWinSecHHomeScore2[2].append(t)
     FirstHAwayWinSecHHomeScore2[3].append("FirstHHomeWinSecHAwayScore2")
     FirstHAwayWinSecHHomeScore2[4].append("HomeGamesPlayed")
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Away Over Two Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[14] :          
     FirstHAwayWinSecHHomeScore3[0].append(str(FirstHalfTrailSecOutput[10])+ "/" +str(FirstHalfTrailSecOutput[11]))
     FirstHAwayWinSecHHomeScore3[1].append(len(rfdA))
     FirstHAwayWinSecHHomeScore3[2].append(t)
     FirstHAwayWinSecHHomeScore3[3].append("FirstHomeWinSecHAwayScore3")
     FirstHAwayWinSecHHomeScore3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Home Over Zero Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[6] :          
     FirstHAwayWinSecHAwayScore1[0].append(str(FirstHalfTrailSecOutput[14])+ "/" +str(FirstHalfTrailSecOutput[15]))
     FirstHAwayWinSecHAwayScore1[1].append(len(rfdA))
     FirstHAwayWinSecHAwayScore1[2].append(t)
     FirstHAwayWinSecHAwayScore1[3].append("FirstHHomeWinSecHHomeScore1")
     FirstHAwayWinSecHAwayScore1[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Home Over one Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[8] :          
     FirstHAwayWinSecHAwayScore2[0].append(str(FirstHalfTrailSecOutput[16])+ "/" +str(FirstHalfTrailSecOutput[17]))
     FirstHAwayWinSecHAwayScore2[1].append(len(rfdA))
     FirstHAwayWinSecHAwayScore2[2].append(t)
     FirstHAwayWinSecHAwayScore2[3].append("FirstHHomeWinSecHHomeScore2")
     FirstHAwayWinSecHAwayScore2[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Home Over Two Sechnd HAlf
     #if len(rfdA) - FirstHalfTrailSecOutput[10] :          
     FirstHAwayWinSecHAwayScore3[0].append(str(FirstHalfTrailSecOutput[18])+ "/" +str(FirstHalfTrailSecOutput[19]))
     FirstHAwayWinSecHAwayScore3[1].append(len(rfdA))
     FirstHAwayWinSecHAwayScore3[2].append(t)
     FirstHAwayWinSecHAwayScore3[3].append("FirstHHomeWinSecHHomeScore3")
     FirstHAwayWinSecHAwayScore3[4].append("HomeGamesPlayed")

#=====================================================================================================#
#Home HalftimeAction Winning,Second Half output: Home leading Halftime//Home WinDraw vs AwayDraw
     #if len(rfdA) - FirstHalfTrailSecOutput[2] :          
     FirstHalfAwayWinSecondHalfHomeWindraw[0].append(str(FirstHalfTrailSecOutput[2])+ "/" +str(FirstHalfTrailSecOutput[3]))
     FirstHalfAwayWinSecondHalfHomeWindraw[1].append(len(rfdA))
     FirstHalfAwayWinSecondHalfHomeWindraw[2].append(t)
     FirstHalfAwayWinSecondHalfHomeWindraw[3].append("FirstHalfHomeWinSecHalfAwayWD")
     FirstHalfAwayWinSecondHalfHomeWindraw[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Winning,Second Half output: lost while leading Halftime
     #if len(rfdA) - FirstHalfTrailSecOutput[0] :          
     FirstHalfAwayWinSecondHalfLose[0].append(str(FirstHalfTrailSecOutput[1])+ "/" +str(FirstHalfTrailSecOutput[0]))
     FirstHalfAwayWinSecondHalfLose[1].append(len(rfdA))
     FirstHalfAwayWinSecondHalfLose[2].append(t)
     FirstHalfAwayWinSecondHalfLose[3].append("FirstHalfHomeWinSecHalfLose")
     FirstHalfAwayWinSecondHalfLose[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Zero:Zero First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[0] :          
     FirstHalfAcionSecondHalfOverUnderZ[0].append(str(ActionOutpFrstHalfOverUnder[1])+ "/" +str(ActionOutpFrstHalfOverUnder[6]))
     FirstHalfAcionSecondHalfOverUnderZ[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderZ[2].append(t)
     FirstHalfAcionSecondHalfOverUnderZ[3].append("FirstHalfUnderZeroSecOverZero")
     FirstHalfAcionSecondHalfOverUnderZ[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Zero:One First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[10] :          
     FirstHalfAcionSecondHalfOverUnderZOne[0].append(str(ActionOutpFrstHalfOverUnder[11])+ "/" +str(ActionOutpFrstHalfOverUnder[16]))
     FirstHalfAcionSecondHalfOverUnderZOne[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderZOne[2].append(t)
     FirstHalfAcionSecondHalfOverUnderZOne[3].append("FirstHalfOverZeroSecOverOne")
     FirstHalfAcionSecondHalfOverUnderZOne[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Zero:Two First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[20] :          
     FirstHalfAcionSecondHalfOverUnderZTwo[0].append(str(ActionOutpFrstHalfOverUnder[21])+ "/" +str(ActionOutpFrstHalfOverUnder[26]))
     FirstHalfAcionSecondHalfOverUnderZTwo[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderZTwo[2].append(t)
     FirstHalfAcionSecondHalfOverUnderZTwo[3].append("FirstHalfOverZeroSecOverTwo")
     FirstHalfAcionSecondHalfOverUnderZTwo[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Zero:Three First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[2] :          
     FirstHalfAcionSecondHalfOverUnderZThree[0].append(str(ActionOutpFrstHalfOverUnder[31])+ "/" +str(ActionOutpFrstHalfOverUnder[36]))
     FirstHalfAcionSecondHalfOverUnderZThree[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderZThree[2].append(t)
     FirstHalfAcionSecondHalfOverUnderZThree[3].append("FirstHalfOverZeroSecOverThree")
     FirstHalfAcionSecondHalfOverUnderZThree[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over One:Zero First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[1] :          
     FirstHalfAcionSecondHalfOverUnderO[0].append(str(ActionOutpFrstHalfOverUnder[2])+ "/" +str(ActionOutpFrstHalfOverUnder[7]))
     FirstHalfAcionSecondHalfOverUnderO[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderO[2].append(t)
     FirstHalfAcionSecondHalfOverUnderO[3].append("FirstHalfOverOneSecOverZero")
     FirstHalfAcionSecondHalfOverUnderO[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over One:One First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[11] :          
     FirstHalfAcionSecondHalfOverUnderOOne[0].append(str(ActionOutpFrstHalfOverUnder[12])+ "/" +str(ActionOutpFrstHalfOverUnder[17]))
     FirstHalfAcionSecondHalfOverUnderOOne[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderOOne[2].append(t)
     FirstHalfAcionSecondHalfOverUnderOOne[3].append("FirstHalfOverOneSecOverOne")
     FirstHalfAcionSecondHalfOverUnderOOne[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over One:Two First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[21] :          
     FirstHalfAcionSecondHalfOverUnderOTwo[0].append(str(ActionOutpFrstHalfOverUnder[22])+ "/" +str(ActionOutpFrstHalfOverUnder[27]))
     FirstHalfAcionSecondHalfOverUnderOTwo[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderOTwo[2].append(t)
     FirstHalfAcionSecondHalfOverUnderOTwo[3].append("FirstHalfOverOneSecOverTwo")
     FirstHalfAcionSecondHalfOverUnderOTwo[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over One:Three First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[31] :          
     FirstHalfAcionSecondHalfOverUnderOThree[0].append(str(ActionOutpFrstHalfOverUnder[32])+ "/" +str(ActionOutpFrstHalfOverUnder[37]))
     FirstHalfAcionSecondHalfOverUnderOThree[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderOThree[2].append(t)
     FirstHalfAcionSecondHalfOverUnderOThree[3].append("FirstHalfOverOneSecOverThree")
     FirstHalfAcionSecondHalfOverUnderOThree[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Two:Zero First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[2] :          
     FirstHalfAcionSecondHalfOverUnderT[0].append(str(ActionOutpFrstHalfOverUnder[3])+ "/" +str(ActionOutpFrstHalfOverUnder[8]))
     FirstHalfAcionSecondHalfOverUnderT[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderT[2].append(t)
     FirstHalfAcionSecondHalfOverUnderT[3].append("FirstHalfOverTwoSecOverZero")
     FirstHalfAcionSecondHalfOverUnderT[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Two:One First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[12] :          
     FirstHalfAcionSecondHalfOverUnderTOne[0].append(str(ActionOutpFrstHalfOverUnder[13])+ "/" +str(ActionOutpFrstHalfOverUnder[18]))
     FirstHalfAcionSecondHalfOverUnderTOne[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTOne[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTOne[3].append("FirstHalfOverTwoSecOverOne")
     FirstHalfAcionSecondHalfOverUnderTOne[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Two:Two First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[22] :          
     FirstHalfAcionSecondHalfOverUnderTTwo[0].append(str(ActionOutpFrstHalfOverUnder[23])+ "/" +str(ActionOutpFrstHalfOverUnder[28]))
     FirstHalfAcionSecondHalfOverUnderTTwo[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTTwo[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTTwo[3].append("FirstHalfOverTwoSecOverTwo")
     FirstHalfAcionSecondHalfOverUnderTTwo[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Two:Three First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[32] :          
     FirstHalfAcionSecondHalfOverUnderTThree[0].append(str(ActionOutpFrstHalfOverUnder[33])+ "/" +str(ActionOutpFrstHalfOverUnder[38]))
     FirstHalfAcionSecondHalfOverUnderTThree[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTThree[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTThree[3].append("FirstHalfOverTwoSecOverThree")
     FirstHalfAcionSecondHalfOverUnderTThree[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Three:Zero First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[3] :          
     FirstHalfAcionSecondHalfOverUnderTT[0].append(str(ActionOutpFrstHalfOverUnder[4])+ "/" +str(ActionOutpFrstHalfOverUnder[9]))
     FirstHalfAcionSecondHalfOverUnderTT[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTT[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTT[3].append("FirstHalfOverThreeSecUnderZero")
     FirstHalfAcionSecondHalfOverUnderTT[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Three:One First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[13] :          
     FirstHalfAcionSecondHalfOverUnderTTOne[0].append(str(ActionOutpFrstHalfOverUnder[14])+ "/" +str(ActionOutpFrstHalfOverUnder[19]))
     FirstHalfAcionSecondHalfOverUnderTTOne[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTTOne[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTTOne[3].append("FirstHalfOverThreeSecOverOne")
     FirstHalfAcionSecondHalfOverUnderTTOne[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Three:Two First Half Goal /second Half Output over/under
     #if len(rfdA) - ActionOutpFrstHalfOverUnder[23] :          
     FirstHalfAcionSecondHalfOverUnderTTTwo[0].append(str(ActionOutpFrstHalfOverUnder[24])+ "/" +str(ActionOutpFrstHalfOverUnder[29]))
     FirstHalfAcionSecondHalfOverUnderTTTwo[1].append(len(rfdA))
     FirstHalfAcionSecondHalfOverUnderTTTwo[2].append(t)
     FirstHalfAcionSecondHalfOverUnderTTTwo[3].append("FirstHalfOverThreeSecOverTwo")
     FirstHalfAcionSecondHalfOverUnderTTTwo[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: Over Three:Three First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[33] :          
          FirstHalfAcionSecondHalfOverUnderTTThree[0].append(str(ActionOutpFrstHalfOverUnder[34])+ "/" +str(ActionOutpFrstHalfOverUnder[39]))
          FirstHalfAcionSecondHalfOverUnderTTThree[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTTThree[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTTThree[3].append("FirstHalfOverThreeSecOverThree")
          FirstHalfAcionSecondHalfOverUnderTTThree[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home HalftimeAction Fulltime output: First Half Goal , /second Half Output
     if len(rfdA) - ActionOutpFrstHalf[0] :          
          FirstHalfAcionSecondHalfOutput[0].append(str(ActionOutpFrstHalf[0])+ "/" +str(ActionOutpFrstHalf[1]))
          FirstHalfAcionSecondHalfOutput[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOutput[2].append(t)
          FirstHalfAcionSecondHalfOutput[3].append("FirstHalfGoalFulltimeOverUnder")
          FirstHalfAcionSecondHalfOutput[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Scores  First Half/Fulltime Away output "Home Conceed"
     if len(rfdA) - ScoreFrstHalf[0] :          
          ScoreFSoutcomeAny[0].append(str(ScoreFrstHalf[0])+ "/" +str(ScoreFrstHalf[1]))
          ScoreFSoutcomeAny[1].append(len(rfdA))
          ScoreFSoutcomeAny[2].append(t)
          ScoreFSoutcomeAny[3].append("HomeScoreFirstHSecAOut")
          ScoreFSoutcomeAny[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Scores Zero First Half/Second Half Away output "Home Conceed"
     if len(rfdA) - ScoreXnumFrstHalf[0] :          
          ScoreFSoutcome[0].append(str(ScoreXnumFrstHalf[0])+ "/" +str(ScoreXnumFrstHalf[5]))
          ScoreFSoutcome[1].append(len(rfdA))
          ScoreFSoutcome[2].append(t)
          ScoreFSoutcome[3].append("HomeScoreZeroFirstHSecAOut")
          ScoreFSoutcome[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Scores One First Half/Second Half out Away output "Home Conceed"
     if len(rfdA) - ScoreXnumFrstHalf[1] :          
          ScoreFSoutcomeOne[0].append(str(ScoreXnumFrstHalf[1])+ "/" +str(ScoreXnumFrstHalf[6]))
          ScoreFSoutcomeOne[1].append(len(rfdA))
          ScoreFSoutcomeOne[2].append(t)
          ScoreFSoutcomeOne[3].append("HomeScoreOneFirstHSecAOut")
          ScoreFSoutcomeOne[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Scores Two First Half/Second Half out Away output "Home Conceed"
     if len(rfdA) - ScoreXnumFrstHalf[2] :          
          ScoreFSoutcomeTwo[0].append(str(ScoreXnumFrstHalf[2])+ "/" +str(ScoreXnumFrstHalf[7]))
          ScoreFSoutcomeTwo[1].append(len(rfdA))
          ScoreFSoutcomeTwo[2].append(t)
          ScoreFSoutcomeTwo[3].append("HomeScoreTwoFirstHSecAOut")
          ScoreFSoutcomeTwo[4].append("HomeGamesPlayed")
#=====================================================================================================#
#Home Conceed Zero First Half/Second Half out Away output "Home Conceed"
     if len(rfdA) - ConceedXnumFrstHalf[0] :          
          ConceedFSoutcome[0].append(str(ConceedXnumFrstHalf[0])+ "/" +str(ConceedXnumFrstHalf[5]))
          ConceedFSoutcome[1].append(len(rfdA))
          ConceedFSoutcome[2].append(t)
          ConceedFSoutcome[3].append("HomeConceedZeroFirstHSecAOut")
          ConceedFSoutcome[4].append("HomeGamesPlayed")
#Home Conceed One First Half/Second Half out Away output "Home Conceed"
     if len(rfdA) - ConceedXnumFrstHalf[1] :          
          ConceedFSoutcomeOne[0].append(str(ConceedXnumFrstHalf[1])+ "/" +str(ConceedXnumFrstHalf[6]))
          ConceedFSoutcomeOne[1].append(len(rfdA))
          ConceedFSoutcomeOne[2].append(t)
          ConceedFSoutcomeOne[3].append("HomeConceedOneFirstHSecAOut")
          ConceedFSoutcomeOne[4].append("AwayGamesPlayed")
#Home Conceed Two First Half/Second Half out Away output "Home Conceed"
     if len(rfdA) - ConceedXnumFrstHalf[2] :          
          ConceedFSoutcomeTwo[0].append(str(ConceedXnumFrstHalf[2])+ "/" +str(ConceedXnumFrstHalf[7]))
          ConceedFSoutcomeTwo[1].append(len(rfdA))
          ConceedFSoutcomeTwo[2].append(t)
          ConceedFSoutcomeTwo[3].append("HomeConceedTwoHSecAOut")
          ConceedFSoutcomeTwo[4].append("AwayGamesPlayed")

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
          HSWinsDraw[0].append(str(HWinLose[9]) + "/" + str(HWinLose[13]))
          HSWinsDraw[1].append(len(rfdA))
          HSWinsDraw[2].append(t)
          HSWinsDraw[3].append("HomeSecondHalfWinDraw")
          HSWinsDraw[4].append("HomeGamesPlayed") 
#========================================================================#
#Home Secondhalf Win 
     if len(rfdA) - HWinLose[10] :          
          H2ndHWins[0].append(str(HWinLose[11])+ "/" +str(HWinLose[17]))
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


homeFilter(sql_data)
          #1             #2          #3           #4           #5               #6             #7             #8                #9               #10            #11          #12           #13             #14          #15       #16     #17        #18          #19         #20       #21           #22            #23           #24         #25       #26        #27      #28         #29        #30       #31      #32        #33        #34           #35          #36               #37                      #38                     #39                      #40                        #41                         #42                #43                #44                  #45           #46               #47               #47               #48                  #49                                    #50                                #51                                     #52                                     #53                                #54                                #55                                     #56                                     #57                                #58                                     #59                                #60                                    #61                                 #62                                #63                                     #64                           #65                      #66                           #67                           #68                      #69                   #70                              #71                           #72                                #73                           #74                           #75                                #76                                #77                           #78                           #79                                #80                                #81                            #82                               #83                            #84                               #85                            #86                       #87                           #88                      89                          90                            91                              92                     93                       94                            95                            96                            97                            98                           99                             100                       101                          102                        103                              104                      105                           106                      107                           108                           109                           110                           111                           112                           113                           114                           115                           116                           117                           118                      119                      120                      121                           122                      123                       124                          125                   126                         127                      128                           129                      130                         131                        132                      133                                    

Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ,ConceedFSoutcomeOne,ConceedFSoutcomeTwo,ConceedFSoutcome,ScoreFSoutcome,ScoreFSoutcomeOne,ScoreFSoutcomeTwo,ScoreFSoutcomeAny,FirstHalfAcionSecondHalfOutput,FirstHalfAcionSecondHalfOverUnderTTThree,FirstHalfAcionSecondHalfOverUnderTTTwo,FirstHalfAcionSecondHalfOverUnderTTOne,FirstHalfAcionSecondHalfOverUnderTT,FirstHalfAcionSecondHalfOverUnderT,FirstHalfAcionSecondHalfOverUnderTOne,FirstHalfAcionSecondHalfOverUnderTTwo,FirstHalfAcionSecondHalfOverUnderTThree,FirstHalfAcionSecondHalfOverUnderO,FirstHalfAcionSecondHalfOverUnderOOne,FirstHalfAcionSecondHalfOverUnderOTwo,FirstHalfAcionSecondHalfOverUnderOThree,FirstHalfAwayWinSecondHalfLose,FirstHalfAwayWinSecondHalfHomeWindraw,FirstHAwayWinSecHAwayScore3,FirstHAwayWinSecHAwayScore1,FirstHAwayWinSecHAwayScore2,FirstHAwayWinSecHHomeScore1,FirstHAwayWinSecHHomeScore2,FirstHAwayWinSecHHomeScore3,awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12,awayConceedOvUvHomeConceedOvUv13,awayConceedOvUvHomeConceedOvUv14,awayConceedOvUvHomeConceedOvUv15,awayConceedOvUvHomeConceedOvUv16,awayConOvUvHomeConceedOvUv,awayConOvUvHomeConceedOvUv2,awayConOvUvHomeConceedOvUv3,awayConOvUvHomeConceedOvUv4,awayConOvUvHomeConceedOvUv5,awayConOvUvHomeConceedOvUv6,awayConOvUvHomeConceedOvUv7,awayConOvUvHomeConceedOvUv8,awayConOvUvHomeConceedOvUv9,awayConOvUvHomeConceedOvUv10,awayConOvUvHomeConceedOvUv11,awayConOvUvHomeConceedOvUv12,awayConOvUvHomeConceedOvUv13,awayConOvUvHomeConceedOvUv14,awayConOvUvHomeConceedOvUv15,awayConOvUvHomeConceedOvUv16,awayScorOvUvHomeConceedOvUv,awayScorOvUvHomeConceedOvUv2,awayScorOvUvHomeConceedOvUv3,awayScorOvUvHomeConceedOvUv4,awayScorOvUvHomeConceedOvUv5,awayScorOvUvHomeConceedOvUv6,awayScorOvUvHomeConceedOvUv7,awayScorOvUvHomeConceedOvUv8,awayScorOvUvHomeConceedOvUv9,awayScorOvUvHomeConceedOvUv10,awayScorOvUvHomeConceedOvUv11,awayScorOvUvHomeConceedOvUv12,awayScorOvUvHomeConceedOvUv13,awayScorOvUvHomeConceedOvUv14,awayScorOvUvHomeConceedOvUv15,awayScorOvUvHomeConceedOvUv16,awayScorOvUvHomeScorOvUv,awayScorOvUvHomeScorOvUv2,awayScorOvUvHomeScorOvUv3,awayScorOvUvHomeScorOvUv4,awayScorOvUvHomeScorOvUv5,awayScorOvUvHomeScorOvUv6,awayScorOvUvHomeScorOvUv7,awayScorOvUvHomeScorOvUv8,awayScorOvUvHomeScorOvUv9,awayScorOvUvHomeScorOvUv10,awayScorOvUvHomeScorOvUv11,awayScorOvUvHomeScorOvUv12,awayScorOvUvHomeScorOvUv13,awayScorOvUvHomeScorOvUv14,awayScorOvUvHomeScorOvUv15,awayScorOvUvHomeScorOvUv16)

createReport(Info,pd)
 