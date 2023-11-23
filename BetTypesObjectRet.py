#BetTypesObjectRet.py
class BtOr:

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
    
    def ConcededBothHalvesSeaon(t,data,betype,ht):
        count = 0
        highestMatch = 0
               
        for r in data:
            if r[ht] > r[ht+2] and r[ht+2] >= 1:
                count = count + 1          
        return count
    def OverUnderSeaon(t,data,betype,ht):
        count = 0     
        countOv1 = 0
        countOv2 = 0
        countOv3 = 0
        countOv4 = 0
        countOv5 = 0
        countOv6 = 0

        FrstHcount = 0     
        FrstHcountOv1 = 0
        FrstHcountOv2 = 0
        FrstHcountOv3 = 0
        FrstHcountOv4 = 0
        FrstHcountOv5 = 0
        FrstHcountOv6 = 0

        under0 = 0
        under1 = 0
        under2 = 0
        under3 = 0
        under4 = 0
        under5 = 0
        under6 = 0

        Frstunder0 = 0
        Frstunder1 = 0
        Frstunder2 = 0
        Frstunder3 = 0
        Frstunder4 = 0
        Frstunder5 = 0
        Frstunder6 = 0

        Concedcount = 0     
        ConcedcountOv1 = 0
        ConcedcountOv2 = 0
        ConcedcountOv3 = 0
        ConcedcountOv4 = 0
        ConcedcountOv5 = 0
        ConcedcountOv6 = 0

        Concedunder0 = 0
        Concedunder1 = 0
        Concedunder2 = 0
        Concedunder3 = 0
        Concedunder4 = 0
        Concedunder5 = 0
        Concedunder6 = 0

        overs = []
        unders = []

        Concedovers = []
        Concedunders = []

        FrstHalfovers = []
        FrstHalfunders = []
        
        for r in data:   
            con = int(r[ht])
            conced = int(r[ht+1])
            HomFrstHlf = int(r[ht+2])
            match con:
                case 0:                 
                    under0 = under0 + 1
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
                    countOv1 = countOv1 +1
                    
                    under3 = under3 + 1
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1

                case 3:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1

                    
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1

                case 4:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1

                    
                    
                    under5 = under5 + 1
                    under6 = under6 + 1
                  
                case 5:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1
                    countOv4 = countOv4 +1
                case 6:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1
                    countOv4 = countOv4 +1
                    countOv5 = countOv5 +1
            match conced:
                case 0:                 
                    Concedunder0 = Concedunder0 + 1
                    Concedunder2 = Concedunder2 + 1
                    Concedunder3 = Concedunder3 + 1
                    Concedunder4 = Concedunder4 + 1
                    Concedunder5 = Concedunder5 + 1
                    Concedunder6 = Concedunder6 + 1
                case 1:                 
                    Concedcount = Concedcount + 1
                    Concedunder2 = Concedunder2 + 1
                    Concedunder3 = Concedunder3 + 1
                    Concedunder4 = Concedunder4 + 1
                    Concedunder5 = Concedunder5 + 1
                    Concedunder6 = Concedunder6 + 1

                case 2:                 
                    Concedcount = Concedcount + 1
                    ConcedcountOv1 = ConcedcountOv1 +1
                    
                    Concedunder3 = Concedunder3 + 1
                    Concedunder4 = Concedunder4 + 1
                    Concedunder5 = Concedunder5 + 1
                    Concedunder6 = Concedunder6 + 1

                case 3:                 
                    Concedcount = Concedcount + 1
                    ConcedcountOv1 = ConcedcountOv1 +1
                    ConcedcountOv2 = ConcedcountOv2 +1

                    
                    Concedunder4 = Concedunder4 + 1
                    Concedunder5 = Concedunder5 + 1
                    Concedunder6 = Concedunder6 + 1

                case 4:                 
                    Concedcount = Concedcount + 1
                    ConcedcountOv1 = ConcedcountOv1 +1
                    ConcedcountOv2 = ConcedcountOv2 +1
                    ConcedcountOv3 = ConcedcountOv3 +1

                    
                    
                    Concedunder5 = Concedunder5 + 1
                    Concedunder6 = Concedunder6 + 1
                  
                case 5:                 
                    Concedcount = Concedcount + 1
                    ConcedcountOv1 = ConcedcountOv1 +1
                    ConcedcountOv2 = ConcedcountOv2 +1
                    ConcedcountOv3 = ConcedcountOv3 +1
                    ConcedcountOv4 = ConcedcountOv4 +1
                case 6:                 
                    Concedcount = Concedcount + 1
                    ConcedcountOv1 = ConcedcountOv1 +1
                    ConcedcountOv2 = ConcedcountOv2 +1
                    ConcedcountOv3 = ConcedcountOv3 +1
                    ConcedcountOv4 = ConcedcountOv4 +1
                    ConcedcountOv5 = ConcedcountOv5 +1        
                    
            match HomFrstHlf:
                case 0:                 
                    under0 = under0 + 1
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
                    countOv1 = countOv1 +1
                    
                    under3 = under3 + 1
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1

                case 3:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1

                    
                    under4 = under4 + 1
                    under5 = under5 + 1
                    under6 = under6 + 1

                case 4:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1

                    
                    
                    under5 = under5 + 1
                    under6 = under6 + 1
                  
                case 5:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1
                    countOv4 = countOv4 +1
                case 6:                 
                    count = count + 1
                    countOv1 = countOv1 +1
                    countOv2 = countOv2 +1
                    countOv3 = countOv3 +1
                    countOv4 = countOv4 +1
                    countOv5 = countOv5 +1        
                  
        overs.append(count)        
        overs.append(countOv1)        
        overs.append(countOv2)    
        overs.append(countOv3)
        overs.append(countOv4)
        overs.append(countOv5)
        overs.append(countOv6)

        unders.append(under0)
        unders.append(under2)
        unders.append(under3)
        unders.append(under4)
        unders.append(under5)
        unders.append(under6)

        Concedovers.append(Concedcount)        
        Concedovers.append(ConcedcountOv1)        
        Concedovers.append(ConcedcountOv2)    
        Concedovers.append(ConcedcountOv3)
        Concedovers.append(ConcedcountOv4)
        Concedovers.append(ConcedcountOv5)
        Concedovers.append(ConcedcountOv6)

        Concedunders.append(Concedunder0)
        Concedunders.append(Concedunder2)
        Concedunders.append(Concedunder3)
        Concedunders.append(Concedunder4)
        Concedunders.append(Concedunder5)
        Concedunders.append(Concedunder6)

        arr = ([overs,unders,Concedovers,Concedunders,t])  
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
                
                    