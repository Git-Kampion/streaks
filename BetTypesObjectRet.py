#BetTypesObjectRet.py
class BtOr:
    """"
    def mergeData(arrayOFData):
     mergedDAta = []
     
     return mergedDAta

     
insert_stmt = "select * from LaLiga"
data = ("Chelsea")
cursor.execute(insert_stmt)
sql_data2 = pd.DataFrame(cursor.fetchall())
teamCount2 = 0
halftomeGap2 = 2

arr = ([sql_data,sql_data2])  

mergedFrame = BtOr.mergeData(arr)
    """
    def findConcurrentMAtche(t,data,betype,ht):
        count = 0
        highestMatch = 0
       
        for r in data:
            if r[ht] == t and r[7] == 3:
                count = count + 1
            else:
                if count > 1:
                 highestMatch = count
                 count = 0
                else:
                    count = 0            
        return highestMatch
    
    def refindedDatam(t,data,ht):
         refindedData = []
         for o in data[0]:           
            if t == o[ht]:
              refindedData.append(o)
         return refindedData

    def ScoredWholeSeaon(t,data,betype,ht):
        count = 0
        notCount = 0
        arr = ([],[])
        highestMatch = 0
               
        for r in data:

            con = int(r[ht])
            if con >= 1:
                count = count + 1
            else:
                 notCount = notCount + 1    
        arr = ([count,notCount])       
        return arr
    
    def ndScoredWholeSeaon(t,data,betype,ht):
        count = 0
        notCount = 0
        arr = ([],[])
        highestMatch = 0
               
        for r in data:
         con = int(r[ht])
         ad =  int(r[ht+2])
         if con > ad:
                count = count + 1
         else:
                 notCount = notCount + 1    
        arr = ([count,notCount])       
        return arr
    
    def ScoredBothHalvesSeaon(t,data,betype,ht):
        count = 0
        notCount = 0
        arr = ([],[])
        highestMatch = 0
          
        for r in data:
                con = int(r[ht])
                ad =  r[ht+2]
                con2 = int(ad)
                if con > con2 and con2 >= 1:
                    count = count + 1 
                else:
                    notCount = notCount + 1  
        arr = ([count,notCount])      
        return arr
    
    def ConceededBothHalvesSeaon(t,data,betype,ht):
        count = 0
        highestMatch = 0
               
        for r in data:
            if r[ht] > r[ht+2] and r[ht+2] >= 1:
                count = count + 1          
        return count
    def OverUnderSeaon(t,data,betype,ht):
        count = 0
        highestMatch = 0
        under0 = 0
        under1 = 0
        under2 = 0
        under3 = 0
        under4 = 0
        under5 = 0
        under6 = 0     
        countOv1 = 0
        countOv2 = 0
        countOv3 = 0
        countOv4 = 0
        countOv5 = 0
        countOv6 = 0
        overs = []
        unders = []
        #,countOv1,countOv2,countOv3,countOv4,countOv5,countOv6
        for r in data:   
            con = int(r[ht])
            match con:
                case 0:
                    under0 = under0 + 1
                    under1 = under1 + 1
                    under2 = under2 + 1
                    under3 = under3 + 1
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1 
                case 1:
                    count = count + 1
                  
                    under2 = under2 + 1
                    under3 = under3 + 1
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1 
                case 2:
                    count = count + 1
                    countOv1 = countOv1 + 1
                    
                  
                    under3 = under3 + 1
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1 
                 
                case 3:                                      
                    count = count + 1
                    countOv1 = countOv1 + 1
                    countOv2 = countOv2 + 1
                    
                   
                   
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1 
                case 4:                                      
                    count = count + 1
                    countOv1 = countOv1 + 1
                    countOv2 = countOv2 + 1
                    countOv3 = countOv3 + 1
                   
                   
                    under5 = under5 + 1
                    under6 = under6 + 1 
                case 5:                                      
                    count = count + 1
                    countOv1 = countOv1 + 1
                    countOv2 = countOv2 + 1
                    countOv3 = countOv3 + 1
                    countOv4 = countOv4 + 1
                    
                    
                   
                    under6 = under6 + 1 
                case 6:                                      
                    count = count + 1
                    countOv1 = countOv1 + 1
                    countOv2 = countOv2 + 1
                    countOv3 = countOv3 + 1
                    countOv4 = countOv4 + 1
                    countOv5 = countOv5 + 1
                    
                   
                   
                   
                case 7:                                      
                    count = count + 1
                    countOv1 = countOv1 + 1
                    countOv2 = countOv2 + 1
                    countOv3 = countOv3 + 1
                    countOv4 = countOv4 + 1
                    countOv5 = countOv5 + 1
                    countOv6 = countOv6 + 1
        overs.append(count)
        overs.append(countOv1)    
        overs.append(countOv2)    
        overs.append(countOv3)    
        overs.append(countOv4)    
        overs.append(countOv5)    
        overs.append(countOv6) 
        unders.append(under0)  
        unders.append(under1)  
        unders.append(under2)
        unders.append(under3)  
        unders.append(under4)
        unders.append(under5)
        unders.append(under6)  

        arr = ([overs,unders])  
        return arr
    
    
    def ConcededWholeSeaon(t,data,betype,ht):
        count = 0
        highestMatch = 0
               
        for r in data:
            if r[ht] >= 1:
                count = count + 1          
        return count

    def MatchRes(Title,body,cursor):
       
        cl1 =  body.split("\n")
        """
         HomeAttributes = []
        AwayAttributes = []
        HomeAttributes[0] = cl1[0]
        HomeAttributes[1] = cl1[1]
        DrawName = cl1[2]
        DrawOdd = cl1[3]
        HomeAttributes[2] = cl1[4]
        HomeAttributes[3] = cl1[5] 
        """
        insert_stmt = "INSERT INTO EplBetOdds(team,Match) VALUES (?,?)"
        

        dx = 0
        for lk in cl1: 
          if dx < 5:
            team =   cl1[dx] 
            odd = cl1[dx+1]
            data = ( team,odd)
            cursor.execute(insert_stmt,data)
            cursor.commit()
            dx = dx+5
        #return HomeAttributes
       
      
    def Bts(title,body):
         cl1 =  body.split("\n")
         YesLabel =   cl1[0]
         YesOdd =   cl1[1]
         NoLabel =   cl1[2]
         NoOdd =   cl1[3]
    
    def Dc(Title,body):
        cl1 =  body.split("\n")
        HomeNameDraw = cl1[0]
        HomeWinDrawOdd = cl1[1]
        AwayNameDraw = cl1[2]
        AwayWinDrawOdd = cl1[3]
        AwayWinHomeWin = cl1[4]
        AwayWinHomeWinOdd = cl1[5] 

    def DrawNoBet(title,body):
         cl1 =  body.split("\n")
         HomeLable =   cl1[0]
         HomeOdd =   cl1[1]
         AwayLabel =   cl1[2]
         AwayOdd =   cl1[3]

  

    def Handicap(Title,body):
        cl1 =  body.split("\n")
        HomeOverZeroLabel = cl1[0]
        HomeOverZero = cl1[1]
        AwayUnderZeroLabel = cl1[2]
        AwayUnderZero = cl1[3]
        HomeUnderZeroLabel = cl1[4]
        HomeUnderZero = cl1[5]           
        AwayOverZeroLabel = cl1[6]
        AwayOverZero = cl1[7]
        HomeOverOneLabel = cl1[8]
        HomeOverOne = cl1[9]  
        AwayUnderOneLabel = cl1[10]
        AwayUnderOne = cl1[11]
        HomeOverTwoLabel = cl1[12]
        HomeOverTwo = cl1[13]
        AwayUnderTwoLabel = cl1[14]
        AwayUnderTwo = cl1[15]
      
    def FirstGoal(Title,body):
        cl1 =  body.split("\n")
        HomeLabel = cl1[0]
        HomeFGoal = cl1[1]
        NoneLabel = cl1[2]
        NoneOdd = cl1[3]
        AwayLabel = cl1[4]
        AwayFGoal = cl1[5]     

    def TenMin(Title,body):
        cl1 =  body.split("\n")
        HomeLabel = cl1[0]
        HomeWinTen = cl1[1]
        DrawLabel = cl1[2]
        DrawOdd = cl1[3]
        AwayLabel = cl1[4]
        AwayWinTen = cl1[5]     

    def BothHalfsOever(title,body):
         cl1 =  body.split("\n")
         BHOYesLabel =   cl1[0]
         BHOYesOdd =   cl1[1]
         BHONoLabel =   cl1[2]
         BHONoOdd =   cl1[3]  

    def BothHalfsUnder(title,body):
         cl1 =  body.split("\n")
         BHUYesLabel =   cl1[0]
         BHUYesOdd =   cl1[1]
         BHUNoLabel =   cl1[2]
         BHUNoOdd =   cl1[3] 
       
    def MultiGoals(title,body):
         cl1 =  body.split("\n")
         BHUYesLabel =   cl1[0]
         BHUYesOdd =   cl1[1]
         BHUNoLabel =   cl1[2]
         BHUNoOdd =   cl1[3] 

    def SendingOff(title,body):
         cl1 =  body.split("\n")
         BHUYesLabel =   cl1[0]
         BHUYesOdd =   cl1[1]
         BHUNoLabel =   cl1[2]
         BHUNoOdd =   cl1[3]  

""""
    def insertIntoAccess(refined ,panelText):
        match panelText:
         case "Match":
         """
                
                    