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
        FrstAOver = 0
        FrstAOver1 = 0
        FrstAOver2 = 0

        ASecunder0 = 0
        ASecunder1 = 0
        ASecunder2 = 0
        ASecOver0 = 0
        ASecOver1 = 0
        ASecOver2 = 0


        Concedcount = 0     
        ConcedcountOv1 = 0
        ConcedcountOv2 = 0
        ConcedcountOv3 = 0
        ConcedcountOv4 = 0
        ConcedcountOv5 = 0
        ConcedcountOv6 = 0

        AwayFrstConcedUnder0 = 0
        AwayFrstConcedUnder1 = 0
        AwayFrstConcedUnder2 = 0
        AwayFrstConcedUnder3 = 0
        AwayFrstConcedUnder4 = 0
        AwayFrstConcedUnder5 = 0
        AwayFrstConcedUnder6 = 0

        AwayFrstConcedcount = 0
        AwayFrstConcedcountOv2 = 0
        AwayFrstConcedcountOv3 = 0
        
        AwayFrstConcedcountOv4 = 0

        AwaySecConcedcount = 0     
        AwaySecConcedcountOv1 = 0
        AwaySecConcedcountOv2 = 0
        AwaySecConcedcountOv3 = 0
        AwaySecConcedcountOv4 = 0
        AwaySecConcedcountOv5 = 0
        AwaySecConcedcountOv6 = 0

        AwaySecConcedUnder0 = 0     
        AwaySecConcedUnder1 = 0
        AwaySecConcedUnder2 = 0
        AwaySecConcedUnder3 = 0
        AwaySecConcedUnder4 = 0
        AwaySecConcedUnder5 = 0
        AwaySecConcedUnder6 = 0

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
        FrstHalfAovers = []       
        FrstHalfAunders = []

        SecHalfAovers = []
        SecHalfAUnders = []

        Concedovers = []
        Concedunders = []

        AwayConcedFirstHovers = []
        AwayConcedSecHovers = []
        AwayConcedSecHunder = []
        AwayConcedFirstHunder = []
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
               HomSecHlf = 0
             else:
              HomSecHlf = Hcon - HomFrstHlf

             Acon = int(r[ht + 1])
             AFrstHlf = int(r[ht + 3])

             if Acon == AFrstHlf:
              ASecHlf = 0
             else:
                 ASecHlf = Acon - AFrstHlf       
         else:
             Hcon = int(r[ht - 1])
             HomFrstHlf = int(r[ht + 1]) 
             if Hcon == HomFrstHlf:
               HomSecHlf = 0
             else:
              HomSecHlf = Hcon - HomFrstHlf

             Acon = int(r[ht])
             AFrstHlf = int(r[ht + 2])

             if Acon == AFrstHlf:
              ASecHlf = 0
             else:
                ASecHlf = Acon - AFrstHlf
            
             match HomFrstHlf:
              case 0:  
                AwayFrstConcedUnder0 = AwayFrstConcedUnder0 + 1     
                AwayFrstConcedUnder1 = AwayFrstConcedUnder1 + 1
                AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  
             
              case 1:    
                AwayFrstConcedcount = AwayFrstConcedcount + 1
                AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                AwayFrstConcedUnder1 = AwayFrstConcedUnder1 + 1
                AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1   
              case 2:    
                AwayFrstConcedcount = AwayFrstConcedcount + 1
                AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  

              case 3:  
                AwayFrstConcedcount = AwayFrstConcedcount + 1
                AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                AwayFrstConcedcountOv3 = AwayFrstConcedcountOv3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  
              case 4:                 
                 AwayFrstConcedcount = AwayFrstConcedcount + 1
                 AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                 AwayFrstConcedcountOv3 = AwayFrstConcedcountOv3 + 1
                 AwayFrstConcedcountOv4 = AwayFrstConcedcountOv4 + 1
                 AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                 AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  


             match HomSecHlf:
              case 0:  
                AwaySecConcedUnder0 = AwaySecConcedUnder0 + 1     
                AwaySecConcedUnder1 = AwaySecConcedUnder1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1  
             
              case 1:    
                AwaySecConcedcount = AwaySecConcedcount + 1
                AwaySecConcedUnder1 = AwaySecConcedUnder1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1  
              case 2:  
                AwaySecConcedcount = AwaySecConcedcount + 1  
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1

              case 3:  
                AwaySecConcedcount = AwaySecConcedcount + 1
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedcountOv2 = AwaySecConcedcountOv2 + 1               
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1
              case 4:  
                AwaySecConcedcount = AwaySecConcedcount + 1               
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedcountOv2 = AwaySecConcedcountOv2 + 1               
                AwaySecConcedcountOv3 = AwaySecConcedcountOv3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1

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
              case 5:                 
                count = count + 1
                countOv1 = countOv1 +1
                countOv2 = countOv2 +1
                countOv3 = countOv3 +1
                countOv4 = countOv4 +1
               
                under6 = under6 + 1
              case 6:                 
                count = count + 1
                countOv1 = countOv1 +1
                countOv2 = countOv2 +1
                countOv3 = countOv3 +1
                countOv4 = countOv4 +1
                countOv5 = countOv5 +1
                under6 = under6 + 1

             match AFrstHlf:
              case 0:                 
               Frstunder0 = Frstunder0 + 1
               Frstunder1 = Frstunder1 + 1
               Frstunder2 = Frstunder2 + 1
             
              case 1:    
                FrstAOver = FrstAOver + 1
                Frstunder1 = Frstunder1 + 1
                Frstunder2 = Frstunder2 + 1
              case 2:    
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               Frstunder2 = Frstunder2 + 1

              case 3:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1
              case 4:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1
              case 5:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1
              case 6:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1

             match ASecHlf:
              case 0:                 
               ASecunder0 = ASecunder0 + 1
               ASecunder1 = ASecunder1 + 1
               ASecunder2 = ASecunder2 + 1
             
              case 1:    
                ASecOver0 = ASecOver0 + 1
                ASecunder1 = ASecunder1 + 1
                ASecunder2 = ASecunder2 + 1
              case 2:    
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecunder2 = ASecunder2 + 1

              case 3:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1
              case 4:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1
              case 5:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1
              case 6:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1

        overs.append(count)        
        overs.append(countOv1)        
        overs.append(countOv2)    
        overs.append(countOv3)
        overs.append(countOv4)
        unders.append(under1)
        unders.append(under2)
        unders.append(under3)
        unders.append(under4)
        unders.append(under5)
        unders.append(under6)

        FrstHalfAovers.append(FrstAOver)        
        FrstHalfAovers.append(FrstAOver1)        
        FrstHalfAovers.append(FrstAOver2)    
        FrstHalfAunders.append(Frstunder0)        
        FrstHalfAunders.append(Frstunder1)        
        FrstHalfAunders.append(Frstunder2)   
     
        SecHalfAovers.append(ASecOver0)        
        SecHalfAovers.append(ASecOver1)        
        SecHalfAovers.append(ASecOver2)    
        SecHalfAUnders.append(ASecunder0)        
        SecHalfAUnders.append(ASecunder1)        
        SecHalfAUnders.append(ASecunder2)  

        AwayConcedFirstHovers.append(AwayFrstConcedcount)        
        
        AwayConcedFirstHovers.append(AwayFrstConcedcountOv2)        
        AwayConcedFirstHovers.append(AwayFrstConcedcountOv3)    
        AwayConcedFirstHovers.append(AwayFrstConcedcountOv4) 

        AwayConcedSecHovers.append(AwaySecConcedcount)        
        AwayConcedSecHovers.append(AwaySecConcedcountOv1)        
        AwayConcedSecHovers.append(AwaySecConcedcountOv2)        
        AwayConcedSecHovers.append(AwaySecConcedcountOv3)    
        AwayConcedSecHovers.append(AwaySecConcedcountOv4)   

        AwayConcedSecHunder.append(AwaySecConcedUnder0)    
        AwayConcedSecHunder.append(AwaySecConcedUnder1)        
        AwayConcedSecHunder.append(AwaySecConcedUnder2)    
        AwayConcedSecHunder.append(AwaySecConcedUnder3)      
        AwayConcedSecHunder.append(AwaySecConcedUnder4)   

        AwayConcedFirstHunder.append(AwayFrstConcedUnder0)        
        AwayConcedFirstHunder.append(AwayFrstConcedUnder1)        
        AwayConcedFirstHunder.append(AwayFrstConcedUnder2)    
        AwayConcedFirstHunder.append(AwayFrstConcedUnder3)      
        AwayConcedFirstHunder.append(AwayFrstConcedUnder4)         
        
       

        arr = ([overs,unders,FrstHalfAovers,FrstHalfAunders,SecHalfAovers,SecHalfAUnders,AwayConcedSecHovers,AwayConcedFirstHovers,AwayConcedSecHunder,AwayConcedFirstHunder])
        return arr
    
    
    def ConcededWholeSeaon(t,data,betype,ht):
        count = 0
        highestMatch = 0
               
        for r in data:
            if r[ht] >= 1:
                count = count + 1          
        return count

    def MatchRes(t,data,betype,ht):
      HomeWinCount = 0
      AwayWinCount = 0
      HomeFailToWin = 0
      AwayFailTowin = 0

      HomeFlvWinCount = 0
      AwayFlvWinCount = 0
      HomeFlvFailToWin = 0
      AwayFlvFailTowin = 0

      HomeSecFlvWinCount = 0
      AwaySecFlvWinCount = 0
      HomeSecFlvFailToWin = 0
      AwaySecFlvFailTowin = 0

      Hcon = 0
      HomFrstHlf = 0
      HomeSecHlf = 0

      Acon = 0
      AFrstHlf = 0
      AwSecHlf = 0
      for r in data:
        if betype == "k":
             Hcon = int(r[ht])
             HomFrstHlf = int(r[ht + 2])
             HomeSecHlf = Hcon - HomFrstHlf
        else:
             Acon = int(r[ht])
             AFrstHlf = int(r[ht + 2])
             AwSecHlf = Acon - AFrstHlf

        if Hcon > Acon:
           HomeWinCount = HomeWinCount + 1
           AwayFailTowin = AwayFailTowin + 1
        if Acon > Hcon:
           AwayWinCount = AwayWinCount + 1
           HomeFailToWin = HomeFailToWin + 1
        if Hcon == Acon:
           AwayFailTowin = AwayFailTowin + 1
           HomeFailToWin = HomeFailToWin + 1
      
        if HomFrstHlf > AFrstHlf:
           HomeFlvWinCount = HomeFlvWinCount + 1
           AwayFlvFailTowin = AwayFlvFailTowin + 1
        if AFrstHlf > HomFrstHlf:
           AwayFlvWinCount = AwayFlvWinCount + 1
           HomeFlvFailToWin = HomeFlvFailToWin + 1
        if HomFrstHlf == AFrstHlf:
           AwayFlvFailTowin = AwayFlvFailTowin + 1
           HomeFlvFailToWin = HomeFlvFailToWin + 1  

        if HomeSecHlf > AwSecHlf:
           HomeSecFlvWinCount = HomeSecFlvWinCount + 1
           AwaySecFlvFailTowin = AwaySecFlvFailTowin + 1
        if AFrstHlf > HomFrstHlf:
           AwaySecFlvWinCount = AwaySecFlvWinCount + 1
           HomeSecFlvFailToWin = HomeSecFlvFailToWin + 1
        if HomFrstHlf == AFrstHlf:
           AwaySecFlvFailTowin = AwaySecFlvFailTowin + 1
           HomeSecFlvFailToWin = HomeSecFlvFailToWin + 1  



      arr = ([HomeWinCount,AwayFailTowin,AwayWinCount,HomeFailToWin,HomeFlvWinCount,AwayFlvFailTowin,AwayFlvWinCount,HomeFlvFailToWin,HomeSecFlvWinCount,AwaySecFlvFailTowin,AwaySecFlvWinCount,HomeSecFlvFailToWin])  
      return arr
    
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


                
                    