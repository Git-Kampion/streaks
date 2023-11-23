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
            con = int(r[ht])
            conced = int(r[ht+1])
            HomFrstHlf = int(r[ht+2])
            HomSecHlf = int(r[ht])
            FirstHconced = int(r[ht+3])
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
                    Frstunder0 = Frstunder0 + 1
                    Frstunder2 = Frstunder2 + 1
                    Frstunder3 = Frstunder3 + 1
                    Frstunder4 = Frstunder4 + 1
                    Frstunder5 = Frstunder5 + 1
                    Frstunder6 = Frstunder6 + 1
                case 1:                 
                    FrstHcount = FrstHcount + 1
                    Frstunder2 = Frstunder2 + 1
                    Frstunder3 = Frstunder3 + 1
                    Frstunder4 = Frstunder4 + 1
                    Frstunder5 = Frstunder5 + 1
                    Frstunder6 = Frstunder6 + 1

                case 2:                 
                    FrstHcount = FrstHcount + 1
                    FrstHcountOv1 = FrstHcountOv1 +1
                    
                    Frstunder3 = Frstunder3 + 1
                    Frstunder4 = Frstunder4 + 1
                    Frstunder5 = Frstunder5 + 1
                    Frstunder6 = Frstunder6 + 1

                case 3:                 
                    FrstHcount = FrstHcount + 1
                    FrstHcountOv1 = FrstHcountOv1 +1
                    FrstHcountOv2 = FrstHcountOv2 +1

                    
                    Frstunder4 = Frstunder4 + 1
                    Frstunder5 = Frstunder5 + 1
                    Frstunder6 = Frstunder6 + 1
                case 4:                 
                    FrstHcount = FrstHcount + 1
                    FrstHcountOv1 = FrstHcountOv1 +1
                    FrstHcountOv2 = FrstHcountOv2 +1
                    FrstHcountOv3 = FrstHcountOv3 +1

                    
                    
                    Frstunder5 = Frstunder5 + 1
                    Frstunder6 = Frstunder6 + 1
                  
                case 5:                 
                    FrstHcount =  FrstHcount + 1
                    FrstHcountOv1 =  FrstHcountOv1 +1
                    FrstHcountOv2 = FrstHcountOv2 +1
                    FrstHcountOv3 = FrstHcountOv3 +1
                    FrstHcountOv4 = FrstHcountOv4 +1
                    Frstunder6 = Frstunder6 + 1
                case 6:                 
                    FrstHcount = FrstHcount + 1
                    FrstHcountOv1 = FrstHcountOv1 +1
                    FrstHcountOv2 = FrstHcountOv2 +1
                    FrstHcountOv3 = FrstHcountOv3 +1
                    FrstHcountOv4 = FrstHcountOv4 +1
                    FrstHcountOv5 = FrstHcountOv5 +1     
            HomSecHlf = HomSecHlf - HomFrstHlf
            if HomSecHlf > 0:
             match HomSecHlf:
                case 0:                 
                   Secunder0 = Secunder0 + 1
                case 1:                 
                    SecHcount = SecHcount + 1
                    Secunder2 = Secunder2 + 1
                    Secunder3 = Secunder3 + 1
                    Secunder4 = Secunder4 + 1
                    Secunder5 = Secunder5 + 1
                    Secunder6 = Secunder6 + 1

                case 2:                 
                    SecHcount = SecHcount + 1
                    SecHcountOv1 = SecHcountOv1 +1
                    
                    Secunder3 = Secunder3 + 1
                    Secunder4 = Secunder4 + 1
                    Secunder5 = Secunder5 + 1
                    Secunder6 = Secunder6 + 1

                case 3:                 
                    SecHcount = SecHcount + 1
                    SecHcountOv1 = SecHcountOv1 +1
                    SecHcountOv2 = SecHcountOv2 +1

                    
                    Secunder4 = Secunder4 + 1
                    Secunder5 = Secunder5 + 1
                    Secunder6 = Secunder6 + 1
                case 4:                 
                    SecHcount = SecHcount + 1
                    SecHcountOv1 = SecHcountOv1 +1
                    SecHcountOv2 = SecHcountOv2 +1
                    SecHcountOv3 = SecHcountOv3 +1

                    
                    
                    Secunder5 = Secunder5 + 1
                    Secunder6 = Secunder6 + 1
                  
                case 5:                 
                    SecHcount =  SecHcount + 1
                    SecHcountOv1 =  SecHcountOv1 +1
                    SecHcountOv2 = SecHcountOv2 +1
                    SecHcountOv3 = SecHcountOv3 +1
                    SecHcountOv4 = SecHcountOv4 +1
                    Secunder6 = Secunder6 + 1
                case 6:                 
                    SecHcount = SecHcount + 1
                    SecHcountOv1 = SecHcountOv1 +1
                    SecHcountOv2 = SecHcountOv2 +1
                    SecHcountOv3 = SecHcountOv3 +1
                    SecHcountOv4 = SecHcountOv4 +1
                    SecHcountOv5 = SecHcountOv5 +1        
            else:
                    Secunder0 = Secunder0 + 1
                    Secunder2 = Secunder2 + 1
                    Secunder3 = Secunder3 + 1
                    Secunder4 = Secunder4 + 1
                    Secunder5 = Secunder5 + 1
                    Secunder6 = Secunder6 + 1
            
            match FirstHconced:
                case 0:                 
                    FrstHConcedunder0 = FrstHConcedunder0 + 1
                    FrstHConcedunder2 = FrstHConcedunder2 + 1
                    FrstHConcedunder3 = FrstHConcedunder3 + 1
                    FrstHConcedunder4 = FrstHConcedunder4 + 1
                    FrstHConcedunder5 = FrstHConcedunder5 + 1
                    FrstHConcedunder6 = FrstHConcedunder6 + 1
                case 1:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedunder2 = FrstHConcedunder2 + 1
                    FrstHConcedunder3 = FrstHConcedunder3 + 1
                    FrstHConcedunder4 = FrstHConcedunder4 + 1
                    FrstHConcedunder5 = FrstHConcedunder5 + 1
                    FrstHConcedunder6 = FrstHConcedunder6 + 1

                case 2:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedcountOv1 = FrstHConcedcountOv1 +1
                    
                    FrstHConcedunder3 = FrstHConcedunder3 + 1
                    FrstHConcedunder4 = FrstHConcedunder4 + 1
                    FrstHConcedunder5 = FrstHConcedunder5 + 1
                    FrstHConcedunder6 = FrstHConcedunder6 + 1

                case 3:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedcountOv1 = FrstHConcedcountOv1 +1
                    FrstHConcedcountOv2 = FrstHConcedcountOv2 +1

                    
                    FrstHConcedunder4 = FrstHConcedunder4 + 1
                    FrstHConcedunder5 = FrstHConcedunder5 + 1
                    FrstHConcedunder6 = FrstHConcedunder6 + 1

                case 4:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedcountOv1 = FrstHConcedcountOv1 +1
                    FrstHConcedcountOv2 = FrstHConcedcountOv2 +1
                    FrstHConcedcountOv3 = FrstHConcedcountOv3 +1

                    
                    
                    FrstHConcedunder5 = FrstHConcedunder5 + 1
                    FrstHConcedunder6 = FrstHConcedunder6 + 1
                  
                case 5:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedcountOv1 = FrstHConcedcountOv1 +1
                    FrstHConcedcountOv2 = FrstHConcedcountOv2 +1
                    FrstHConcedcountOv3 = FrstHConcedcountOv3 +1
                    FrstHConcedcountOv4 = FrstHConcedcountOv4 +1
                case 6:                 
                    FrstHConcedcount = FrstHConcedcount + 1
                    FrstHConcedcountOv1 = FrstHConcedcountOv1 +1
                    FrstHConcedcountOv2 = FrstHConcedcountOv2 +1
                    FrstHConcedcountOv3 = FrstHConcedcountOv3 +1
                    FrstHConcedcountOv4 = FrstHConcedcountOv4 +1
                    FrstHConcedcountOv5 = FrstHConcedcountOv5 +1  
                    
        overs.append(count)        
        overs.append(countOv1)        
        overs.append(countOv2)    
        overs.append(countOv3)
        overs.append(countOv4)
        overs.append(countOv5)
        overs.append(countOv6)

        FrstHalfovers.append(FrstHcount)        
        FrstHalfovers.append(FrstHcountOv1)        
        FrstHalfovers.append(FrstHcountOv2)    
        FrstHalfovers.append(FrstHcountOv3)
        FrstHalfovers.append(FrstHcountOv4)
        FrstHalfovers.append(FrstHcountOv5)

        SecondHalfovers.append(SecHcount)        
        SecondHalfovers.append(SecHcountOv1)        
        SecondHalfovers.append(SecHcountOv2)    
        SecondHalfovers.append(SecHcountOv3)
        SecondHalfovers.append(SecHcountOv4)
        SecondHalfovers.append(SecHcountOv5)
        

        unders.append(under0)
        unders.append(under2)
        unders.append(under3)
        unders.append(under4)
        unders.append(under5)
        unders.append(under6)

        FrstHalfunders.append(Frstunder0)
        FrstHalfunders.append(Frstunder2)
        FrstHalfunders.append(Frstunder3)
        FrstHalfunders.append(Frstunder4)
        FrstHalfunders.append(Frstunder5)
        FrstHalfunders.append(Frstunder6)

        SecondHalfunders.append(Secunder0)
        SecondHalfunders.append(Secunder2)
        SecondHalfunders.append(Secunder3)
        SecondHalfunders.append(Secunder4)
        SecondHalfunders.append(Secunder5)
        SecondHalfunders.append(Secunder6)

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

        FrstHalfConcedovers.append(FrstHConcedcount)        
        FrstHalfConcedovers.append(FrstHConcedcountOv1)        
        FrstHalfConcedovers.append(FrstHConcedcountOv2)    
        FrstHalfConcedovers.append(FrstHConcedcountOv3)
        FrstHalfConcedovers.append(FrstHConcedcountOv4)
        FrstHalfConcedovers.append(FrstHConcedcountOv5)
        FrstHalfConcedovers.append(FrstHConcedcountOv6)

        FrstHalfConcedunders.append(FrstHConcedunder0)
        FrstHalfConcedunders.append(FrstHConcedunder2)
        FrstHalfConcedunders.append(FrstHConcedunder3)
        FrstHalfConcedunders.append(FrstHConcedunder4)
        FrstHalfConcedunders.append(FrstHConcedunder5)
        FrstHalfConcedunders.append(FrstHConcedunder6)

        arr = ([overs,unders,Concedovers,Concedunders ,FrstHalfovers,FrstHalfunders,SecondHalfovers,SecondHalfunders,FrstHalfConcedovers,FrstHalfConcedunders,t])  
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


                
                    