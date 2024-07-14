import pyodbc
from TypesObjectRet import BtOr
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sb
from SecLPAnylaysis import SlPA

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cursor = conn.cursor()

insert_stmt2 = "select * from serieBB ORDER BY Round ASC"
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



def createReport(data1,pd):
 
 #with pd.ExcelWriter('Homestreaks.xlsx') as writer:
 with pd.ExcelWriter('multistreaks.xlsx') as writer:

  for ff in data1:
   if len(ff) >= 1: 

      sheetName =  ff[2][1]
      df2 = pd.DataFrame(list(zip(ff[1],ff[2])),ff[0],columns =[ff[3][1],sheetName])
      df2.to_excel(writer, sheet_name=sheetName )  

def aFHFsc():
 awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv3 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv4 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv7 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv8 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[])



 overs = ([],[],[],[],[])
 unders = ([],[],[],[],[])

 Aunders = ([],[],[],[],[])
 Aovers = ([],[],[],[],[])

 ATTovers = ([],[],[],[],[])
 ATTunders = ([],[],[],[],[])

 ATovers = ([],[],[],[],[])
 ATunders = ([],[],[],[],[])

 for ee in sql_data[0]:

   countovr1 = 0
   countovr2 = 0
   countovr3 = 0
   countovr4 = 0
   underovr1 = 0
   underovr2 = 0
   underovr3 = 0
   underovr4 = 0


   HNunderovr1 = 0
   HNunderovr2 = 0
   HNunderovr3 = 0
   HNunderovr4 = 0
   HNexcountovr1 = 0
   HNexcountovr2 = 0
   HNexcountovr3 = 0
   HNexcountovr4 = 0

   HNTunderovr1 = 0
   HNTunderovr2 = 0
   HNTunderovr3 = 0
   HNTunderovr4 = 0
   HNTexcountovr1 = 0
   HNTexcountovr2 = 0
   HNTexcountovr3 = 0
   HNTexcountovr4 = 0

   HNTTunderovr1 = 0
   HNTTunderovr2 = 0
   HNTTunderovr3 = 0
   HNTTunderovr4 = 0
   HNTTexcountovr1 = 0
   HNTTexcountovr2 = 0
   HNTTexcountovr3 = 0
   HNTTexcountovr4 = 0


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    
    for ec in sql_data[0]:
     if index == ec[0] or indx == True:
       index = ec[0]
       indx = True
       if ec[4] == t: 
        sw = int(ec[5])
        if int(ec[5]) > 4:
           sw = 4            
        match sw:
                case 0:
                    underovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 1:
                    countovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 2:
                    countovr1 += 1
                    countovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 3:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    underovr4+= 1
                case 4:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    countovr4 += 1
       
        for bb in sql_data[0]:
         if index == bb[0]:
            indxFound = True
         if bb[3] == t and indxFound == True: 
            index = bb[0]  
            indx = False
            ll = int(bb[5])
            es = int(ec[5])
            ed = int(ec[6])
            ef = int(bb[6])
            fws = int(bb[7])
            fes = int(bb[8])
            if int(bb[5]) > 4:
                ll = 4
            if int(ec[5]) > 4:
                es = 4
            if int(ec[6]) > 4:
                ed = 4
            if int(bb[6]) > 4:
                ef = 4
            if int(bb[7]) > 4:
                fws = 4
            if int(bb[8]) > 4:
                fes = 4
            
            #c = ll  - fws
            #a = ef  - fes  
            ws = ll + ef  
            aws = ed + es  
            if ws > 4:
                ws = 4
            if aws > 4:
                aws = 4
            match aws:
              case 0:
                  a = 0
              case 1:
               match ws:
                case 0:                    
                        HNunderovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 1:
                    
                        HNexcountovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 2:
                   
                        HNexcountovr1 += 1
                        HNexcountovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 3:
                  
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNunderovr4+= 1
                case 4:
                 
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNexcountovr4 += 1
              case 2:
               match ws:
                case 0:                    
                        HNTunderovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 1:
                        HNTexcountovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 2:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 3:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTunderovr4+= 1
                case 4:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTexcountovr4 += 1  
              case 3:
               match ws:
                case 0:                    
                        HNTTunderovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 1:
                        HNTTexcountovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 2:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 3:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTunderovr4+= 1
                case 4:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTexcountovr4 += 1  
            
            indxFound = False         
            break
   if teamFound == True:
    overs[0].append(t) 
    overs[1].append(countovr1)               
    overs[2].append(countovr2)         
    overs[3].append(countovr3)         
    overs[4].append(countovr4) 

    unders[0].append(t) 
    unders[1].append(underovr1)                
    unders[2].append(underovr2)         
    unders[3].append(underovr3)         
    unders[4].append(underovr4) 

    Aunders[0].append(t)  
    Aunders[1].append(HNunderovr1)                
    Aunders[2].append(HNunderovr2)         
    Aunders[3].append(HNunderovr3)         
    Aunders[4].append(HNunderovr4)

    Aovers[0].append(t) 
    Aovers[1].append(HNexcountovr1)           
    Aovers[2].append(HNexcountovr2)         
    Aovers[3].append(HNexcountovr3)         
    Aovers[4].append(HNexcountovr4) 

    ATovers[0].append(t) 
    ATovers[1].append(HNTexcountovr1)           
    ATovers[2].append(HNTexcountovr2)         
    ATovers[3].append(HNTexcountovr3)         
    ATovers[4].append(HNTexcountovr4) 

    ATunders[0].append(t)  
    ATunders[1].append(HNTunderovr1)                
    ATunders[2].append(HNTunderovr2)         
    ATunders[3].append(HNTunderovr3)         
    ATunders[4].append(HNTunderovr4)

    ATTovers[0].append(t) 
    ATTovers[1].append(HNTTexcountovr1)           
    ATTovers[2].append(HNTTexcountovr2)         
    ATTovers[3].append(HNTTexcountovr3)         
    ATTovers[4].append(HNTTexcountovr4) 

    ATTunders[0].append(t)  
    ATTunders[1].append(HNTTunderovr1)                
    ATTunders[2].append(HNTTunderovr2)         
    ATTunders[3].append(HNTTunderovr3)         
    ATTunders[4].append(HNTTunderovr4)
    teamFound = False

 arr = (Aovers,Aunders,ATovers,ATunders,ATTovers,ATTunders)
 inn = 0
 bb = False
 for t in arr:
    if bb == True:
        break;
    aa = len(t[0]) - 1
    for e in t[0]:
        b =  e
        c =  t[1][inn]
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv[1].append(str(t[1][inn]) + "/" + str(arr[1][1][inn]))
        awayConceedOvUvHomeConceedOvUv[2].append("TAFTTeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv[3].append("AwayGamesPatt")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv2[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[1][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAFT1TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv3[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv3[1].append(str(t[3][inn]) + "/" + str(arr[1][3][inn]))
        awayConceedOvUvHomeConceedOvUv3[2].append("TAFT1TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv3[3].append("AwayGamesPatt")
# Team A/Away Fulltime 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv4[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv4[1].append(str(t[4][inn]) + "/" + str(arr[1][4][inn]))
        awayConceedOvUvHomeConceedOvUv4[2].append("TAFT1TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv4[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv5[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv5[1].append(str(arr[2][1][inn]) + "/" + str(arr[3][1][inn]))
        awayConceedOvUvHomeConceedOvUv5[2].append("TAFT2TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv5[3].append("AwayGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv6[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv6[1].append(str(arr[2][2][inn]) + "/" + str(arr[3][2][inn]))
        awayConceedOvUvHomeConceedOvUv6[2].append("TAFT2TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv6[3].append("AwayGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv7[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv7[1].append(str(arr[2][3][inn]) + "/" + str(arr[3][3][inn]))
        awayConceedOvUvHomeConceedOvUv7[2].append("TAFT2TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv7[3].append("AwayGamesPatt")
# Team A/Away Fulltime 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv8[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv8[1].append(str(arr[2][4][inn]) + "/" + str(arr[3][4][inn]))
        awayConceedOvUvHomeConceedOvUv8[2].append("TAFT2TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv8[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv9[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv9[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv9[2].append("TAFT3TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv9[3].append("AwayGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAFT3TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAFT3TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away Fulltime 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAFT3TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")


        inn += 1
        if aa == inn:
           bb = True
           break;
   

 mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12)
 createReport(mulLayerInfor,pd)

def aConHFsc():
 awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv3 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv4 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv7 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv8 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[])



 overs = ([],[],[],[],[])
 unders = ([],[],[],[],[])

 Aunders = ([],[],[],[],[])
 Aovers = ([],[],[],[],[])

 ATTovers = ([],[],[],[],[])
 ATTunders = ([],[],[],[],[])

 ATovers = ([],[],[],[],[])
 ATunders = ([],[],[],[],[])

 for ee in sql_data[0]:

   countovr1 = 0
   countovr2 = 0
   countovr3 = 0
   countovr4 = 0
   underovr1 = 0
   underovr2 = 0
   underovr3 = 0
   underovr4 = 0


   HNunderovr1 = 0
   HNunderovr2 = 0
   HNunderovr3 = 0
   HNunderovr4 = 0
   HNexcountovr1 = 0
   HNexcountovr2 = 0
   HNexcountovr3 = 0
   HNexcountovr4 = 0

   HNTunderovr1 = 0
   HNTunderovr2 = 0
   HNTunderovr3 = 0
   HNTunderovr4 = 0
   HNTexcountovr1 = 0
   HNTexcountovr2 = 0
   HNTexcountovr3 = 0
   HNTexcountovr4 = 0

   HNTTunderovr1 = 0
   HNTTunderovr2 = 0
   HNTTunderovr3 = 0
   HNTTunderovr4 = 0
   HNTTexcountovr1 = 0
   HNTTexcountovr2 = 0
   HNTTexcountovr3 = 0
   HNTTexcountovr4 = 0


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    
    for ec in sql_data[0]:
     if index == ec[0] or indx == True:
       index = ec[0]
       indx = True
       if ec[4] == t: 
        sw = int(ec[5])
        if int(ec[5]) > 4:
           sw = 4            
        match sw:
                case 0:
                    underovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 1:
                    countovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 2:
                    countovr1 += 1
                    countovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 3:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    underovr4+= 1
                case 4:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    countovr4 += 1
       
        for bb in sql_data[0]:
         if index == bb[0]:
            indxFound = True
         if bb[3] == t and indxFound == True: 
            index = bb[0]  
            indx = False
            ll = int(bb[5])
            es = int(ec[5])
            ef = int(bb[6])
            fws = int(bb[7])
            fes = int(bb[8])
            if int(bb[5]) > 4:
                ll = 4
            if int(ec[5]) > 4:
                es = 4
            if int(bb[6]) > 4:
                ef = 4
            if int(bb[7]) > 4:
                fws = 4
            if int(bb[8]) > 4:
                fes = 4
            if bb[3] == "Como":
             a = 0
            #c = ll  - fws
            #a = ef  - fes  
            ws = ll + ef   
            if ws > 4:
                ws = 4
            match es:
              case 0:
                  a = 0
              case 1:
               match ws:
                case 0:                    
                        HNunderovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 1:
                    
                        HNexcountovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 2:
                   
                        HNexcountovr1 += 1
                        HNexcountovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 3:
                  
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNunderovr4+= 1
                case 4:
                 
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNexcountovr4 += 1
              case 2:
               match ws:
                case 0:                    
                        HNTunderovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 1:
                        HNTexcountovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 2:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 3:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTunderovr4+= 1
                case 4:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTexcountovr4 += 1  
              case 3:
               match ws:
                case 0:                    
                        HNTTunderovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 1:
                        HNTTexcountovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 2:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 3:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTunderovr4+= 1
                case 4:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTexcountovr4 += 1  
            
            indxFound = False         
            break
   if teamFound == True:
    overs[0].append(t) 
    overs[1].append(countovr1)               
    overs[2].append(countovr2)         
    overs[3].append(countovr3)         
    overs[4].append(countovr4) 

    unders[0].append(t) 
    unders[1].append(underovr1)                
    unders[2].append(underovr2)         
    unders[3].append(underovr3)         
    unders[4].append(underovr4) 

    Aunders[0].append(t)  
    Aunders[1].append(HNunderovr1)                
    Aunders[2].append(HNunderovr2)         
    Aunders[3].append(HNunderovr3)         
    Aunders[4].append(HNunderovr4)

    Aovers[0].append(t) 
    Aovers[1].append(HNexcountovr1)           
    Aovers[2].append(HNexcountovr2)         
    Aovers[3].append(HNexcountovr3)         
    Aovers[4].append(HNexcountovr4) 

    ATovers[0].append(t) 
    ATovers[1].append(HNTexcountovr1)           
    ATovers[2].append(HNTexcountovr2)         
    ATovers[3].append(HNTexcountovr3)         
    ATovers[4].append(HNTexcountovr4) 

    ATunders[0].append(t)  
    ATunders[1].append(HNTunderovr1)                
    ATunders[2].append(HNTunderovr2)         
    ATunders[3].append(HNTunderovr3)         
    ATunders[4].append(HNTunderovr4)

    ATTovers[0].append(t) 
    ATTovers[1].append(HNTTexcountovr1)           
    ATTovers[2].append(HNTTexcountovr2)         
    ATTovers[3].append(HNTTexcountovr3)         
    ATTovers[4].append(HNTTexcountovr4) 

    ATTunders[0].append(t)  
    ATTunders[1].append(HNTTunderovr1)                
    ATTunders[2].append(HNTTunderovr2)         
    ATTunders[3].append(HNTTunderovr3)         
    ATTunders[4].append(HNTTunderovr4)
    teamFound = False

 arr = (Aovers,Aunders,ATovers,ATunders,ATTovers,ATTunders)
 inn = 0
 bb = False
 for t in arr:
    if bb == True:
        break;
    aa = len(t[0]) - 1
    for e in t[0]:
        b =  e
        c =  t[1][inn]
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv[1].append(str(t[1][inn]) + "/" + str(arr[1][1][inn]))
        awayConceedOvUvHomeConceedOvUv[2].append("TAConceedTeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv2[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[1][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAConceed1TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv3[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv3[1].append(str(t[3][inn]) + "/" + str(arr[1][3][inn]))
        awayConceedOvUvHomeConceedOvUv3[2].append("TAConceed1TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv3[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv4[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv4[1].append(str(t[4][inn]) + "/" + str(arr[1][4][inn]))
        awayConceedOvUvHomeConceedOvUv4[2].append("TAConceed1TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv4[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv5[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv5[1].append(str(arr[2][1][inn]) + "/" + str(arr[3][1][inn]))
        awayConceedOvUvHomeConceedOvUv5[2].append("TAConceed2TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv5[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv6[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv6[1].append(str(arr[2][2][inn]) + "/" + str(arr[3][2][inn]))
        awayConceedOvUvHomeConceedOvUv6[2].append("TAConceed2TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv6[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv7[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv7[1].append(str(arr[2][3][inn]) + "/" + str(arr[3][3][inn]))
        awayConceedOvUvHomeConceedOvUv7[2].append("TAConceed2TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv7[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv8[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv8[1].append(str(arr[2][4][inn]) + "/" + str(arr[3][4][inn]))
        awayConceedOvUvHomeConceedOvUv8[2].append("TAConceed2TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv8[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv9[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv9[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv9[2].append("TAConceed3TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv9[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAConceed3TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAConceed3TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAConceed3TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")


        inn += 1
        if aa == inn:
           bb = True
           break;
   

 mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12)
 createReport(mulLayerInfor,pd)

def aScHFsc():
 awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv3 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv4 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv7 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv8 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[])



 overs = ([],[],[],[],[])
 unders = ([],[],[],[],[])

 Aunders = ([],[],[],[],[])
 Aovers = ([],[],[],[],[])

 ATTovers = ([],[],[],[],[])
 ATTunders = ([],[],[],[],[])

 ATovers = ([],[],[],[],[])
 ATunders = ([],[],[],[],[])

 for ee in sql_data[0]:

   countovr1 = 0
   countovr2 = 0
   countovr3 = 0
   countovr4 = 0
   underovr1 = 0
   underovr2 = 0
   underovr3 = 0
   underovr4 = 0


   HNunderovr1 = 0
   HNunderovr2 = 0
   HNunderovr3 = 0
   HNunderovr4 = 0
   HNexcountovr1 = 0
   HNexcountovr2 = 0
   HNexcountovr3 = 0
   HNexcountovr4 = 0

   HNTunderovr1 = 0
   HNTunderovr2 = 0
   HNTunderovr3 = 0
   HNTunderovr4 = 0
   HNTexcountovr1 = 0
   HNTexcountovr2 = 0
   HNTexcountovr3 = 0
   HNTexcountovr4 = 0

   HNTTunderovr1 = 0
   HNTTunderovr2 = 0
   HNTTunderovr3 = 0
   HNTTunderovr4 = 0
   HNTTexcountovr1 = 0
   HNTTexcountovr2 = 0
   HNTTexcountovr3 = 0
   HNTTexcountovr4 = 0


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    
    for ec in sql_data[0]:
     if index == ec[0] or indx == True:
       index = ec[0]
       indx = True
       if ec[4] == t: 
        sw = int(ec[6])
        if int(ec[6]) > 4:
           sw = 4            
        match sw:
                case 0:
                    underovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 1:
                    countovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 2:
                    countovr1 += 1
                    countovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 3:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    underovr4+= 1
                case 4:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    countovr4 += 1
       
        for bb in sql_data[0]:
         if index == bb[0]:
            indxFound = True
         if bb[3] == t and indxFound == True: 
            index = bb[0]  
            indx = False
            ll = int(bb[5])
            es = int(ec[6])
            ef = int(bb[6])
            fws = int(bb[7])
            fes = int(bb[8])
            if int(bb[5]) > 4:
                ll = 4
            if int(ec[6]) > 4:
                es = 4
            if int(bb[6]) > 4:
                ef = 4
            if int(bb[7]) > 4:
                fws = 4
            if int(bb[8]) > 4:
                fes = 4
            
            #c = ll  - fws
            #a = ef  - fes  
            ws = ll + ef   
            
            match es:
              case 0:
                  a = 0
              case 1:
               match ws:
                case 0:                    
                        HNunderovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 1:
                    
                        HNexcountovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 2:
                   
                        HNexcountovr1 += 1
                        HNexcountovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 3:
                  
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNunderovr4+= 1
                case 4:
                 
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNexcountovr4 += 1
              case 2:
               match ws:
                case 0:                    
                        HNTunderovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 1:
                        HNTexcountovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 2:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 3:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTunderovr4+= 1
                case 4:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTexcountovr4 += 1  
              case 3:
               match ws:
                case 0:                    
                        HNTTunderovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 1:
                        HNTTexcountovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 2:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 3:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTunderovr4+= 1
                case 4:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTexcountovr4 += 1  
            
            indxFound = False         
            break
   if teamFound == True:
    overs[0].append(t) 
    overs[1].append(countovr1)               
    overs[2].append(countovr2)         
    overs[3].append(countovr3)         
    overs[4].append(countovr4) 

    unders[0].append(t) 
    unders[1].append(underovr1)                
    unders[2].append(underovr2)         
    unders[3].append(underovr3)         
    unders[4].append(underovr4) 

    Aunders[0].append(t)  
    Aunders[1].append(HNunderovr1)                
    Aunders[2].append(HNunderovr2)         
    Aunders[3].append(HNunderovr3)         
    Aunders[4].append(HNunderovr4)

    Aovers[0].append(t) 
    Aovers[1].append(HNexcountovr1)           
    Aovers[2].append(HNexcountovr2)         
    Aovers[3].append(HNexcountovr3)         
    Aovers[4].append(HNexcountovr4) 

    ATovers[0].append(t) 
    ATovers[1].append(HNTexcountovr1)           
    ATovers[2].append(HNTexcountovr2)         
    ATovers[3].append(HNTexcountovr3)         
    ATovers[4].append(HNTexcountovr4) 

    ATunders[0].append(t)  
    ATunders[1].append(HNTunderovr1)                
    ATunders[2].append(HNTunderovr2)         
    ATunders[3].append(HNTunderovr3)         
    ATunders[4].append(HNTunderovr4)

    ATTovers[0].append(t) 
    ATTovers[1].append(HNTTexcountovr1)           
    ATTovers[2].append(HNTTexcountovr2)         
    ATTovers[3].append(HNTTexcountovr3)         
    ATTovers[4].append(HNTTexcountovr4) 

    ATTunders[0].append(t)  
    ATTunders[1].append(HNTTunderovr1)                
    ATTunders[2].append(HNTTunderovr2)         
    ATTunders[3].append(HNTTunderovr3)         
    ATTunders[4].append(HNTTunderovr4)
    teamFound = False

 arr = (Aovers,Aunders,ATovers,ATunders,ATTovers,ATTunders)
 inn = 0
 bb = False
 for t in arr:
    if bb == True:
        break;
    aa = len(t[0]) - 1
    for e in t[0]:
        b =  e
        c =  t[1][inn]
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv[1].append(str(t[1][inn]) + "/" + str(arr[1][1][inn]))
        awayConceedOvUvHomeConceedOvUv[2].append("TAscoresTeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv2[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[1][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAscores1TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv3[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv3[1].append(str(t[3][inn]) + "/" + str(arr[1][3][inn]))
        awayConceedOvUvHomeConceedOvUv3[2].append("TAscores1TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv3[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv4[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv4[1].append(str(t[4][inn]) + "/" + str(arr[1][4][inn]))
        awayConceedOvUvHomeConceedOvUv4[2].append("TAscores1TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv4[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv5[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv5[1].append(str(arr[2][1][inn]) + "/" + str(arr[3][1][inn]))
        awayConceedOvUvHomeConceedOvUv5[2].append("TAscores2TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv5[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv6[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv6[1].append(str(arr[2][2][inn]) + "/" + str(arr[3][2][inn]))
        awayConceedOvUvHomeConceedOvUv6[2].append("TAscores2TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv6[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv7[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv7[1].append(str(arr[2][3][inn]) + "/" + str(arr[3][3][inn]))
        awayConceedOvUvHomeConceedOvUv7[2].append("TAscores2TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv7[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv8[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv8[1].append(str(arr[2][4][inn]) + "/" + str(arr[3][4][inn]))
        awayConceedOvUvHomeConceedOvUv8[2].append("TAscores2TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv8[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv9[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv9[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv9[2].append("TAscores3TeamHFullTimeRes1+")
        awayConceedOvUvHomeConceedOvUv9[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAscores3TeamHFullTimeRes2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAscores3TeamHFullTimeRes3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home Fulltime Res        
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAscores3TeamHFullTimeRes4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")


        inn += 1
        if aa == inn:
           bb = True
           break;
   

 mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12)
 createReport(mulLayerInfor,pd)


def aScHsc():
 awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv3 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv4 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv7 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv8 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[])



 overs = ([],[],[],[],[])
 unders = ([],[],[],[],[])

 Aunders = ([],[],[],[],[])
 Aovers = ([],[],[],[],[])

 ATTovers = ([],[],[],[],[])
 ATTunders = ([],[],[],[],[])

 ATovers = ([],[],[],[],[])
 ATunders = ([],[],[],[],[])

 for ee in sql_data[0]:

   countovr1 = 0
   countovr2 = 0
   countovr3 = 0
   countovr4 = 0
   underovr1 = 0
   underovr2 = 0
   underovr3 = 0
   underovr4 = 0


   HNunderovr1 = 0
   HNunderovr2 = 0
   HNunderovr3 = 0
   HNunderovr4 = 0
   HNexcountovr1 = 0
   HNexcountovr2 = 0
   HNexcountovr3 = 0
   HNexcountovr4 = 0

   HNTunderovr1 = 0
   HNTunderovr2 = 0
   HNTunderovr3 = 0
   HNTunderovr4 = 0
   HNTexcountovr1 = 0
   HNTexcountovr2 = 0
   HNTexcountovr3 = 0
   HNTexcountovr4 = 0

   HNTTunderovr1 = 0
   HNTTunderovr2 = 0
   HNTTunderovr3 = 0
   HNTTunderovr4 = 0
   HNTTexcountovr1 = 0
   HNTTexcountovr2 = 0
   HNTTexcountovr3 = 0
   HNTTexcountovr4 = 0


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    
    for ec in sql_data[0]:
     if index == ec[0] or indx == True:
       index = ec[0]
       indx = True
       if ec[4] == t: 
        sw = int(ec[6])
        if int(ec[6]) > 4:
           sw = 4            
        match sw:
                case 0:
                    underovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 1:
                    countovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 2:
                    countovr1 += 1
                    countovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 3:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    underovr4+= 1
                case 4:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    countovr4 += 1
       
        for bb in sql_data[0]:
         if index == bb[0]:
            indxFound = True
         if bb[3] == t and indxFound == True: 
            index = bb[0]  
            indx = False
            ws = int(bb[5])
            es = int(ec[6])
            if int(bb[5]) > 4:
                ws = 4
            if int(ec[6]) > 4:
                es = 4
            match es:
              case 0:
                  a = 0
              case 1:
               match ws:
                case 0:                    
                        HNunderovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 1:
                    
                        HNexcountovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 2:
                   
                        HNexcountovr1 += 1
                        HNexcountovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 3:
                  
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNunderovr4+= 1
                case 4:
                 
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNexcountovr4 += 1
              case 2:
               match ws:
                case 0:                    
                        HNTunderovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 1:
                        HNTexcountovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 2:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 3:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTunderovr4+= 1
                case 4:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTexcountovr4 += 1  
              case 3:
               match ws:
                case 0:                    
                        HNTTunderovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 1:
                        HNTTexcountovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 2:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 3:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTunderovr4+= 1
                case 4:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTexcountovr4 += 1  
            
            indxFound = False         
            break
   if teamFound == True:
    overs[0].append(t) 
    overs[1].append(countovr1)               
    overs[2].append(countovr2)         
    overs[3].append(countovr3)         
    overs[4].append(countovr4) 

    unders[0].append(t) 
    unders[1].append(underovr1)                
    unders[2].append(underovr2)         
    unders[3].append(underovr3)         
    unders[4].append(underovr4) 

    Aunders[0].append(t)  
    Aunders[1].append(HNunderovr1)                
    Aunders[2].append(HNunderovr2)         
    Aunders[3].append(HNunderovr3)         
    Aunders[4].append(HNunderovr4)

    Aovers[0].append(t) 
    Aovers[1].append(HNexcountovr1)           
    Aovers[2].append(HNexcountovr2)         
    Aovers[3].append(HNexcountovr3)         
    Aovers[4].append(HNexcountovr4) 

    ATovers[0].append(t) 
    ATovers[1].append(HNTexcountovr1)           
    ATovers[2].append(HNTexcountovr2)         
    ATovers[3].append(HNTexcountovr3)         
    ATovers[4].append(HNTexcountovr4) 

    ATunders[0].append(t)  
    ATunders[1].append(HNTunderovr1)                
    ATunders[2].append(HNTunderovr2)         
    ATunders[3].append(HNTunderovr3)         
    ATunders[4].append(HNTunderovr4)

    ATTovers[0].append(t) 
    ATTovers[1].append(HNTTexcountovr1)           
    ATTovers[2].append(HNTTexcountovr2)         
    ATTovers[3].append(HNTTexcountovr3)         
    ATTovers[4].append(HNTTexcountovr4) 

    ATTunders[0].append(t)  
    ATTunders[1].append(HNTTunderovr1)                
    ATTunders[2].append(HNTTunderovr2)         
    ATTunders[3].append(HNTTunderovr3)         
    ATTunders[4].append(HNTTunderovr4)
    teamFound = False

 arr = (Aovers,Aunders,ATovers,ATunders,ATTovers,ATTunders)
 inn = 0
 bb = False
 for t in arr:
    if bb == True:
        break;
    aa = len(t[0]) - 1
    for e in t[0]:
        b =  e
        c =  t[1][inn]
# Team A/Away scores 1 Goal, Team A goes home scores 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv[1].append(str(t[1][inn]) + "/" + str(arr[1][1][inn]))
        awayConceedOvUvHomeConceedOvUv[2].append("TAscoresTeamHscores1+")
        awayConceedOvUvHomeConceedOvUv[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home scores 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv2[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[1][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAscores1TeamHscores2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home scores 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv3[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv3[1].append(str(t[3][inn]) + "/" + str(arr[1][3][inn]))
        awayConceedOvUvHomeConceedOvUv3[2].append("TAscores1TeamHscores3+")
        awayConceedOvUvHomeConceedOvUv3[3].append("AwayGamesPatt")
# Team A/Away scores 1 Goal, Team A goes home scores 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv4[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv4[1].append(str(t[4][inn]) + "/" + str(arr[1][4][inn]))
        awayConceedOvUvHomeConceedOvUv4[2].append("TAscores1TeamHscores4+")
        awayConceedOvUvHomeConceedOvUv4[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 2 Goal, Team A goes home scores 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv5[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv5[1].append(str(arr[2][1][inn]) + "/" + str(arr[3][1][inn]))
        awayConceedOvUvHomeConceedOvUv5[2].append("TAscores2TeamHscores1+")
        awayConceedOvUvHomeConceedOvUv5[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home scores 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv6[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv6[1].append(str(arr[2][2][inn]) + "/" + str(arr[3][2][inn]))
        awayConceedOvUvHomeConceedOvUv6[2].append("TAscores2TeamHscores2+")
        awayConceedOvUvHomeConceedOvUv6[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home scores 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv7[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv7[1].append(str(arr[2][3][inn]) + "/" + str(arr[3][3][inn]))
        awayConceedOvUvHomeConceedOvUv7[2].append("TAscores2TeamHscores3+")
        awayConceedOvUvHomeConceedOvUv7[3].append("AwayGamesPatt")
# Team A/Away scores 2 Goal, Team A goes home scores 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv8[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv8[1].append(str(arr[2][4][inn]) + "/" + str(arr[3][4][inn]))
        awayConceedOvUvHomeConceedOvUv8[2].append("TAscores2TeamHscores4+")
        awayConceedOvUvHomeConceedOvUv8[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away scores 3 Goal, Team A goes home scores 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv9[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv9[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv9[2].append("TAscores3TeamHscores1+")
        awayConceedOvUvHomeConceedOvUv9[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home scores 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAscores3TeamHscores2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home scores 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAscores3TeamHscores3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away scores 3 Goal, Team A goes home scores 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAscores3TeamHscores4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")


        inn += 1
        if aa == inn:
           bb = True
           break;
   

 mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12)
 createReport(mulLayerInfor,pd)

def aCHC():
 awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv3 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv4 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv5 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv6 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv7 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv8 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv9 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv10 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv11 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv12 = ([],[],[],[])
 awayConceedOvUvHomeConceedOvUv13 = ([],[],[],[])



 overs = ([],[],[],[],[])
 unders = ([],[],[],[],[])

 Aunders = ([],[],[],[],[])
 Aovers = ([],[],[],[],[])

 ATTovers = ([],[],[],[],[])
 ATTunders = ([],[],[],[],[])

 ATovers = ([],[],[],[],[])
 ATunders = ([],[],[],[],[])

 for ee in sql_data[0]:
   countovr1 = 0
   countovr2 = 0
   countovr3 = 0
   countovr4 = 0
   underovr1 = 0
   underovr2 = 0
   underovr3 = 0
   underovr4 = 0


   HNunderovr1 = 0
   HNunderovr2 = 0
   HNunderovr3 = 0
   HNunderovr4 = 0
   HNexcountovr1 = 0
   HNexcountovr2 = 0
   HNexcountovr3 = 0
   HNexcountovr4 = 0

   HNTunderovr1 = 0
   HNTunderovr2 = 0
   HNTunderovr3 = 0
   HNTunderovr4 = 0
   HNTexcountovr1 = 0
   HNTexcountovr2 = 0
   HNTexcountovr3 = 0
   HNTexcountovr4 = 0

   HNTTunderovr1 = 0
   HNTTunderovr2 = 0
   HNTTunderovr3 = 0
   HNTTunderovr4 = 0
   HNTTexcountovr1 = 0
   HNTTexcountovr2 = 0
   HNTTexcountovr3 = 0
   HNTTexcountovr4 = 0


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    
    for ec in sql_data[0]:
     if index == ec[0] or indx == True:
       index = ec[0]
       indx = True
       if ec[4] == t: 
        sw = int(ec[5])
        if int(ec[5]) > 4:
           sw = 4            
        match sw:
                case 0:
                    underovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 1:
                    countovr1 += 1
                    underovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 2:
                    countovr1 += 1
                    countovr2 += 1
                    underovr3 += 1
                    underovr4 += 1
                case 3:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    underovr4+= 1
                case 4:
                    countovr1 += 1
                    countovr2 += 1
                    countovr3 += 1
                    countovr4 += 1
       
        for bb in sql_data[0]:
         if index == bb[0]:
            indxFound = True
         if bb[3] == t and indxFound == True: 
            index = bb[0]  
            indx = False
            ws = int(bb[6])
            es = int(ec[5])
            if int(bb[6]) > 4:
                ws = 4
            if int(ec[5]) > 4:
                es = 4
            match es:
              case 0:
                  a = 0
              case 1:
               match ws:
                case 0:                    
                        HNunderovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 1:
                    
                        HNexcountovr1 += 1
                        HNunderovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 2:
                   
                        HNexcountovr1 += 1
                        HNexcountovr2 += 1
                        HNunderovr3 += 1
                        HNunderovr4 += 1
                case 3:
                  
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNunderovr4+= 1
                case 4:
                 
                    HNexcountovr1 += 1
                    HNexcountovr2 += 1
                    HNexcountovr3 += 1
                    HNexcountovr4 += 1
              case 2:
               match ws:
                case 0:                    
                        HNTunderovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 1:
                        HNTexcountovr1 += 1
                        HNTunderovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 2:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTunderovr3 += 1
                        HNTunderovr4 += 1
                case 3:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTunderovr4+= 1
                case 4:
                        HNTexcountovr1 += 1
                        HNTexcountovr2 += 1
                        HNTexcountovr3 += 1
                        HNTexcountovr4 += 1  
              case 3:
               match ws:
                case 0:                    
                        HNTTunderovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 1:
                        HNTTexcountovr1 += 1
                        HNTTunderovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 2:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTunderovr3 += 1
                        HNTTunderovr4 += 1
                case 3:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTunderovr4+= 1
                case 4:
                        HNTTexcountovr1 += 1
                        HNTTexcountovr2 += 1
                        HNTTexcountovr3 += 1
                        HNTTexcountovr4 += 1  
            
            indxFound = False         
            break
   if teamFound == True:
    overs[0].append(t) 
    overs[1].append(countovr1)               
    overs[2].append(countovr2)         
    overs[3].append(countovr3)         
    overs[4].append(countovr4) 

    unders[0].append(t) 
    unders[1].append(underovr1)                
    unders[2].append(underovr2)         
    unders[3].append(underovr3)         
    unders[4].append(underovr4) 

    Aunders[0].append(t)  
    Aunders[1].append(HNunderovr1)                
    Aunders[2].append(HNunderovr2)         
    Aunders[3].append(HNunderovr3)         
    Aunders[4].append(HNunderovr4)

    Aovers[0].append(t) 
    Aovers[1].append(HNexcountovr1)           
    Aovers[2].append(HNexcountovr2)         
    Aovers[3].append(HNexcountovr3)         
    Aovers[4].append(HNexcountovr4) 

    ATovers[0].append(t) 
    ATovers[1].append(HNTexcountovr1)           
    ATovers[2].append(HNTexcountovr2)         
    ATovers[3].append(HNTexcountovr3)         
    ATovers[4].append(HNTexcountovr4) 

    ATunders[0].append(t)  
    ATunders[1].append(HNTunderovr1)                
    ATunders[2].append(HNTunderovr2)         
    ATunders[3].append(HNTunderovr3)         
    ATunders[4].append(HNTunderovr4)

    ATTovers[0].append(t) 
    ATTovers[1].append(HNTTexcountovr1)           
    ATTovers[2].append(HNTTexcountovr2)         
    ATTovers[3].append(HNTTexcountovr3)         
    ATTovers[4].append(HNTTexcountovr4) 

    ATTunders[0].append(t)  
    ATTunders[1].append(HNTTunderovr1)                
    ATTunders[2].append(HNTTunderovr2)         
    ATTunders[3].append(HNTTunderovr3)         
    ATTunders[4].append(HNTTunderovr4)
    teamFound = False

 arr = (Aovers,Aunders,ATovers,ATunders,ATTovers,ATTunders)
 inn = 0
 bb = False
 for t in arr:
    if bb == True:
        break;
    aa = len(t[0]) - 1
    for e in t[0]:
        b =  e
        c =  t[1][inn]
# Team A/Away conceeds 1 Goal, Team A goes home conceeds 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv[1].append(str(t[1][inn]) + "/" + str(arr[1][1][inn]))
        awayConceedOvUvHomeConceedOvUv[2].append("TAConceed1TeamHConceed1+")
        awayConceedOvUvHomeConceedOvUv[3].append("AwayGamesPatt")
# Team A/Away conceeds 1 Goal, Team A goes home conceeds 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv2[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[1][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAConceed1TeamHConceed2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
# Team A/Away conceeds 1 Goal, Team A goes home conceeds 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv3[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv3[1].append(str(t[3][inn]) + "/" + str(arr[1][3][inn]))
        awayConceedOvUvHomeConceedOvUv3[2].append("TAConceed1TeamHConceed3+")
        awayConceedOvUvHomeConceedOvUv3[3].append("AwayGamesPatt")
# Team A/Away conceeds 1 Goal, Team A goes home conceeds 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv4[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv4[1].append(str(t[4][inn]) + "/" + str(arr[1][4][inn]))
        awayConceedOvUvHomeConceedOvUv4[2].append("TAConceed1TeamHConceed4+")
        awayConceedOvUvHomeConceedOvUv4[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away conceeds 2 Goal, Team A goes home conceeds 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv5[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv5[1].append(str(arr[2][1][inn]) + "/" + str(arr[3][1][inn]))
        awayConceedOvUvHomeConceedOvUv5[2].append("TAConceed2TeamHConceed1+")
        awayConceedOvUvHomeConceedOvUv5[3].append("AwayGamesPatt")
# Team A/Away conceeds 2 Goal, Team A goes home conceeds 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv6[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv6[1].append(str(arr[2][2][inn]) + "/" + str(arr[3][2][inn]))
        awayConceedOvUvHomeConceedOvUv6[2].append("TAConceed2TeamHConceed2+")
        awayConceedOvUvHomeConceedOvUv6[3].append("AwayGamesPatt")
# Team A/Away conceeds 2 Goal, Team A goes home conceeds 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv7[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv7[1].append(str(arr[2][3][inn]) + "/" + str(arr[3][3][inn]))
        awayConceedOvUvHomeConceedOvUv7[2].append("TAConceed2TeamHConcee3+")
        awayConceedOvUvHomeConceedOvUv7[3].append("AwayGamesPatt")
# Team A/Away conceeds 2 Goal, Team A goes home conceeds 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv8[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv8[1].append(str(arr[2][4][inn]) + "/" + str(arr[3][4][inn]))
        awayConceedOvUvHomeConceedOvUv8[2].append("TAConceed2TeamHConcee4+")
        awayConceedOvUvHomeConceedOvUv8[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away conceeds 3 Goal, Team A goes home conceeds 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv9[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv9[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv9[2].append("TAConceed3TeamHConceed1+")
        awayConceedOvUvHomeConceedOvUv9[3].append("AwayGamesPatt")
# Team A/Away conceeds 3 Goal, Team A goes home conceeds 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAConceed3TeamHConceed2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away conceeds 3 Goal, Team A goes home conceeds 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAConceed3TeamHConcee3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away conceeds 3 Goal, Team A goes home conceeds 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAConceed3TeamHConcee4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")
#============================================================================================
# Team A/Away Scores 1 Goal, Team A goes home scores 1 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv13[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv13[1].append(str(arr[4][1][inn]) + "/" + str(arr[5][1][inn]))
        awayConceedOvUvHomeConceedOvUv13[2].append("TACScores3TeamHScores1+")
        awayConceedOvUvHomeConceedOvUv13[3].append("AwayGamesPatt")
# Team A/Away Scores 4 Goal, Team A goes home Scores 2 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv10[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv10[1].append(str(arr[4][2][inn]) + "/" + str(arr[5][2][inn]))
        awayConceedOvUvHomeConceedOvUv10[2].append("TAConceed3TeamHScores2+")
        awayConceedOvUvHomeConceedOvUv10[3].append("AwayGamesPatt")
# Team A/Away Scores 4 Goal, Team A goes home Scores 3 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv11[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv11[1].append(str(arr[4][3][inn]) + "/" + str(arr[5][3][inn]))
        awayConceedOvUvHomeConceedOvUv11[2].append("TAConceed3TeamHScores3+")
        awayConceedOvUvHomeConceedOvUv11[3].append("AwayGamesPatt")
# Team A/Away Scores 4 Goal, Team A goes home Scores 4 Goal fulltime       
        awayConceedOvUvHomeConceedOvUv12[0].append(str(t[0][inn]))         
        awayConceedOvUvHomeConceedOvUv12[1].append(str(arr[4][4][inn]) + "/" + str(arr[5][4][inn]))
        awayConceedOvUvHomeConceedOvUv12[2].append("TAConceed3TeamHScores4+")
        awayConceedOvUvHomeConceedOvUv12[3].append("AwayGamesPatt")

        inn += 1
        if aa == inn:
           bb = True
           break;
   

 mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2,awayConceedOvUvHomeConceedOvUv3,awayConceedOvUvHomeConceedOvUv4,awayConceedOvUvHomeConceedOvUv5,awayConceedOvUvHomeConceedOvUv6,awayConceedOvUvHomeConceedOvUv7,awayConceedOvUvHomeConceedOvUv8,awayConceedOvUvHomeConceedOvUv9,awayConceedOvUvHomeConceedOvUv10,awayConceedOvUvHomeConceedOvUv11,awayConceedOvUvHomeConceedOvUv12)
 createReport(mulLayerInfor,pd)
          
aScHsc()    
    
         
  
  