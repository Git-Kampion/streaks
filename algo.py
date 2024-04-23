import pandas as pd
import time
import pyodbc
import openpyxl


tencents = 0.10

def getInfo(parm):
    return 0

def btParse(ftype,Ttype,team):
 match ftype:
    case "Away2ndHalfWins":
      res = getOdds(Ttype,"secHalvAwayWin",team)
    case "AwayHalftimeFailToWin":
      res = getOdds(Ttype,"firstHalvHomeDraw",team)
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
       res = getOdds(Ttype,"secHalvHomeWin",team)
    case "Home2ndHalfFailToWin":
       res = getOdds(Ttype,"secHalvAwayDraw",team)
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

def getTeamSheet():
  file = open("identity.txt", "r")
  content = file.read().split("\n")
  data = [content]
  return data

def getOdds(HomeAway,sqlparm,TeamName):
    teamQuery = HomeAway + " = ?"
    count = 0
    ds = getTeamSheet();
    tuples = []
    if len(TeamName) > 1:
       for t in TeamName:
         for k in ds[0]:
          if t in k:
             BetEplindex = ds[0].index(k)
             st = ds[0][BetEplindex]
             
             #teamQuery = teamQuery +  str(st).split("=")[1].strip()
             tuples.append(str(st).split("=")[1].strip())
             count = count + 1
             if count != len(TeamName):
               teamQuery = teamQuery + "  or " + HomeAway + " = ?"
             break; 
    else:
       teamQuery = TeamName[0]
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\odds.accdb')
    cursor = conn.cursor()
   # insert_stmt2 = "select "+sqlparm+ " from EplBetOdds Where " +HomeAway+ "= ?  +HomeAway+ "= ?""   
    insert_stmt2 = "select "+sqlparm+ ", "+HomeAway+" from EplBetOdds Where " + teamQuery 
    
    data = (tuples)
    cursor.execute(insert_stmt2,data)
    sql_data = pd.DataFrame(cursor.fetchall())
    a = 0
v = pd.ExcelFile('streaks.xlsx')

sheetNames = v.sheet_names

teams = []

for sn in sheetNames:
   xl = v.parse(sn)
   teams = xl.iloc[:,0].values
   Ttype = sn[:4]
   if Ttype == "Home":
    btParse(sn,"HTeam",teams)
   else:
    btParse(sn,"ATeam",teams)
