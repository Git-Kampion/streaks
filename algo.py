import pandas as pd
import time
import pyodbc


tencents = 0.10

def getInfo(parm):
    return 0

def btParse(ftype,Ttype,team):
 match ftype:
    case "Away2ndHalfWins":
      res = getOdds("away","secHalvAwayWin",team)
    case "AwayHalftimeFailToWin":
       a = 1 
    case "AwayHalfWins":
       a = 1 
    case "AwayHalftimeFailToWin":
       a = 1 
    case "AwayWins":
       a = 1 
    case "AwayFailToWin":
       a = 1
    case "AwayFailConceed1stHlvGoal":
       a = 1
    case "AwayFailConceed21stHlvGoal":
       a = 1 
    case "AwayFailConceed31stHlvGoal":
       a = 1
    case "AwayFailConceedSecHlvGoal":
       a = 1
    case "AwayFailConceed2SecHlvGoal":
       a = 1
    case "AwayFailConceed3SecHlvGoal":
       a = 1
    case "AwayConceedSecHlvGoal":
       a = 1
    case "AwayConceed2SecHlvGoal":
       a = 1
    case "AwayConceed3SecHlvGoal":
       a = 1
    case "AwayConceed1stHlvGoal":
       a = 1
    case "AwayConceed1stcHlvGoal2":
       a = 1
    case "AwayConceed1stHlvGoal3":
       a = 1
    case "AwayOverSecHlvGoal":
       a = 1
    case "AwayOverSecHlv1Goal":
       a = 1
    case "AwayOverSecHlv2Goal":
       a = 1
    case "AwayUnderSecHlvGoal":
       a = 1
    case "AwayUnderSecHlv1Goal":
       a = 1
    case "AwayUnderSecHlv2Goal":
       a = 1
    case "AwayOverFirstHlvGoal":
       a = 1
    case "AwayOverFirstHlv1Goal":
       a = 1
    case "AwayOverFirstHlv2Goal":
       a = 1
    case "AwayUnderFirstHlvGoal":
       a = 1
    case "AwayUnderFirstHlv1Goal":
       a = 1
    case "AwayUnderFirstHlv2Goal":
       a = 1
    case "AwayUnder1Goal":
       a = 1
    case "AwayUnder2Goal":
       a = 1
    case "AwayUnder3Goal":
       a = 1
    case "AwayUnder4Goal":
       a = 1
    case "AwayUnder5Goal":
       a = 1
    case "AwayGoal":
       a = 1
    case "AwayGoalover2":
       a = 1
    case "AwayGoalover3":
       a = 1
    case "AwayBTS":
       a = 1
    case "AwayFullTimeOver1":
       a = 1
    case "AwayFullTimeOver2":
       a = 1
    case "AwayFullTimeOver3":
       a = 1
    case "AwayFullTimeOver4":
       a = 1
    case "Home2ndHalfWins":
       a = 1
    case "Home2ndHalfFailToWin":
       a = 1
    case "HomeHalfTimeWins":
       a = 1
    case "HomeHalftimeFailToWin":
       a = 1
    case "HomeWins":
       a = 1
    case "HomeFailToWin":
       a = 1
    case "HomeFailConceed1stHlvGoal":
       a = 1
    case "HomeFailConceed1stHlv2Goal":
       a = 1
    case "HomeFailConceed1stHlv3Goal":
       a = 1
    case "HomeFailConceedSecHlvGoal":
       a = 1
    case "HomeFailConceedSecHlv2Goal":
       a = 1
    case "HomeFailConceedSecHlv3Goal":
       a = 1
    case "HomeConceedSecHlvGoal":
       a = 1
    case "HomeConceedSecHlv2Goal":
       a = 1
    case "HomeConceedSecHlv3Goal":
       a = 1
    case "HomeConceed1stHlvGoal":
       a = 1
    case "HomeConceed1stHlv2Goal":
       a = 1
    case "HomeConceed1stHlv3Goal":
       a = 1
    case "HomeOverSecHlvGoal":
       a = 1
    case "HomeOverSecHlv1Goal":
       a = 1
    case "HomeOverSecHlv2Goal":
       a = 1
    case "HomeUnderSecHlvGoal":
       a = 1
    case "HomeUnderSecHlv2Goal":
       a = 1
    case "HomeUnderSecHlv3Goal":
       a = 1
    case "HomeUnderFirstHlvGoal":
       a = 1
    case "HomeUnderFirstHlv2Goal":
       a = 1
    case "HomeUnderFirstHlv3Goal":
       a = 1
    case "HomeOverFirstHlvGoal":
       a = 1
    case "HomeOverFirstHlv2Goal":
       a = 1
    case "HomeOverFirstHlv3Goal":
       a = 1
    case "HomeOverHlvGoal":
       a = 1
    case "HomeOverHlv1Goal":
       a = 1
    case "HomeOverHlv2Goal":
       a = 1
    case "HomeOverHlv3Goal":
       a = 1
    case "HomeUnderHlvGoal":
       a = 1
    case "HomeUnderHlv1Goal":
       a = 1
    case "HomeUnderHlv2Goal":
       a = 1
    case "HomeUnderHlv3Goal":
       a = 1
    case "HomeFixtureNoGoal":
       a = 1
    case "HomeFixtureUnde1Goal":
       a = 1
    case "HomeFixtureUnder2Goal":
       a = 1
    case "HomeFixtureUnder3Goal":
       a = 1
def getOdds(HomeAway,sqlparm,TeamName):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\odds.accdb')
    cursor = conn.cursor()
    insert_stmt2 = "select * from EplBetOdds"
    data = ("Chelsea")
    cursor.execute(insert_stmt2)
    sql_data = pd.DataFrame(cursor.fetchall())

dataframe1 = pd.ExcelFile('streaks.xlsx')
sheetNames = dataframe1.sheet_names
for sn in sheetNames:
    btParse(sn,sn)
getInfo(tencents)