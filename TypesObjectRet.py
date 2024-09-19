#BetTypesObjectRet.py
import pandas as pd
class BtOr:
   
       
    def removeEmptyPAnels(pamels):
      newMelem = []
      for melem in pamels:
        if melem.text != "":
          newMelem.append(melem.text)
        else:
          s = ""
      return newMelem

    def checkBolts(elel):
      newElem = []
      for uu in elel:
        if uu == "bolt":
          a = 1
        else:
          newElem.append(uu)
      return newElem
    
    def MatchResbreakDown(panel):
        
        try:
         matchResHomeLbl = panel[0]
        except:
          matchResHomeLbl = "N/A"
        try:
         matchResHome = panel[1]
        except:
          matchResHome = "N/A"

        try:
         matchResAwayLbl = panel[4]
        except:
          matchResAwayLbl = "N/A"
        try:
         matchResAway = panel[5]
        except:
            matchResAway = "N/A"
        MatchRes= [matchResHomeLbl,matchResAwayLbl,matchResHome, matchResAway]
        return MatchRes
        
    
    def BothTSBreakDown(panel):
        
        try:
         matchYesLbl = panel[0]
        except:
           matchYesLbl = "N/A"

        try:
         matchYesdd = panel[1]
        except:
           matchYesdd = "N/A"
        
        try:
         matchNoLbl = panel[2]
        except:
           matchNoLbl = "N/A"
        
        try:
         matchNodd = panel[3]
        except:
           matchNodd = "N/A"
        
        MatchRes= [matchYesdd, matchNodd]
        return MatchRes
    
    def firstBothTSBreakDown(panel):
        try:
         matchYesLbl = panel[0]
        except:
           matchYesLbl = "N/A"

        try:
         matchYesdd = panel[1]
        except:
           matchYesdd = "N/A"
        
        try:
         matchNoLbl = panel[2]
        except:
           matchNoLbl = "N/A"

        try:
         matchNodd = panel[3]
        except:
           matchNodd = "N/A"
        
        
        MatchRes= [matchYesdd, matchNodd]
        return MatchRes

    def DcBreakDown(panel):
        try:
         DCHomeDrawLbl = panel[0]
        except:
           DCHomeDrawLbl = "N/A"

        try:
         DCHomeDrawdd = panel[1]
        except:
           DCHomeDrawLbl = "N/A"

        try:
         DCAwayDrawLbl = panel[5]
        except:
           DCAwayDrawLbl = "N/A"
        
        try:
         DCAwayDrawdd = panel[4]
        except:
           DCAwayDrawdd = "N/A"

        try:
         DCAwayHomeLbl = panel[6]
        except:
           DCAwayHomeLbl = "N/A"
        
        try:
         DCAwayHomedd = panel[7]
        except:
           DCAwayHomedd = "N/A"
        
        MatchRes= [DCHomeDrawdd, DCAwayDrawdd, DCAwayHomedd]
        return MatchRes
    
    def firstDCBreakDown(panel):

        try:
         DCHomeDrawLbl = panel[0]
        except:
           DCHomeDrawLbl = "N/A"

        try:
         DCHomeDrawdd = panel[1]
        except:
           DCHomeDrawdd = "N/A"

        try:
         DCAwayDrawLbl = panel[5]
        except:
           DCAwayDrawLbl = "N/A"

        try:
          DCAwayDrawdd = panel[4]
        except:
           DCAwayDrawdd = "N/A"
        
        try:
          DCAwayHomeLbl = panel[6]
        except:
           DCAwayHomeLbl = "N/A"
       
        try:
          DCAwayHomedd = panel[7]
        except:
           DCAwayHomedd = "N/A"
        
        
        MatchRes= [DCHomeDrawdd, DCAwayDrawdd, DCAwayHomedd]
        return MatchRes
    
    def firstHalvWin(panel):
        try:
         matchResHomeLbl = panel[0]
        except:
           matchResHomeLbl = "N/A"

        try:
         matchResHome = panel[1]
        except:
           matchResHome = "N/A"

        try:
         matchResAwayLbl = panel[4]
        except:
           matchResAwayLbl = "N/A"
        
        try:
         matchResAway = panel[5]
        except:
           matchResAway = "N/A"
        
        
        MatchRes= [matchResHomeLbl,matchResAwayLbl,matchResHome, matchResAway]
        return MatchRes
       
    def OverUndeBreakdown(panel):
       
      try:
       OverallOverZeroLbl = panel[0]
       OverallOverZerodd = panel[1]
      except:
       OverallOverZeroLbl = "def"
       OverallOverZerodd = "N/A"

      try:
       OverallUnderZerLbl = panel[2]
       OverallUnderZerdd = panel[3]
      except:
       OverallUnderZerLbl = "def"
       OverallUnderZerLbl = "N/A"

      try:
       OverallOverOneLbl = panel[4]
       OverallOverOnedd = panel[5]
      except:
       OverallOverOneLbl = "def"
       OverallOverOnedd = "N/A"

      try:
       OverallUnderOneLbl = panel[6]
       OverallUnderOnedd = panel[7]
      except:
        OverallUnderOneLbl = "def"
        OverallUnderOnedd = "N/A"

      try:
       OverallOverYwoLbl = panel[8]
       OverallOverYwodd = panel[9]
      except:
       OverallOverYwoLbl = "def"
       OverallOverYwodd = "N/A"

      try:
       OverallUnderYwoLbl = panel[10]
       OverallUnderYwodd = panel[11]
      except:
       OverallUnderYwoLbl=  "def"
       OverallUnderYwodd =  "N/A"

      try:
       OverallOverThreLbl = panel[12]
       OverallOverThreodd = panel[13]
      except:
       OverallOverThreLbl = "def"
       OverallOverThreodd = "N/A"

      try:
       OverallUnderThreLbl = panel[14]
       OverallUnderThredd = panel[15]
      except:
       OverallUnderThreLbl = "def"
       OverallUnderThredd = "N/A"
       
      try:
       OverallOverFourLbl = panel[16]
       OverallOverFourodd = panel[17]
      except:
       OverallOverFourLbl = "def"
       OverallOverFourodd = "N/A"

      try:
       OverallUnderFourLbl = panel[18]
       OverallUnderFourdd = panel[19]
      except:
       OverallUnderFourLbl = "def"
       OverallUnderFourdd = "N/A"

      try:
       OverallOverFiveLbl = panel[20]
       OverallOverFiveodd = panel[21]
      except:
       OverallOverFiveLbl = "def"
       OverallOverFiveodd = "N/A"

      try:
       OverallUnderFiveLbl = panel[22]
       OverallUnderFivedd = panel[23]
      except:
       OverallUnderFiveLbl = "def"
       OverallUnderFivedd = "N/A"


      MatchRes= [OverallOverZerodd, OverallOverOnedd, OverallOverYwodd, OverallOverThreodd,OverallOverFourodd,OverallOverFiveodd,OverallUnderZerdd,OverallUnderOnedd,OverallUnderYwodd,OverallUnderThredd,OverallUnderFourdd,OverallUnderFivedd]    
      return MatchRes
    
    def firstAwaOverUnderBreakDown(panel):
       
      try:
       OverallOverZeroLbl = panel[0]
       OverallOverZerodd = panel[1]
      except:
       OverallOverZeroLbl = "def"
       OverallOverZerodd = "N/A"

      try:
        OverallUnderZerLbl = panel[2]
        OverallUnderZerdd = panel[3]
      except:
        OverallUnderZerLbl = "def"
        OverallUnderZerdd = "N/A"

      try:
       OverallOverOneLbl = panel[4]
       OverallOverOnedd = panel[5]
      except:
        OverallOverOneLbl = "def"
        OverallOverOnedd = "N/A"

      try:
       OverallUnderOneLbl = panel[6]
       OverallUnderOnedd = panel[7]
      except:
       OverallUnderOneLbl = "def"
       OverallUnderOnedd = "N/A"

      try:
       OverallOverYwoLbl = panel[8]
       OverallOverYwodd = panel[9]
      except:
       OverallOverYwoLbl = "def"
       OverallOverYwodd = "N/A"

      try:
       OverallUnderYwoLbl = panel[10]
       OverallUnderYwodd = panel[11]
      except:
       OverallUnderYwoLbl = "def"
       OverallUnderYwodd = "N/A"

       
      MatchRes= [OverallOverZerodd, OverallOverOnedd, OverallOverYwodd, OverallUnderZerdd,OverallUnderOnedd,OverallUnderYwodd]
      return MatchRes
    def firstHomOverUnderBreakDown(panel):
       
      try:
       OverallOverZeroLbl = panel[0]
       OverallOverZerodd = panel[1]
      except:
       OverallOverZeroLbl = "def"
       OverallOverZerodd = "N/A"

      try:
        OverallUnderZerLbl = panel[2]
        OverallUnderZerdd = panel[3]
      except:
        OverallUnderZerLbl = "def"
        OverallUnderZerdd = "N/A"

      try:
       OverallOverOneLbl = panel[4]
       OverallOverOnedd = panel[5]
      except:
        OverallOverOneLbl = "def"
        OverallOverOnedd = "N/A"

      try:
       OverallUnderOneLbl = panel[6]
       OverallUnderOnedd = panel[7]
      except:
       OverallUnderOneLbl = "def"
       OverallUnderOnedd = "N/A"

      try:
       OverallOverYwoLbl = panel[8]
       OverallOverYwodd = panel[9]
      except:
       OverallOverYwoLbl = "def"
       OverallOverYwodd = "N/A"
       
      try:
       OverallUnderYwoLbl = panel[10]
       OverallUnderYwodd = panel[11]
      except:
       OverallUnderYwoLbl = "def"
       OverallUnderYwodd = "N/A"


      MatchRes= [OverallOverZerodd, OverallOverOnedd, OverallOverYwodd, OverallUnderZerdd,OverallUnderOnedd,OverallUnderYwodd]

      return MatchRes
    
    def firstOverUnderBreakDown(panel):
       
      try:
       OverallOverZeroLbl = panel[0]
       OverallOverZerodd = panel[1]
      except:
       OverallOverZeroLbl = "def"
       OverallOverZerodd = "N/A"

      try:
        OverallUnderZerLbl = panel[2]
        OverallUnderZerdd = panel[3]
      except:
        OverallUnderZerLbl = "def"
        OverallUnderZerdd = "N/A"

      try:
       OverallOverOneLbl = panel[4]
       OverallOverOnedd = panel[5]
      except:
        OverallOverOneLbl = "def"
        OverallOverOnedd = "N/A"

      try:
       OverallUnderOneLbl = panel[6]
       OverallUnderOnedd = panel[7]
      except:
       OverallUnderOneLbl = "def"
       OverallUnderOnedd = "N/A"

      try:
       OverallOverYwoLbl = panel[8]
       OverallOverYwodd = panel[9]
      except:
       OverallOverYwoLbl = "def"
       OverallOverYwodd = "N/A"
       
      try:
       OverallUnderYwoLbl = panel[10]
       OverallUnderYwodd = panel[11]
      except:
       OverallUnderYwoLbl = "def"
       OverallUnderYwodd = "N/A"


       
      MatchRes= [OverallOverZerodd, OverallOverOnedd, OverallOverYwodd, OverallUnderZerdd,OverallUnderOnedd,OverallUnderYwodd]

      return MatchRes
  
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
    
    def FixOverUnders(t,data,betype,ht,half):
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
            Hcon = int(r[ht])
            Acon = int(r[ht + 1])
            HomFrstHlf = int(r[ht + 2])
            AwaFrstHlf = int(r[ht + 3])
            AwaSecHlf = 0
            HomSecHlf = 0
            if Hcon == HomFrstHlf:
                  HomSecHlf = 0
            else:
                  HomSecHlf = Hcon - HomFrstHlf
              
            if Acon == AwaFrstHlf:
                  AwaSecHlf = 0
            else:
                  AwaSecHlf = Acon - AwaFrstHlf
             
          
            if half == "sec":
             FullScore = HomSecHlf + AwaSecHlf
            if half == "first":
             FullScore = HomFrstHlf + AwaFrstHlf
            if half == "over":
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

    def Bts(t,data,betype,ht,way):
        
       count = 0
       notCount = 0
       arr = ([],[])
       for r in data:
           
             Hcon = int(r[ht])
             Acon = int(r[ht + 1])
             HFirstHalf = int(r[ht + 2])
             AFirstHalf = int(r[ht + 3])
             HomSecHlf = 0
             awaSecHlf = 0
             if Hcon == HFirstHalf:
                HomSecHlf = 0
             else:
                HomSecHlf = Hcon - HFirstHalf

             if Acon == AFirstHalf:
                awaSecHlf = 0
             else:
                awaSecHlf = Acon - AFirstHalf

             if way == "over":            
              if Hcon > 0 and Acon > 0:
                  count = count +1
              else:
                  notCount = notCount+1
             if way == "first":            
              if HFirstHalf > 0 and AFirstHalf > 0:
                  count = count +1
              else:
                  notCount = notCount+1
             if way == "sec":            
              if HomSecHlf > 0 and awaSecHlf > 0:
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

        Acount = 0     
        AcountOv1 = 0
        AcountOv2 = 0
        AcountOv3 = 0
        AcountOv4 = 0
        AcountOv5 = 0
        AcountOv6 = 0

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

        HomeFrstConcedUnder0 = 0
        HomeFrstConcedUnder1 = 0
        HomeFrstConcedUnder2 = 0
        HomeFrstConcedUnder3 = 0
        HomeFrstConcedUnder4 = 0
        HomeFrstConcedUnder5 = 0
        HomeFrstConcedUnder6 = 0

        AwayFrstConcedcount = 0
        AwayFrstConcedcountOv2 = 0
        AwayFrstConcedcountOv3 = 0        
        AwayFrstConcedcountOv4 = 0

        HomeFrstConcedcount = 0
        HomeFrstConcedcountOv2 = 0
        HomeFrstConcedcountOv3 = 0        
        HomeFrstConcedcountOv4 = 0

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

        HomeSecConcedUnder0 = 0     
        HomeSecConcedUnder1 = 0
        HomeSecConcedUnder2 = 0
        HomeSecConcedUnder3 = 0
        HomeSecConcedUnder4 = 0
        HomeSecConcedUnder5 = 0
        HomeSecConcedUnder6 = 0

        

        HomeSecConcedcount = 0     
        HomeSecConcedcountOv1 = 0
        HomeSecConcedcountOv2 = 0
        HomeSecConcedcountOv3 = 0
        HomeSecConcedcountOv4 = 0
        HomeSecConcedcountOv5 = 0
        HomeSecConcedcountOv6 = 0

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
        Aovers = []
        Aunders = []
        FrstHalfAovers = []       
        FrstHalfAunders = []

        FrstHalfHunders = []       
        FrstHalfHovers = []

        Aunder1 = 0
        Aunder2 = 0
        Aunder3 = 0
        Aunder4 = 0
        Aunder5 = 0
        Aunder6 = 0 

        HomeSecunder1 = 0
        HomeSecunder2 = 0
        HomeSecunder3 = 0
        HomeSecunder4 = 0
        HomeSecunder5 = 0
        HomeSecunder6 = 0

        HomeSecOver1 = 0
        HomeSecOver2 = 0
        HomeSecOver3 = 0
        HomeSecOver4 = 0
        HomeSecOver5 = 0
        HomeSecOver6 = 0

        Homefrstunder1 = 0
        Homefrstunder2 = 0
        Homefrstunder3 = 0
        Homefrstunder4 = 0
        Homefrstunder5 = 0
        Homefrstunder6 = 0

        HomefrstOverZ = 0
        HomefrstOver1 = 0
        HomefrstOver2 = 0
        HomefrstOver3 = 0
        HomefrstOver4 = 0
        HomefrstOver5 = 0
        HomefrstOver6 = 0

        SecHalfHovers = []
        SecHalfAovers = []
        SecHalfHUnders = []
        SecHalfAUnders = []

        Concedovers = []
        Concedunders = []

        AwayConcedFirstHovers = []
        HomeConcedFirstHovers = []
        HomeFailConcedFirstHovers = []
        HomeFailConcedSecHovers = []
        AwayConcedSecHovers = []
        AwayConcedSecHunder = []
        AwayConcedFirstHunder = []

        HomeConcedSecHovers = []

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
            
            if HomFrstHlf > 4:
               HomFrstHlf = 4
            if HomSecHlf > 4:
               HomSecHlf = 4
            if Acon > 4:
              Acon = 4
            if Hcon > 4:
              Hcon = 4 
            if AFrstHlf > 4:
              AFrstHlf = 4 
            if ASecHlf > 4:
              ASecHlf = 4 
            match HomFrstHlf:
              case 0:  
                AwayFrstConcedUnder0 = AwayFrstConcedUnder0 + 1     
                #AwayFrstConcedUnder1 = AwayFrstConcedUnder1 + 1
                AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  
             
                Homefrstunder1 = Homefrstunder1 + 1
                Homefrstunder2 = Homefrstunder2 + 1
                Homefrstunder3 = Homefrstunder3 + 1
                Homefrstunder4 = Homefrstunder4 + 1
                Homefrstunder5 = Homefrstunder5 + 1
                Homefrstunder6 = Homefrstunder6 + 1
              case 1:    
                AwayFrstConcedcount = AwayFrstConcedcount + 1
               # AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                #AwayFrstConcedUnder1 = AwayFrstConcedUnder1 + 1
                AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1   

                HomefrstOver1 = HomefrstOver1 + 1
                Homefrstunder2 = Homefrstunder2 + 1
                Homefrstunder3 = Homefrstunder3 + 1
                Homefrstunder4 = Homefrstunder4 + 1
                Homefrstunder5 = Homefrstunder5 + 1
                Homefrstunder6 = Homefrstunder6 + 1
              case 2:    
                AwayFrstConcedcount = AwayFrstConcedcount + 1
                AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                #AwayFrstConcedUnder2 = AwayFrstConcedUnder2 + 1
                AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1

                HomefrstOver1 = HomefrstOver1 + 1
                HomefrstOver2 = HomefrstOver2 + 1
                Homefrstunder3 = Homefrstunder3 + 1
                Homefrstunder4 = Homefrstunder4 + 1
                Homefrstunder5 = Homefrstunder5 + 1
                Homefrstunder6 = Homefrstunder6 + 1

              case 3:  
                AwayFrstConcedcount = AwayFrstConcedcount + 1
                AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                AwayFrstConcedcountOv3 = AwayFrstConcedcountOv3 + 1
                #AwayFrstConcedUnder3 = AwayFrstConcedUnder3 + 1
                AwayFrstConcedUnder4 = AwayFrstConcedUnder4 + 1
                AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1 

                HomefrstOver1 = HomefrstOver1 + 1
                HomefrstOver2 = HomefrstOver2 + 1
                HomefrstOver3 = HomefrstOver3 + 1
                HomefrstOver4 = HomefrstOver4 + 1
                HomefrstOver5 = HomefrstOver5 + 1
                HomefrstOver6 = HomefrstOver6 + 1

                Homefrstunder4 = Homefrstunder4 + 1
                Homefrstunder5 = Homefrstunder5 + 1
                Homefrstunder6 = Homefrstunder6 + 1
              case 4:                 
                 AwayFrstConcedcount = AwayFrstConcedcount + 1
                 AwayFrstConcedcountOv2 = AwayFrstConcedcountOv2 + 1
                 AwayFrstConcedcountOv3 = AwayFrstConcedcountOv3 + 1
                 AwayFrstConcedcountOv4 = AwayFrstConcedcountOv4 + 1
                 AwayFrstConcedUnder5 = AwayFrstConcedUnder5 + 1
                 AwayFrstConcedUnder6 = AwayFrstConcedUnder6 + 1  
                 
                 HomefrstOver1 = HomefrstOver1 + 1
                 HomefrstOver2 = HomefrstOver2 + 1 
                 HomefrstOver3 = HomefrstOver3 + 1
                 HomefrstOver4 = HomefrstOver4 + 1
                 HomefrstOver5 = HomefrstOver5 + 1
                 HomefrstOver6 = HomefrstOver6 + 1  
                 Homefrstunder5 = Homefrstunder5 + 1
                 Homefrstunder6 = Homefrstunder6 + 1 
            match HomSecHlf:
              case 0:  
                AwaySecConcedUnder0 = AwaySecConcedUnder0 + 1     
                AwaySecConcedUnder1 = AwaySecConcedUnder1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1  
             
                HomeSecunder1 = HomeSecunder1 + 1
                HomeSecunder2 = HomeSecunder2 + 1
                HomeSecunder3 = HomeSecunder3 + 1
                HomeSecunder4 = HomeSecunder4 + 1
                HomeSecunder5 = HomeSecunder5 + 1
                HomeSecunder6 = HomeSecunder6 + 1 

               
                
               
                 
              case 1:    
                AwaySecConcedcount = AwaySecConcedcount + 1
                AwaySecConcedUnder1 = AwaySecConcedUnder1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1 

                HomeSecOver1 = HomeSecOver1 + 1
                HomeSecunder2 = HomeSecunder2 + 1
                HomeSecunder3 = HomeSecunder3 + 1
                HomeSecunder4 = HomeSecunder4 + 1
                HomeSecunder5 = HomeSecunder5 + 1
                HomeSecunder6 = HomeSecunder6 + 1 
              case 2:  
                AwaySecConcedcount = AwaySecConcedcount + 1  
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedUnder2 = AwaySecConcedUnder2 + 1
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1

                HomeSecOver1 = HomeSecOver1 + 1
                HomeSecOver2 = HomeSecOver2 + 1
                HomeSecunder3 = HomeSecunder3 + 1
                HomeSecunder4 = HomeSecunder4 + 1
                HomeSecunder5 = HomeSecunder5 + 1
                HomeSecunder6 = HomeSecunder6 + 1 

              case 3:  
                AwaySecConcedcount = AwaySecConcedcount + 1
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedcountOv2 = AwaySecConcedcountOv2 + 1               
                AwaySecConcedUnder3 = AwaySecConcedUnder3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1


                HomeSecOver1 = HomeSecOver1 + 1
                HomeSecOver2 = HomeSecOver2 + 1
                HomeSecOver3 = HomeSecOver3 + 1
                
                HomeSecunder4 = HomeSecunder4 + 1
                HomeSecunder5 = HomeSecunder5 + 1
                HomeSecunder6 = HomeSecunder6 + 1 
              case 4:  
                AwaySecConcedcount = AwaySecConcedcount + 1               
                AwaySecConcedcountOv1 = AwaySecConcedcountOv1 + 1
                AwaySecConcedcountOv2 = AwaySecConcedcountOv2 + 1               
                AwaySecConcedcountOv3 = AwaySecConcedcountOv3 + 1
                AwaySecConcedUnder4 = AwaySecConcedUnder4 + 1
                AwaySecConcedUnder5 = AwaySecConcedUnder5 + 1
                AwaySecConcedUnder6 = AwaySecConcedUnder6 + 1

                HomeSecOver1 = HomeSecOver1 + 1
                HomeSecOver2 = HomeSecOver2 + 1
                HomeSecOver3 = HomeSecOver3 + 1
                HomeSecOver4 = HomeSecOver4 + 1
                HomeSecunder5 = HomeSecunder5 + 1
                HomeSecunder6 = HomeSecunder6 + 1 

            match Acon:
              case 0:                 
               Aunder1 = Aunder1 + 1
               Aunder2 = Aunder2 + 1
               Aunder3 = Aunder3 + 1
               Aunder4 = Aunder4 + 1
               Aunder5 = Aunder5 + 1
               Aunder6 = Aunder6 + 1  
              case 1:    
                Acount = Acount + 1
                Aunder2 = Aunder2 + 1
                Aunder3 = Aunder3 + 1
                Aunder4 = Aunder4 + 1
                Aunder5 = Aunder5 + 1
                Aunder6 = Aunder6 + 1
              case 2:    
               Acount = Acount + 1
               AcountOv1 = AcountOv1 +1
                    
               Aunder3 = Aunder3 + 1
               Aunder4 = Aunder4 + 1
               Aunder5 = Aunder5 + 1
               Aunder6 = Aunder6 + 1
              case 3:                 
               Acount = Acount + 1
               AcountOv1 = AcountOv1 +1
               AcountOv2 = AcountOv2 +1
               Aunder4 = Aunder4 + 1
               Aunder5 = Aunder5 + 1
               Aunder6 = Aunder6 + 1
              case 4:                 
                Acount = Acount + 1
                AcountOv1 = AcountOv1 +1
                AcountOv2 = AcountOv2 +1
                AcountOv3 = AcountOv3 +1
                Aunder5 = Aunder5 + 1
                Aunder6 = Aunder6 + 1
              case 5:                 
                Acount = Acount + 1
                AcountOv1 = AcountOv1 +1
                AcountOv2 = AcountOv2 +1
                AcountOv3 = AcountOv3 +1
                AcountOv4 = AcountOv4 +1
               
                Aunder6 = Aunder6 + 1
              case 6:                 
                Acount = Acount + 1
                AcountOv1 = AcountOv1 +1
                AcountOv2 = AcountOv2 +1
                AcountOv3 = AcountOv3 +1
                AcountOv4 = AcountOv4 +1
                AcountOv5 = AcountOv5 +1
                Aunder6 = Aunder6 + 1
            match Hcon:
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

               HomeFrstConcedUnder0 = HomeFrstConcedUnder0 + 1     
               #AwayFrstConcedUnder1 = AwayFrstConcedUnder1 + 1
               HomeFrstConcedUnder2 = HomeFrstConcedUnder2 + 1
               HomeFrstConcedUnder3 = HomeFrstConcedUnder3 + 1
               HomeFrstConcedUnder4 = HomeFrstConcedUnder4 + 1
               HomeFrstConcedUnder5 = HomeFrstConcedUnder5 + 1
               HomeFrstConcedUnder6 = HomeFrstConcedUnder6 + 1  
             
              case 1:    
                FrstAOver = FrstAOver + 1
                Frstunder1 = Frstunder1 + 1
                Frstunder2 = Frstunder2 + 1

                HomeFrstConcedcount = HomeFrstConcedcount + 1
                HomeFrstConcedUnder2 = HomeFrstConcedUnder2 + 1
                HomeFrstConcedUnder3 = HomeFrstConcedUnder3 + 1
                HomeFrstConcedUnder4 = HomeFrstConcedUnder4 + 1
                HomeFrstConcedUnder5 = HomeFrstConcedUnder5 + 1
                HomeFrstConcedUnder6 = HomeFrstConcedUnder6 + 1 
              case 2:    
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               Frstunder2 = Frstunder2 + 1

               HomeFrstConcedcount = HomeFrstConcedcount + 1
               HomeFrstConcedcountOv2 = HomeFrstConcedcountOv2 + 1
               HomeFrstConcedUnder3 = HomeFrstConcedUnder3 + 1
               HomeFrstConcedUnder4 = HomeFrstConcedUnder4 + 1
               HomeFrstConcedUnder5 = HomeFrstConcedUnder5 + 1
               HomeFrstConcedUnder6 = HomeFrstConcedUnder6 + 1 

              case 3:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1

               HomeFrstConcedcount = HomeFrstConcedcount + 1
               HomeFrstConcedcountOv2 = HomeFrstConcedcountOv2 + 1
               HomeFrstConcedcountOv3 = HomeFrstConcedcountOv3 + 1
               HomeFrstConcedUnder4 = HomeFrstConcedUnder4 + 1
               HomeFrstConcedUnder5 = HomeFrstConcedUnder5 + 1
               HomeFrstConcedUnder6 = HomeFrstConcedUnder6 + 1
              case 4:                 
               FrstAOver = FrstAOver + 1
               FrstAOver1 = FrstAOver1 + 1
               FrstAOver2 = FrstAOver2 + 1

               HomeFrstConcedcount = HomeFrstConcedcount + 1
               HomeFrstConcedcountOv2 = HomeFrstConcedcountOv2 + 1
               HomeFrstConcedcountOv3 = HomeFrstConcedcountOv3 + 1
               HomeFrstConcedcountOv4 = HomeFrstConcedcountOv4 + 1
               HomeFrstConcedUnder5 = HomeFrstConcedUnder5 + 1
               HomeFrstConcedUnder6 = HomeFrstConcedUnder6 + 1
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
             
                    
               #HomeSecConcedUnder1 = HomeSecConcedUnder1 + 1
               HomeSecConcedUnder0 = HomeSecConcedUnder0 + 1
               HomeSecConcedUnder2 = HomeSecConcedUnder2 + 1
               HomeSecConcedUnder3 = HomeSecConcedUnder3 + 1
               HomeSecConcedUnder4 = HomeSecConcedUnder4 + 1
               HomeSecConcedUnder5 = HomeSecConcedUnder5 + 1
               HomeSecConcedUnder6 = HomeSecConcedUnder6 + 1  
              case 1:    
                ASecOver0 = ASecOver0 + 1
                ASecunder1 = ASecunder1 + 1
                ASecunder2 = ASecunder2 + 1


                HomeSecConcedcount = HomeSecConcedcount + 1 
                HomeSecConcedUnder2 = HomeSecConcedUnder2 + 1
                HomeSecConcedUnder3 = HomeSecConcedUnder3 + 1
                HomeSecConcedUnder4 = HomeSecConcedUnder4 + 1
                HomeSecConcedUnder5 = HomeSecConcedUnder5 + 1
                HomeSecConcedUnder6 = HomeSecConcedUnder6 + 1  
              case 2:    
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecunder2 = ASecunder2 + 1

               HomeSecConcedcount = HomeSecConcedcount + 1               
               HomeSecConcedcountOv2 = HomeSecConcedcountOv2 + 1
               HomeSecConcedUnder3 = HomeSecConcedUnder3 + 1
               HomeSecConcedUnder4 = HomeSecConcedUnder4 + 1
               HomeSecConcedUnder5 = HomeSecConcedUnder5 + 1
               HomeSecConcedUnder6 = HomeSecConcedUnder6 + 1 

              case 3:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1

               HomeSecConcedcount = HomeSecConcedcount + 1               
               
               HomeSecConcedcountOv2 = HomeSecConcedcountOv2 + 1 
               HomeSecConcedcountOv3 = HomeSecConcedcountOv3 + 1 

               HomeSecConcedUnder4 = HomeSecConcedUnder4 + 1
               HomeSecConcedUnder5 = HomeSecConcedUnder5 + 1
               HomeSecConcedUnder6 = HomeSecConcedUnder6 + 1 
              case 4:                 
               ASecOver0 = ASecOver0 + 1
               ASecOver1 = ASecOver1 + 1
               ASecOver2 = ASecOver2 + 1

               HomeSecConcedcount = HomeSecConcedcount + 1               
               
               HomeSecConcedcountOv2 = HomeSecConcedcountOv2 + 1               
               HomeSecConcedcountOv3 = HomeSecConcedcountOv3 + 1
               HomeSecConcedcountOv4 = HomeSecConcedcountOv4 + 1
               HomeSecConcedUnder5 = HomeSecConcedUnder5 + 1
               HomeSecConcedUnder6 = HomeSecConcedUnder6 + 1
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

        Aovers.append(Acount)
        Aovers.append(AcountOv1)
        Aovers.append(AcountOv2)
        Aovers.append(AcountOv3)
        Aovers.append(AcountOv4)

        Aunders.append(Aunder1)
        Aunders.append(Aunder2)
        Aunders.append(Aunder3)
        Aunders.append(Aunder4)
        Aunders.append(Aunder5)
       

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

                
        FrstHalfHovers.append(HomefrstOver1)        
        FrstHalfHovers.append(HomefrstOver2)        
        FrstHalfHovers.append(HomefrstOver3)    
        FrstHalfHovers.append(HomefrstOver4)    
        
        FrstHalfHunders.append(Homefrstunder1)        
        FrstHalfHunders.append(Homefrstunder2)        
        FrstHalfHunders.append(Homefrstunder3) 
        FrstHalfHunders.append(Homefrstunder4) 

        HomeConcedSecHovers.append(HomeSecConcedcount)
        HomeConcedSecHovers.append(HomeSecConcedcountOv2)
        HomeConcedSecHovers.append(HomeSecConcedcountOv3)
        HomeConcedSecHovers.append(HomeSecConcedcountOv4)


        HomeConcedFirstHovers.append(HomeFrstConcedcount)
        HomeConcedFirstHovers.append(HomeFrstConcedcountOv2)
        HomeConcedFirstHovers.append(HomeFrstConcedcountOv3)
        HomeConcedFirstHovers.append(HomeFrstConcedcountOv4)

        HomeFailConcedFirstHovers.append(HomeFrstConcedUnder0)
        HomeFailConcedFirstHovers.append(HomeFrstConcedUnder2)
        HomeFailConcedFirstHovers.append(HomeFrstConcedUnder3)
        HomeFailConcedFirstHovers.append(HomeFrstConcedUnder4)

        HomeFailConcedSecHovers.append(HomeSecConcedUnder0)
        HomeFailConcedSecHovers.append(HomeSecConcedUnder2)
        HomeFailConcedSecHovers.append(HomeSecConcedUnder3)
        HomeFailConcedSecHovers.append(HomeSecConcedUnder4)
     
        SecHalfAovers.append(ASecOver0)        
        SecHalfAovers.append(ASecOver1)        
        SecHalfAovers.append(ASecOver2)  

        SecHalfHovers.append(HomeSecOver1)        
        SecHalfHovers.append(HomeSecOver2)        
        SecHalfHovers.append(HomeSecOver3) 
        SecHalfHovers.append(HomeSecOver4)

        SecHalfHUnders.append(HomeSecunder1)        
        SecHalfHUnders.append(HomeSecunder2)        
        SecHalfHUnders.append(HomeSecunder3) 
        SecHalfHUnders.append(HomeSecunder4)  

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
        
       
                #0      #1        #2              #3            #4            #5                #6                  #7                    #8                      #9                     #10                       #11                  #12                     #13            #14          #15             #16             #17       #18      #19                                                                                       
        arr = ([overs,unders,FrstHalfAovers,FrstHalfAunders,SecHalfAovers,SecHalfAUnders,AwayConcedSecHovers,AwayConcedFirstHovers,AwayConcedSecHunder,AwayConcedFirstHunder,HomeFailConcedFirstHovers,HomeConcedFirstHovers,HomeFailConcedSecHovers,HomeConcedSecHovers,SecHalfHovers,SecHalfHUnders,FrstHalfHunders,FrstHalfHovers,Aovers,Aunders])
        return arr
    
    
    def ConcededWholeSeaon(t,data,betype,ht):
        count = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        Notcount = 0
        Notcount2 = 0
        Notcount3 = 0
        Notcount4 = 0
        Notcount5 = 0
        
        highestMatch = 0
           
        
        for r in data:
            r = int(r[ht]) 
            match r:
              case 0:
                Notcount = Notcount + 1                
                Notcount2 = Notcount2 + 1
                Notcount3 = Notcount3 + 1
                Notcount4 = Notcount4 + 1
                Notcount5 = Notcount5 + 1
              case 1:
                count = count + 1                
                Notcount2 = Notcount2 + 1
                Notcount3 = Notcount3 + 1
                Notcount4 = Notcount4 + 1
                Notcount5 = Notcount5 + 1
              case 2:
                count = count + 1
                count2 = count2 + 1
                Notcount3 = Notcount3 + 1
                Notcount4 = Notcount4 + 1
                Notcount5 = Notcount5 + 1
              case 3:
                count = count + 1
                count2 = count2 + 1
                count3 = count3 + 1            
                Notcount4 = Notcount4 + 1
                Notcount5 = Notcount5 + 1
              case 4:
                count = count + 1
                count2 = count2 + 1
                count3 = count3 + 1            
                count4 = count4 + 1                            
                Notcount5 = Notcount5 + 1
              case 5:
                count = count + 1
                count2 = count2 + 1
                count3 = count3 + 1            
                count4 = count4 + 1                            
                count5 = count5 + 1


        arr = [count,Notcount,count2,Notcount2,count3,Notcount3,count4,Notcount4,count5,Notcount5]       
        return arr

    def MatchRes(t,data,betype,ht):
      HomeWinCount = 0
      AwayWinCount = 0
      HomeFailToWin = 0
      AwayFailTowin = 0
      HomeLose = 0

      HomeFlvWinCount = 0
      AwayFlvWinCount = 0
      HomeFlvLose = 0
      AwayFlvFailToLose = 0
      AwayFlvFailTowin = 0
      HomeFailToLose = 0
      HomeFlvFailToLose = 0
      HomeSecFailToLose = 0
      AwaySecFailToLose = 0

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
             Acon = int(r[ht + 1])
             AFrstHlf = int(r[ht + 3])
             AwSecHlf = Acon - AFrstHlf
        else:
             Hcon = int(r[ht - 1])
             HomFrstHlf = int(r[ht +1])
             HomeSecHlf = Hcon - HomFrstHlf
             Acon = int(r[ht])
             AFrstHlf = int(r[ht + 2])
             AwSecHlf = Acon - AFrstHlf

        if Hcon > Acon:
           HomeWinCount = HomeWinCount + 1
           AwayFailTowin = AwayFailTowin + 1
           HomeFailToLose= HomeFailToLose + 1
        if Acon > Hcon:
           AwayWinCount = AwayWinCount + 1
           HomeFailToWin = HomeFailToWin + 1
           HomeLose = HomeLose + 1
           
        if Hcon == Acon:
           AwayFailTowin = AwayFailTowin + 1
           HomeFailToWin = HomeFailToWin + 1
           HomeFailToLose= HomeFailToLose + 1
      
        if HomFrstHlf > AFrstHlf:
           HomeFlvWinCount = HomeFlvWinCount + 1
           AwayFlvFailTowin = AwayFlvFailTowin + 1
           HomeFlvFailToLose = HomeFlvFailToLose + 1  

        if AFrstHlf > HomFrstHlf:
           AwayFlvWinCount = AwayFlvWinCount + 1
           HomeFlvLose = HomeFlvLose + 1
           AwayFlvFailToLose = AwayFlvFailToLose + 1
           
        if HomFrstHlf == AFrstHlf:
           AwayFlvFailTowin = AwayFlvFailTowin + 1
           HomeFlvFailToLose = HomeFlvFailToLose + 1
           AwayFlvFailToLose = AwayFlvFailToLose + 1


        if HomeSecHlf > AwSecHlf:
           HomeSecFlvWinCount = HomeSecFlvWinCount + 1
           AwaySecFlvFailTowin = AwaySecFlvFailTowin + 1
           HomeSecFailToLose = HomeSecFailToLose + 1
        if AwSecHlf > HomeSecHlf:
           AwaySecFlvWinCount = AwaySecFlvWinCount + 1
           HomeSecFlvFailToWin = HomeSecFlvFailToWin + 1
           AwaySecFailToLose = AwaySecFailToLose + 1 
        if HomeSecHlf == AwSecHlf:
           #AwaySecFlvFailTowin = AwaySecFlvFailTowin + 1
           #HomeSecFlvFailToWin = HomeSecFlvFailToWin + 1 
           HomeSecFailToLose = HomeSecFailToLose + 1 
           AwaySecFailToLose = AwaySecFailToLose + 1 


                #1            #2            #3            #4          #5                #6                  #7            #8            #9                 #10               #11                 #12              #13                 #14              #15            #16        #17              #18
      arr = ([HomeWinCount,AwayFailTowin,AwayWinCount,HomeFailToWin,HomeFlvWinCount,AwayFlvFailTowin,AwayFlvWinCount,HomeFlvLose,HomeFlvFailToLose,HomeSecFailToLose,HomeSecFlvWinCount,AwaySecFlvFailTowin,AwaySecFlvWinCount,HomeSecFlvFailToWin,HomeFailToLose,HomeLose,AwayFlvFailToLose,AwaySecFailToLose])  
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

    def checkDataBase(conn,eventName,tableName):
        #conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
        cursor = conn.cursor()

        insert_st = "SELECT * FROM "+ tableName+" where HTeam = ? AND ATeam = ?"
        #insert_stmt2 = "select * from EplBetOdds where HTeam = " + eventName.split(" ")[0] +" and ATeam = " + eventName.split(" ")[2]
        #insert_stmt2 = "select * from EPL UNION select * from belgiumJPL union select * from EngLeagua1 union select * from EngLeagua2 union select * from SeriaB union select * from EplChampionShip23"
        newEvent = eventName.split(" v ")
        data = (newEvent[0].strip(),newEvent[1].strip())
        #cursor.execute(insert_stmt2)
        cursor.execute(insert_st,data)
        sql_data = pd.DataFrame(cursor.fetchall())
        return sql_data

                
                    