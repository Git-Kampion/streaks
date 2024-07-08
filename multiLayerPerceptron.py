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

def matchScore(num):

 arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4]
 return arr

def createReport(data1,pd):
 
 #with pd.ExcelWriter('Homestreaks.xlsx') as writer:
 with pd.ExcelWriter('multistreaks.xlsx') as writer:

  for ff in data1:
   if len(ff) >= 1: 

      sheetName =  ff[2][1]
      df2 = pd.DataFrame(list(zip(ff[1],ff[2])),ff[0],columns =[ff[3][1],sheetName])
      df2.to_excel(writer, sheet_name=sheetName )  
   



awayConceedOvUvHomeConceedOvUv = ([],[],[],[])
awayConceedOvUvHomeConceedOvUv2 = ([],[],[],[])


overs = ([],[],[],[],[])
unders = ([],[],[],[],[])

Aunders = ([],[],[],[],[])
Aovers = ([],[],[],[],[])


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


   index = 0
   indx = True
   indxFound = False
   
   if ee[4] not in Ateams:
    teamFound = True
    Ateams.append(ee[4])
    t = ee[4]
    if t == "Ternana":
     cons = 0
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
            if int(bb[6]) > 4:
                ws = 4
            match int(ec[5]):
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
    teamFound = False

arr = (Aovers,Aunders,ATovers,ATunders)
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
        awayConceedOvUvHomeConceedOvUv2[1].append(str(t[2][inn]) + "/" + str(arr[0][2][inn]))
        awayConceedOvUvHomeConceedOvUv2[2].append("TAConceed1TeamHConceed2+")
        awayConceedOvUvHomeConceedOvUv2[3].append("AwayGamesPatt")
        inn += 1
        if aa == inn:
           bb = True
           break;
   

mulLayerInfor = (awayConceedOvUvHomeConceedOvUv,awayConceedOvUvHomeConceedOvUv2)
createReport(mulLayerInfor,pd)
          
    
    
         
  
  