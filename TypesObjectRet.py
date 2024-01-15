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
    
    def FixOverUnders(t,data,betype,ht):
        countO = 0
        countOv1 = 0
        countOv2 = 0
        countOv3 = 0
        countOv4 = 0
        countOv5 = 0
        countOv6 = 0

        under0 = 0
        under1 = 0
        under2 = 0
        under3 = 0
        under4 = 0
        under5 = 0
        under6 = 0
        overs = []
        unders = []
        for r in data:
            if betype == "k":
             Hcon = int(r[ht])
             Acon = int(r[ht + 1])
            else:
             Hcon = int(r[ht - 1])
             Acon = int(r[ht])
            FullScore = Hcon + Acon
            
            if FullScore == 0:
                under0 = under0 + 1
                under1 = under1 + 1
                under2 = under2 + 1
                under3 = under3 + 1
                under4 = under4 + 1
                under5 = under5 + 1
                under6 = under6 + 1
            if FullScore == 1:
                countOv1 = countOv1 + 1
                
                under2 = under2 + 1
                under3 = under3 + 1
                under4 = under4 + 1
                under5 = under5 + 1
                under6 = under6 + 1
            if FullScore == 2:
                countOv1 = countOv1 + 1
                countOv2 = countOv2 + 1
                
                
                under3 = under3 + 1
                under4 = under4 + 1
                under5 = under5 + 1
                under6 = under6 + 1
            if FullScore == 3:
                countOv1 = countOv1 + 1
                countOv2 = countOv2 + 1
                countOv3 = countOv3 + 1
                
                under4 = under4 + 1
                under5 = under5 + 1
                under6 = under6 + 1
            if FullScore == 4:
                countOv1 = countOv1 + 1
                countOv2 = countOv2 + 1
                countOv3 = countOv3 + 1
                countOv4 = countOv4 + 1
                
             
                under5 = under5 + 1
                under6 = under6 + 1
            if FullScore == 5:
                countOv1 = countOv1 + 1
                countOv2 = countOv2 + 1
                countOv3 = countOv3 + 1
                countOv4 = countOv4 + 1
                countOv5 = countOv5 + 1
                

                under6 = under6 + 1
            
            if FullScore >= 6:
                countOv1 = countOv1 + 1
                countOv2 = countOv2 + 1
                countOv3 = countOv3 + 1
                countOv4 = countOv4 + 1
                countOv5 = countOv5 + 1
                countOv6 = countOv6 + 1
                            
            
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

        
        arr = ([overs,unders])
        return arr

    def Bts(t,data,betype,ht):
        
       count = 0
       notCount = 0
       arr = ([],[])
       for r in data:
            if betype == "k":
             Hcon = int(r[ht])
             Acon = int(r[ht + 1])
            else:
             Hcon = int(r[ht - 1])
             Acon = int(r[ht])

            if Hcon > 0 and Acon > 0:
                count = count +1
            else:
                notCount = notCount+1
       arr = ([count,notCount])
       return arr
    
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
         if con >= ad:
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

        SecHcount = 0     
        SecHcountOv1 = 0
        SecHcountOv2 = 0
        SecHcountOv3 = 0
        SecHcountOv4 = 0
        SecHcountOv5 = 0
        SecHcountOv6 = 0

        Secunder0 = 0
        Secunder1 = 0
        Secunder2 = 0
        Secunder3 = 0
        Secunder4 = 0
        Secunder5 = 0
        Secunder6 = 0

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

        FrstHConcedcount = 0     
        FrstHConcedcountOv1 = 0
        FrstHConcedcountOv2 = 0
        FrstHConcedcountOv3 = 0
        FrstHConcedcountOv4 = 0
        FrstHConcedcountOv5 = 0
        FrstHConcedcountOv6 = 0

        FrstHConcedunder0 = 0
        FrstHConcedunder1 = 0
        FrstHConcedunder2 = 0
        FrstHConcedunder3 = 0
        FrstHConcedunder4 = 0
        FrstHConcedunder5 = 0
        FrstHConcedunder6 = 0

        overs = []
        unders = []

        Concedovers = []
        Concedunders = []

        FrstHalfovers = []
        FrstHalfunders = []

        SecondHalfovers = []
        SecondHalfunders = []

        FrstHalfConcedovers = []
        FrstHalfConcedunders = []
        

        for r in data:
         if betype == "k":
             Hcon = int(r[ht])
             HomFrstHlf = int(r[ht + 2])

             if Hcon == HomFrstHlf:
               HomSecHlf = Hcon
             else:
              HomSecHlf = Hcon - HomFrstHlf

             Acon = int(r[ht + 1])
             AFrstHlf = int(r[ht + 3])

             if Acon == AFrstHlf:
              ASecHlf = AFrstHlf
             else:
                 ASecHlf = Acon - AFrstHlf
                
        else:
             Hcon = int(r[ht - 1])
             HomFrstHlf = Hcon + 2
             if Hcon == HomFrstHlf:
               HomSecHlf = Hcon
             else:
              HomSecHlf = Hcon - HomFrstHlf

             Acon = int(r[ht])
             AFrstHlf = Acon+ 2

             if Acon == AFrstHlf:
              ASecHlf = AFrstHlf
             else:
                ASecHlf = Acon - AFrstHlf
            

             match Acon:
              case 0:                 
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
        overs.append(count)        
        overs.append(countOv1)        
        overs.append(countOv2)    
        overs.append(countOv3)
        overs.append(countOv4)
        overs.append(countOv5)
        overs.append(countOv6)

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

    def MatchRes(body,cursor):
        insert_stmt = "INSERT INTO EplBetOdds(HTeam,ATeam,HWinOd,AWinOd,BTSyes,BTSno) VALUES (?,?,?,?,?,?)"
        for kk in body:
       
         cl1 =  kk.split("\n")
         
         Hteam =   cl1[0] 
         Hwind = cl1[1]
         Ateam =   cl1[4] 
         Awind = cl1[5]


        data = ( Hteam,Ateam,Hwind,Awind)
        cursor.execute(insert_stmt,data)
        cursor.commit()
        
    
    
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


                
                    