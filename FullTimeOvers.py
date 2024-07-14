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


ConceedFSoutcome = ([],[],[],[],[])
ConceedFSoutcomeOne = ([],[],[],[],[])
ConceedFSoutcomeTwo= ([],[],[],[],[])

ScoreFSoutcome = ([],[],[],[],[])
ScoreFSoutcomeOne = ([],[],[],[],[])
ScoreFSoutcomeTwo = ([],[],[],[],[])

ScoreFSoutcomeAny = ([],[],[],[],[])
FirstHalfAcionSecondHalfOutput = ([],[],[],[],[])

FirstHalfAcionSecondHalfOverUnderZ = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderZThree = ([],[],[],[],[])

FirstHalfAwayWinSecondHalfLose= ([],[],[],[],[])
FirstHalfAwayWinSecondHalfHomeWindraw= ([],[],[],[],[])
FirstHalfAwayWinSecondHalfHomeScore= ([],[],[],[],[])

FirstHAwayWinSecHAwayScore1= ([],[],[],[],[])
FirstHAwayWinSecHAwayScore2= ([],[],[],[],[])
FirstHAwayWinSecHAwayScore3= ([],[],[],[],[])

FirstHAwayWinSecHHomeScore1= ([],[],[],[],[])
FirstHAwayWinSecHHomeScore2= ([],[],[],[],[])
FirstHAwayWinSecHHomeScore3= ([],[],[],[],[])

FirstHalfAcionSecondHalfOverUnderO = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderOThree = ([],[],[],[],[])

FirstHalfAcionSecondHalfOverUnderT = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTThree = ([],[],[],[],[])

FirstHalfAcionSecondHalfOverUnderTT = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTOne = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTTwo = ([],[],[],[],[])
FirstHalfAcionSecondHalfOverUnderTTThree = ([],[],[],[],[])



AwyFirstfailtToConceedOvs= ([],[],[],[],[])
AwyFirstfailtToConceedOvs2= ([],[],[],[],[])
AwyFirstfailtToConceedOvs3= ([],[],[],[],[])

AwySfailtToConceedOvs= ([],[],[],[],[])
AwySfailtToConceedOvs2= ([],[],[],[],[])
AwySfailtToConceedOvs3= ([],[],[],[],[])



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

H2ndHLose = ([],[],[],[],[])


HLose = ([],[],[],[],[])


a2ndHFailureWins= ([],[],[],[],[])
H2ndHFailureWins = ([],[],[],[],[])
aHalftimeWins= ([],[],[],[],[])
aFuilureToWins= ([],[],[],[],[])
aFuilureToHalfWins = ([],[],[],[],[])
HHalftimeLose = ([],[],[],[],[])
HFuilureToWins = ([],[],[],[],[])
HHalftimeWins = ([],[],[],[],[])



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
    # HWinLose = BtOr.MatchRes(t,rfdA,"b",6)
     #AwOvers = BtOr.OverUnderSeaon(t,rfdA,"b",6)
    # HfullTimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"over")
    # HHalfimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"first")
     #HsecHaTimeOver = BtOr.FixOverUnders(t,rfdA,"b",5,"sec")
    # hFBTS  = BtOr.Bts(t,rfdA,"b",5,"over")
    # hfirstBTS = BtOr.Bts(t,rfdA,"b",5,"first")
    # hSecndBTS = BtOr.Bts(t,rfdA,"b",5,"sec")
    # HmeConceedFulltime = BtOr.ConcededWholeSeaon(t,rfdA,"b",5)
    # ConceedXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"k",5)
    # ScoreXnumFrstHalf = SlPA.ConceedSecondLayerPerceptron(t,rfdA,"b",8)
     ScoreFrstHalf = SlPA.ScoreFirstHConceedSecondLayerPerceptron(t,rfdA,"b",8)
     ActionOutpFrstHalf = SlPA.HaltimeFultimeActionOutput(t,rfdA,"b",8)
     ActionOutpFrstHalfOverUnder = SlPA.HaltimeFultimeActionOutputOverUnder(t,rfdA,"b",8)
     FirstHalfTrailSecOutput = SlPA.FirstHalfWinSecHalfOut(t,rfdA,"b",8)

     #hBTS = BtOr.Bts(t,rfdA,"k",5)
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Home Over Zero Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[14] :          
          FirstHAwayWinSecHHomeScore1[0].append(str(FirstHalfTrailSecOutput[14])+ "/" +str(FirstHalfTrailSecOutput[15]))
          FirstHAwayWinSecHHomeScore1[1].append(len(rfdA))
          FirstHAwayWinSecHHomeScore1[2].append(t)
          FirstHAwayWinSecHHomeScore1[3].append("FirstHAwayWinSecHHomeScore1")
          FirstHAwayWinSecHHomeScore1[4].append("AwayGamesPlayed")
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Home Over One Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[14] :          
          FirstHAwayWinSecHHomeScore2[0].append(str(FirstHalfTrailSecOutput[16])+ "/" +str(FirstHalfTrailSecOutput[17]))
          FirstHAwayWinSecHHomeScore2[1].append(len(rfdA))
          FirstHAwayWinSecHHomeScore2[2].append(t)
          FirstHAwayWinSecHHomeScore2[3].append("FirstHAwayWinSecHHomeScore2")
          FirstHAwayWinSecHHomeScore2[4].append("AwayGamesPlayed")
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Home Over Two Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[14] :          
          FirstHAwayWinSecHHomeScore3[0].append(str(FirstHalfTrailSecOutput[18])+ "/" +str(FirstHalfTrailSecOutput[19]))
          FirstHAwayWinSecHHomeScore3[1].append(len(rfdA))
          FirstHAwayWinSecHHomeScore3[2].append(t)
          FirstHAwayWinSecHHomeScore3[3].append("FirstHAwayWinSecHHomeScore3")
          FirstHAwayWinSecHHomeScore3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Away Over Zero Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[6] :          
          FirstHAwayWinSecHAwayScore1[0].append(str(FirstHalfTrailSecOutput[6])+ "/" +str(FirstHalfTrailSecOutput[7]))
          FirstHAwayWinSecHAwayScore1[1].append(len(rfdA))
          FirstHAwayWinSecHAwayScore1[2].append(t)
          FirstHAwayWinSecHAwayScore1[3].append("FirstHAwayWinSecHAwayScore1")
          FirstHAwayWinSecHAwayScore1[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Away Over one Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[8] :          
          FirstHAwayWinSecHAwayScore2[0].append(str(FirstHalfTrailSecOutput[8])+ "/" +str(FirstHalfTrailSecOutput[9]))
          FirstHAwayWinSecHAwayScore2[1].append(len(rfdA))
          FirstHAwayWinSecHAwayScore2[2].append(t)
          FirstHAwayWinSecHAwayScore2[3].append("FirstHAwayWinSecHAwayScore2")
          FirstHAwayWinSecHAwayScore2[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Away Over Two Sechnd HAlf
     if len(rfdA) - FirstHalfTrailSecOutput[10] :          
          FirstHAwayWinSecHAwayScore3[0].append(str(FirstHalfTrailSecOutput[10])+ "/" +str(FirstHalfTrailSecOutput[11]))
          FirstHAwayWinSecHAwayScore3[1].append(len(rfdA))
          FirstHAwayWinSecHAwayScore3[2].append(t)
          FirstHAwayWinSecHAwayScore3[3].append("FirstHAwayWinSecHAwayScore3")
          FirstHAwayWinSecHAwayScore3[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Home score
     if len(rfdA) - FirstHalfTrailSecOutput[4] :          
          FirstHalfAwayWinSecondHalfHomeScore[0].append(str(FirstHalfTrailSecOutput[4])+ "/" +str(FirstHalfTrailSecOutput[5]))
          FirstHalfAwayWinSecondHalfHomeScore[1].append(len(rfdA))
          FirstHalfAwayWinSecondHalfHomeScore[2].append(t)
          FirstHalfAwayWinSecondHalfHomeScore[3].append("FirstHAwayWinSecHHomeScore")
          FirstHalfAwayWinSecondHalfHomeScore[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: Away leading Halftime//Home WinDraw vs AwayDraw
     if len(rfdA) - FirstHalfTrailSecOutput[2] :          
          FirstHalfAwayWinSecondHalfHomeWindraw[0].append(str(FirstHalfTrailSecOutput[2])+ "/" +str(FirstHalfTrailSecOutput[3]))
          FirstHalfAwayWinSecondHalfHomeWindraw[1].append(len(rfdA))
          FirstHalfAwayWinSecondHalfHomeWindraw[2].append(t)
          FirstHalfAwayWinSecondHalfHomeWindraw[3].append("FirstHalfAwayWinSecHalfHomeWD")
          FirstHalfAwayWinSecondHalfHomeWindraw[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Winning,Second Half output: lost while leading Halftime
     if len(rfdA) - FirstHalfTrailSecOutput[0] :          
          FirstHalfAwayWinSecondHalfLose[0].append(str(FirstHalfTrailSecOutput[0])+ "/" +str(FirstHalfTrailSecOutput[1]))
          FirstHalfAwayWinSecondHalfLose[1].append(len(rfdA))
          FirstHalfAwayWinSecondHalfLose[2].append(t)
          FirstHalfAwayWinSecondHalfLose[3].append("FirstHalfAwayWinSecHalfLose")
          FirstHalfAwayWinSecondHalfLose[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Zero:Zero First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[0] :          
          FirstHalfAcionSecondHalfOverUnderZ[0].append(str(ActionOutpFrstHalfOverUnder[0])+ "/" +str(ActionOutpFrstHalfOverUnder[5]))
          FirstHalfAcionSecondHalfOverUnderZ[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderZ[2].append(t)
          FirstHalfAcionSecondHalfOverUnderZ[3].append("FirstHalfUnderZeroSecOverZero")
          FirstHalfAcionSecondHalfOverUnderZ[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Zero:One First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[10] :          
          FirstHalfAcionSecondHalfOverUnderZOne[0].append(str(ActionOutpFrstHalfOverUnder[10])+ "/" +str(ActionOutpFrstHalfOverUnder[15]))
          FirstHalfAcionSecondHalfOverUnderZOne[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderZOne[2].append(t)
          FirstHalfAcionSecondHalfOverUnderZOne[3].append("FirstHalfOverZeroSecOverOne")
          FirstHalfAcionSecondHalfOverUnderZOne[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Zero:Two First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[20] :          
          FirstHalfAcionSecondHalfOverUnderZTwo[0].append(str(ActionOutpFrstHalfOverUnder[20])+ "/" +str(ActionOutpFrstHalfOverUnder[25]))
          FirstHalfAcionSecondHalfOverUnderZTwo[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderZTwo[2].append(t)
          FirstHalfAcionSecondHalfOverUnderZTwo[3].append("FirstHalfOverZeroSecOverTwo")
          FirstHalfAcionSecondHalfOverUnderZTwo[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Zero:Three First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[2] :          
          FirstHalfAcionSecondHalfOverUnderZThree[0].append(str(ActionOutpFrstHalfOverUnder[30])+ "/" +str(ActionOutpFrstHalfOverUnder[35]))
          FirstHalfAcionSecondHalfOverUnderZThree[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderZThree[2].append(t)
          FirstHalfAcionSecondHalfOverUnderZThree[3].append("FirstHalfOverZeroSecOverThree")
          FirstHalfAcionSecondHalfOverUnderZThree[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over One:Zero First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[1] :          
          FirstHalfAcionSecondHalfOverUnderO[0].append(str(ActionOutpFrstHalfOverUnder[1])+ "/" +str(ActionOutpFrstHalfOverUnder[6]))
          FirstHalfAcionSecondHalfOverUnderO[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderO[2].append(t)
          FirstHalfAcionSecondHalfOverUnderO[3].append("FirstHalfOverOneSecUnderZero")
          FirstHalfAcionSecondHalfOverUnderO[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over One:One First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[11] :          
          FirstHalfAcionSecondHalfOverUnderOOne[0].append(str(ActionOutpFrstHalfOverUnder[11])+ "/" +str(ActionOutpFrstHalfOverUnder[16]))
          FirstHalfAcionSecondHalfOverUnderOOne[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderOOne[2].append(t)
          FirstHalfAcionSecondHalfOverUnderOOne[3].append("FirstHalfOverOneSecOverOne")
          FirstHalfAcionSecondHalfOverUnderOOne[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over One:Two First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[21] :          
          FirstHalfAcionSecondHalfOverUnderOTwo[0].append(str(ActionOutpFrstHalfOverUnder[21])+ "/" +str(ActionOutpFrstHalfOverUnder[26]))
          FirstHalfAcionSecondHalfOverUnderOTwo[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderOTwo[2].append(t)
          FirstHalfAcionSecondHalfOverUnderOTwo[3].append("FirstHalfOverOneSecOverTwo")
          FirstHalfAcionSecondHalfOverUnderOTwo[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over One:Three First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[31] :          
          FirstHalfAcionSecondHalfOverUnderOThree[0].append(str(ActionOutpFrstHalfOverUnder[31])+ "/" +str(ActionOutpFrstHalfOverUnder[36]))
          FirstHalfAcionSecondHalfOverUnderOThree[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderOThree[2].append(t)
          FirstHalfAcionSecondHalfOverUnderOThree[3].append("FirstHalfOverOneSecOverThree")
          FirstHalfAcionSecondHalfOverUnderOThree[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Two:Zero First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[2] :          
          FirstHalfAcionSecondHalfOverUnderT[0].append(str(ActionOutpFrstHalfOverUnder[2])+ "/" +str(ActionOutpFrstHalfOverUnder[7]))
          FirstHalfAcionSecondHalfOverUnderT[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderT[2].append(t)
          FirstHalfAcionSecondHalfOverUnderT[3].append("FirstHalfOverTwoSecUnderZero")
          FirstHalfAcionSecondHalfOverUnderT[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Two:One First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[12] :          
          FirstHalfAcionSecondHalfOverUnderTOne[0].append(str(ActionOutpFrstHalfOverUnder[12])+ "/" +str(ActionOutpFrstHalfOverUnder[17]))
          FirstHalfAcionSecondHalfOverUnderTOne[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTOne[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTOne[3].append("FirstHalfOverTwoSecOverOne")
          FirstHalfAcionSecondHalfOverUnderTOne[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Two:Two First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[22] :          
          FirstHalfAcionSecondHalfOverUnderTTwo[0].append(str(ActionOutpFrstHalfOverUnder[22])+ "/" +str(ActionOutpFrstHalfOverUnder[27]))
          FirstHalfAcionSecondHalfOverUnderTTwo[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTTwo[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTTwo[3].append("FirstHalfOverTwoSecOverTwo")
          FirstHalfAcionSecondHalfOverUnderTTwo[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Two:Three First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[32] :          
          FirstHalfAcionSecondHalfOverUnderTThree[0].append(str(ActionOutpFrstHalfOverUnder[32])+ "/" +str(ActionOutpFrstHalfOverUnder[37]))
          FirstHalfAcionSecondHalfOverUnderTThree[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTThree[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTThree[3].append("FirstHalfOverTwoSecOverThree")
          FirstHalfAcionSecondHalfOverUnderTThree[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Three:Zero First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[3] :          
          FirstHalfAcionSecondHalfOverUnderTT[0].append(str(ActionOutpFrstHalfOverUnder[3])+ "/" +str(ActionOutpFrstHalfOverUnder[8]))
          FirstHalfAcionSecondHalfOverUnderTT[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTT[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTT[3].append("FirstHalfOverThreeSecUnderZero")
          FirstHalfAcionSecondHalfOverUnderTT[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Three:One First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[13] :          
          FirstHalfAcionSecondHalfOverUnderTTOne[0].append(str(ActionOutpFrstHalfOverUnder[13])+ "/" +str(ActionOutpFrstHalfOverUnder[18]))
          FirstHalfAcionSecondHalfOverUnderTTOne[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTTOne[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTTOne[3].append("FirstHalfOverTwoSecOverOne")
          FirstHalfAcionSecondHalfOverUnderTTOne[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Three:Two First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[23] :          
          FirstHalfAcionSecondHalfOverUnderTTTwo[0].append(str(ActionOutpFrstHalfOverUnder[23])+ "/" +str(ActionOutpFrstHalfOverUnder[28]))
          FirstHalfAcionSecondHalfOverUnderTTTwo[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTTTwo[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTTTwo[3].append("FirstHalfOverThreeSecOverTwo")
          FirstHalfAcionSecondHalfOverUnderTTTwo[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: Over Three:Three First Half Goal /second Half Output over/under
     if len(rfdA) - ActionOutpFrstHalfOverUnder[33] :          
          FirstHalfAcionSecondHalfOverUnderTTThree[0].append(str(ActionOutpFrstHalfOverUnder[33])+ "/" +str(ActionOutpFrstHalfOverUnder[38]))
          FirstHalfAcionSecondHalfOverUnderTTThree[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOverUnderTTThree[2].append(t)
          FirstHalfAcionSecondHalfOverUnderTTThree[3].append("FirstHalfOverThreeSecOverThree")
          FirstHalfAcionSecondHalfOverUnderTTThree[4].append("AwayGamesPlayed")
#=====================================================================================================#
#Away HalftimeAction Fulltime output: First Half Goal , /second Half Output
     if len(rfdA) - ActionOutpFrstHalf[0] :          
          FirstHalfAcionSecondHalfOutput[0].append(str(ActionOutpFrstHalf[0])+ "/" +str(ActionOutpFrstHalf[1]))
          FirstHalfAcionSecondHalfOutput[1].append(len(rfdA))
          FirstHalfAcionSecondHalfOutput[2].append(t)
          FirstHalfAcionSecondHalfOutput[3].append("FirstHalfGoalFulltimeOverUnder")
          FirstHalfAcionSecondHalfOutput[4].append("AwayGamesPlayed")

#=====================================================================================================#
#Away Scores  First Half/Fulltime Home output "Away Conceed"
     if len(rfdA) - ScoreFrstHalf[0] :          
          ScoreFSoutcomeAny[0].append(str(ScoreFrstHalf[0])+ "/" +str(ScoreFrstHalf[1]))
          ScoreFSoutcomeAny[1].append(len(rfdA))
          ScoreFSoutcomeAny[2].append(t)
          ScoreFSoutcomeAny[3].append("AwayScoreFirstHSecHOut")
          ScoreFSoutcomeAny[4].append("AwayGamesPlayed")


















 












  

#homeFilter(sql_data)
#awayFilter(sql_data)
          #1             #2        #3             #4           #5           #6                 #7              #8                 #9             #10               #11         #12            #13            #14         #15      #16      #17       #18            #19       #20       #21          #22              #23            #24        #25      #26       #27       #28         #29       #30       #31         #32        #33       #34         #35          #36                 #37                     #38                       #39                      #40                        #41                    #42                                                                              
#Info=(HomeFixOver1,HomeFixOver2,HomeFixOver3,HomeFixOver4,HomeFixOver5,HomeFConceedOvs,HomeFConceedOvs2,HomeFConceedOvs3,HomeFConceedOvs4,HomeFConceedOvs5,HomefullOver1,HomefullOver2,HomefullOver3,HomefullOver4,HomefullOver5,HWins,HWinsDraw,HHalftimeWins,HHWinsDraw,HSWinsDraw,H2ndHWins,HomeHalftimeOverZ,HomefrstOver1,HomefrstOver2,HomeSOvs,HomeSOvs1,HomeSOvs2,HomeFFOvs2,HomeFFOvs3,HomeFFOvs,HomeSFOvs,HomeSFOvs2,HomeSFOvs3,HomeallBTS,HomeFrstHBTS,HomeSecndHBTS,HomeHalftimeConceedOverZ,HomeHalftimeConceedOverZ2,HomeHalftimeConceedOverZ3,HomeSectimeConceedOverZ3,HomeSectimeConceedOverZ2,HomeSectimeConceedOverZ, ConceedFSoutcome,ConceedFSoutcomeOne,ConceedFSoutcomeTwo, ScoreFSoutcome, ScoreFSoutcomeTwo, ScoreFSoutcomeOne,)
                      
#SecLayerInfor = (ScoreFSoutcomeAny,FirstHalfAcionSecondHalfOutput,FirstHalfAcionSecondHalfOverUnderZ,FirstHalfAcionSecondHalfOverUnderZOne,FirstHalfAcionSecondHalfOverUnderZTwo,FirstHalfAcionSecondHalfOverUnderZThree,FirstHalfAcionSecondHalfOverUnderO,FirstHalfAcionSecondHalfOverUnderOOne,FirstHalfAcionSecondHalfOverUnderOTwo,FirstHalfAcionSecondHalfOverUnderOThree,FirstHalfAcionSecondHalfOverUnderTThree,FirstHalfAcionSecondHalfOverUnderTTwo,FirstHalfAcionSecondHalfOverUnderTTOne,FirstHalfAcionSecondHalfOverUnderTT,FirstHalfAcionSecondHalfOverUnderTTThree,FirstHalfAcionSecondHalfOverUnderTTTwo,FirstHalfAwayWinSecondHalfLose,FirstHalfAwayWinSecondHalfHomeWindraw,FirstHalfAwayWinSecondHalfHomeScore,FirstHAwayWinSecHAwayScore1,FirstHAwayWinSecHAwayScore2,FirstHAwayWinSecHAwayScore3,FirstHAwayWinSecHHomeScore1,FirstHAwayWinSecHHomeScore2,FirstHAwayWinSecHHomeScore3)
#createReport(Info,pd)





