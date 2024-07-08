class SlPA:
 
 def ConceedHomeXNumOutcomeAwayOverUnder(t,data,betype,ht):
      Ucount = 0
      count = 0
      for r in data:
         c =  int(r[ht - 1])  
         v = int(r[ht])  
 def FirstHalfWinSecHalfOut(t,data,betype,ht): 
    homeSecWin = 0
    homeSecWindraw = 0
    awaySecWindraw = 0
    awaySecWin = 0
    countovr1 = 0
    countovr2 = 0
    countovr3 = 0
    countovr4 = 0
    underovr1 = 0
    underovr2 = 0
    underovr3 = 0
    underovr4 = 0
    Ucount = 0
    count = 0

    Hcountovr1 = 0
    Hcountovr2 = 0
    Hcountovr3 = 0
    Hcountovr4 = 0
    Hunderovr1 = 0
    Hunderovr2 = 0
    Hunderovr3 = 0
    Hunderovr4 = 0
    HUcount = 0
    Hcount = 0
    for r in data:
         
         c =  int(r[ht - 1])  
         v = int(r[ht])  
         secH  =  int(r[ht -3]) - int(r[ht - 1]) 
         secA  =   int(r[ht - 2]) - int(r[ht ])
         FullH  =  int(r[ht -3]) 
         FullA  =   int(r[ht -2]) 
         if v > c:
             if FullH > FullA:
                homeSecWin = homeSecWin + 1
                homeSecWindraw = homeSecWindraw + 1
             if FullH == FullA:
                 homeSecWindraw = homeSecWindraw + 1
                 awaySecWindraw = awaySecWindraw+1
             if FullA > FullH:
                awaySecWin = awaySecWin + 1
                awaySecWindraw = awaySecWindraw+1
             if secH > c:
                count = count + 1
             else:
                 Ucount = Ucount + 1
             match secA:
                case 0:
                  underovr1 = underovr1 + 1
                  underovr2 = underovr2 + 1
                  underovr3 = underovr3 + 1
                  underovr4 = underovr4 + 1 
                case 1:
                  countovr1 = countovr1 + 1
                  underovr2 = underovr2 + 1
                  underovr3 = underovr3 + 1
                  underovr4 = underovr4 + 1 
                case 2:
                  countovr1 = countovr1 + 1
                  countovr2 = countovr2 + 1
                  underovr3 = underovr3 + 1
                  underovr4 = underovr4 + 1 
                case 3:
                  countovr1 = countovr1 + 1
                  countovr2 = countovr2 + 1
                  countovr3 = countovr3 + 1
                  underovr4 = underovr4 + 1 
                case 4:
                  countovr1 = countovr1 + 1
                  countovr2 = countovr2 + 1
                  countovr3 = countovr3 + 1
                  countovr4 = countovr4 + 1
             match secH:
                case 0:
                  Hunderovr1 = Hunderovr1 + 1
                  Hunderovr2 = Hunderovr2 + 1
                  Hunderovr3 = Hunderovr3 + 1
                  Hunderovr4 = Hunderovr4 + 1 
                case 1:
                  Hcountovr1 = Hcountovr1 + 1
                  Hunderovr2 = Hunderovr2 + 1
                  Hunderovr3 = Hunderovr3 + 1
                  Hunderovr4 = Hunderovr4 + 1 
                case 2:
                  Hcountovr1 = Hcountovr1 + 1
                  Hcountovr2 = Hcountovr2 + 1
                  Hunderovr3 = Hunderovr3 + 1
                  Hunderovr4 = Hunderovr4 + 1 
                case 3:
                  Hcountovr1 = Hcountovr1 + 1
                  Hcountovr2 = Hcountovr2 + 1
                  Hcountovr3 = Hcountovr3 + 1
                  Hunderovr4 = Hunderovr4 + 1
                case 4:
                  Hcountovr1 = Hcountovr1 + 1
                  Hcountovr2 = Hcountovr2 + 1
                  Hcountovr3 = Hcountovr3 + 1
                  Hcountovr4 = Hcountovr4 + 1   
    arr = [homeSecWin,awaySecWin,homeSecWindraw,awaySecWindraw,count,Ucount,countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,Hcountovr1,Hunderovr1,Hcountovr2,Hunderovr2,Hcountovr3,Hunderovr3,Hcountovr4,Hunderovr4]
    return arr

 def HaltimeFultimeActionOutputOverUnder(t,data,betype,ht): 
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

        Ccount = 0
        Ccount2 = 0
        Ccount3 = 0
        Ccount4 = 0
        Ccount5 = 0
        CNotcount = 0
        CNotcount2 = 0
        CNotcount3 = 0
        CNotcount4 = 0
        CNotcount5 = 0

        CCcount = 0
        CCcount2 = 0
        CCcount3 = 0
        CCcount4 = 0
        CCcount5 = 0
        CCNotcount = 0
        CCNotcount2 = 0
        CCNotcount3 = 0
        CCNotcount4 = 0
        CCNotcount5 = 0

        CCCcount = 0
        CCCcount2 = 0
        CCCcount3 = 0
        CCCcount4 = 0
        CCCcount5 = 0
        CCCNotcount = 0
        CCCNotcount2 = 0
        CCCNotcount3 = 0
        CCCNotcount4 = 0
        CCCNotcount5 = 0

        CCCCcount = 0
        CCCCcount2 = 0
        CCCCcount3 = 0
        CCCCcount4 = 0
        CCCCcount5 = 0
        CCCCNotcount = 0
        CCCCNotcount2 = 0
        CCCCNotcount3 = 0
        CCCCNotcount4 = 0
        CCCCNotcount5 = 0
        
        highestMatch = 0
           
        
        for r in data:
         
            c = int(r[ht])  + int(r[ht - 1])   
            
            secH  =  int(r[ht -3]) - int(r[ht - 1]) 
            secA  =   int(r[ht - 2]) - int(r[ht ])

            v = secH + secA
            #v = int(r[ht]) 
            if v > 4:
               v == 4
            match  c:
              case 0:
                match v:
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
              case 1:
                match v:
                 case 0:
                     CNotcount = CNotcount + 1                
                     CNotcount2 = CNotcount2 + 1
                     CNotcount3 = CNotcount3 + 1
                     CNotcount4 = CNotcount4 + 1
                     CNotcount5 = CNotcount5 + 1
                 case 1:
                    Ccount = Ccount + 1 
                    CNotcount2 = CNotcount2 + 1
                    CNotcount3 = CNotcount3 + 1
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1
                 case 2:
                    Ccount = Ccount + 1 
                    Ccount2 = Ccount2 + 1
                    CNotcount3 = CNotcount3 + 1
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1
                 case 3:
                    Ccount = Ccount + 1 
                    Ccount2 = Ccount2 + 1
                    Ccount3 = Ccount3 + 1   
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1 
                 case 4:
                     Ccount = Ccount + 1
                     Ccount2 = Ccount2 + 1
                     Ccount3 = Ccount3 + 1            
                     Ccount4 = Ccount4 + 1                            
                     CNotcount5 = CNotcount5 + 1 
              case 2:
                match v:
                 case 0:
                     CCNotcount = CCNotcount + 1                
                     CCNotcount2 = CCNotcount2 + 1
                     CCNotcount3 = CCNotcount3 + 1
                     CCNotcount4 = CCNotcount4 + 1
                     CCNotcount5 = CCNotcount5 + 1
                 case 1:
                    CCcount = CCcount + 1 
                    CCNotcount2 = CCNotcount2 + 1
                    CCNotcount3 = CCNotcount3 + 1
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1
                 case 2:
                    CCcount = CCcount + 1 
                    CCcount2 = CCcount2 + 1
                    CCNotcount3 = CCNotcount3 + 1
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1
                 case 3:
                    CCcount = CCcount + 1 
                    CCcount2 = CCcount2 + 1
                    CCcount3 = CCcount3 + 1   
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1 
                 case 4:
                     CCcount = CCcount + 1
                     CCcount2 = CCcount2 + 1
                     CCcount3 = CCcount3 + 1            
                     CCcount4 = CCcount4 + 1                            
                     CCNotcount5 = CCNotcount5 + 1 
              case 3:
                match v:
                 case 0:
                     CCCNotcount = CCCNotcount + 1                
                     CCCNotcount2 = CCCNotcount2 + 1
                     CCCNotcount3 = CCCNotcount3 + 1
                     CCCNotcount4 = CCCNotcount4 + 1
                     CCCNotcount5 = CCCNotcount5 + 1
                 case 1:
                     CCCcount = CCCcount + 1 
                     CCCNotcount2 = CCCNotcount2 + 1
                     CCCNotcount3 = CCCNotcount3 + 1
                     CCCNotcount4 = CCCNotcount4 + 1
                     CCCNotcount5 = CCCNotcount5 + 1
                 case 2:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCNotcount3 = CCCNotcount3 + 1
                    CCCNotcount4 = CCCNotcount4 + 1
                    CCCNotcount5 = CCCNotcount5 + 1
                 case 3:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCcount3 = CCCcount3 + 1   
                    CCCNotcount4 = CCCNotcount4 + 1
                    CCCNotcount5 = CCCNotcount5 + 1
                 case 4:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCcount3 = CCCcount3 + 1            
                    CCCcount4 = CCCcount4 + 1                            
                    CCCNotcount5 = CCCNotcount5 + 1
              case 4:
                match v:
                 case 0:
                     CCCCNotcount = CCCCNotcount + 1                
                     CCCCNotcount2 = CCCCNotcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 1:
                     CCCCcount = CCCCcount + 1 
                     CCCCNotcount2 = CCCCNotcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 2:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 3:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCcount3 = CCCCcount3 + 1   
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 4:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCcount3 = CCCCcount3 + 1              
                     CCCCcount4 = CCCCcount4 + 1                            
                     CCCCNotcount5 = CCCCNotcount5 + 1
              

                 #1    #2     #3        #4       #5       #6         #7      #8            #9           #10     #11     #12     #13       #14      #15         #16       #17         #18       #19             #20       #21    #22      #23      #24        #25        #26       #27        #28         #29          #30         #31    #32      #33       #34       #35       #36        #37        #38          #39          #40                                                      
        arr = [count,Ccount,CCcount,CCCcount,CCCCcount,Notcount,CNotcount,CCNotcount,CCCNotcount,CCCCNotcount,count2,Ccount2,CCcount2,CCCcount2,CCCCcount2,Notcount2,CNotcount2,CCNotcount2,CCCNotcount2,CCCCNotcount2,count3,Ccount3,CCcount3,CCCcount3,CCCCcount3,Notcount3,CNotcount3,CCNotcount3,CCCNotcount3,CCCCNotcount3,count4,Ccount4,CCcount4,CCCcount4,CCCCcount4,Notcount4,CNotcount4,CCNotcount4,CCCNotcount4,CCCCNotcount4]       
        return arr
 
 def ScoreFirstHConceedSecondLayerPerceptron(t,data,betype,ht):
        count = 0
      
        Notcount = 0

        for r in data:
            c =  int(r[ht - 3])
            v = int(r[ht]) 
            if v > 0:
               if c > 0:
                  count = count + 1
               else:
                  Notcount = Notcount + 1
              
                
        arr = [count,Notcount]       
        return arr
 def HaltimeFultimeActionOutput(t,data,betype,ht):
        count = 0
      
        Notcount = 0

        for r in data:
            c =  int(r[ht - 1])
            v = int(r[ht]) 
            d =  int(r[ht - 3]) - int(r[ht - 1])
            f = int(r[ht - 2]) - int(r[ht]) 
            if v > 0 or c > 0 :
               if d > 0 or f > 0:
                  count = count + 1
               else:
                  Notcount = Notcount + 1
              
                
        arr = [count,Notcount]       
        return arr
 
 def ConceedSecondLayerPerceptron(t,data,betype,ht):
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

        Ccount = 0
        Ccount2 = 0
        Ccount3 = 0
        Ccount4 = 0
        Ccount5 = 0
        CNotcount = 0
        CNotcount2 = 0
        CNotcount3 = 0
        CNotcount4 = 0
        CNotcount5 = 0

        CCcount = 0
        CCcount2 = 0
        CCcount3 = 0
        CCcount4 = 0
        CCcount5 = 0
        CCNotcount = 0
        CCNotcount2 = 0
        CCNotcount3 = 0
        CCNotcount4 = 0
        CCNotcount5 = 0

        CCCcount = 0
        CCCcount2 = 0
        CCCcount3 = 0
        CCCcount4 = 0
        CCCcount5 = 0
        CCCNotcount = 0
        CCCNotcount2 = 0
        CCCNotcount3 = 0
        CCCNotcount4 = 0
        CCCNotcount5 = 0

        CCCCcount = 0
        CCCCcount2 = 0
        CCCCcount3 = 0
        CCCCcount4 = 0
        CCCCcount5 = 0
        CCCCNotcount = 0
        CCCCNotcount2 = 0
        CCCCNotcount3 = 0
        CCCCNotcount4 = 0
        CCCCNotcount5 = 0
        
        highestMatch = 0
           
        
        for r in data:
          if betype == "k":
            c = int(r[ht])  - int(r[ht + 2])   
            v = int(r[ht + 2]) 
          if betype == "b":
            c = int(r[ht -3]) - int(r[ht - 1]) 
            v = int(r[ht]) 
            match  v:
              case 0:
                match c:
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
              case 1:
                match c:
                 case 0:
                     CNotcount = CNotcount + 1                
                     CNotcount2 = CNotcount2 + 1
                     CNotcount3 = CNotcount3 + 1
                     CNotcount4 = CNotcount4 + 1
                     CNotcount5 = CNotcount5 + 1
                 case 1:
                    Ccount = Ccount + 1 
                    CNotcount2 = CNotcount2 + 1
                    CNotcount3 = CNotcount3 + 1
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1
                 case 2:
                    Ccount = Ccount + 1 
                    Ccount2 = Ccount2 + 1
                    CNotcount3 = CNotcount3 + 1
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1
                 case 3:
                    Ccount = Ccount + 1 
                    Ccount2 = Ccount2 + 1
                    Ccount3 = Ccount3 + 1   
                    CNotcount4 = CNotcount4 + 1
                    CNotcount5 = CNotcount5 + 1 
                 case 4:
                     Ccount = Ccount + 1
                     Ccount2 = Ccount2 + 1
                     Ccount3 = Ccount3 + 1            
                     Ccount4 = Ccount4 + 1                            
                     CNotcount5 = CNotcount5 + 1 
              case 2:
                match c:
                 case 0:
                     CCNotcount = CCNotcount + 1                
                     CCNotcount2 = CCNotcount2 + 1
                     CCNotcount3 = CCNotcount3 + 1
                     CCNotcount4 = CCNotcount4 + 1
                     CCNotcount5 = CCNotcount5 + 1
                 case 1:
                    CCcount = CCcount + 1 
                    CCNotcount2 = CCNotcount2 + 1
                    CCNotcount3 = CCNotcount3 + 1
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1
                 case 2:
                    CCcount = CCcount + 1 
                    CCcount2 = CCcount2 + 1
                    CCNotcount3 = CCNotcount3 + 1
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1
                 case 3:
                    CCcount = CCcount + 1 
                    CCcount2 = CCcount2 + 1
                    CCcount3 = CCcount3 + 1   
                    CCNotcount4 = CCNotcount4 + 1
                    CCNotcount5 = CCNotcount5 + 1 
                 case 4:
                     CCcount = CCcount + 1
                     CCcount2 = CCcount2 + 1
                     CCcount3 = CCcount3 + 1            
                     CCcount4 = CCcount4 + 1                            
                     CCNotcount5 = CCNotcount5 + 1 
              case 3:
                match c:
                 case 0:
                     CCCNotcount = CCCNotcount + 1                
                     CCCNotcount2 = CCCNotcount2 + 1
                     CCCNotcount3 = CCCNotcount3 + 1
                     CCCNotcount4 = CCCNotcount4 + 1
                     CCCNotcount5 = CCCNotcount5 + 1
                 case 1:
                     CCCcount = CCCcount + 1 
                     CCCNotcount2 = CCCNotcount2 + 1
                     CCCNotcount3 = CCCNotcount3 + 1
                     CCCNotcount4 = CCCNotcount4 + 1
                     CCCNotcount5 = CCCNotcount5 + 1
                 case 2:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCNotcount3 = CCCNotcount3 + 1
                    CCCNotcount4 = CCCNotcount4 + 1
                    CCCNotcount5 = CCCNotcount5 + 1
                 case 3:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCcount3 = CCCcount3 + 1   
                    CCCNotcount4 = CCCNotcount4 + 1
                    CCCNotcount5 = CCCNotcount5 + 1
                 case 4:
                    CCCcount = CCCcount + 1 
                    CCCcount2 = CCCcount2 + 1
                    CCCcount3 = CCCcount3 + 1            
                    CCCcount4 = CCCcount4 + 1                            
                    CCCNotcount5 = CCCNotcount5 + 1
              case 4:
                match c:
                 case 0:
                     CCCCNotcount = CCCCNotcount + 1                
                     CCCCNotcount2 = CCCCNotcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 1:
                     CCCCcount = CCCCcount + 1 
                     CCCCNotcount2 = CCCCNotcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 2:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCNotcount3 = CCCCNotcount3 + 1
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 3:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCcount3 = CCCCcount3 + 1   
                     CCCCNotcount4 = CCCCNotcount4 + 1
                     CCCCNotcount5 = CCCCNotcount5 + 1
                 case 4:
                     CCCCcount = CCCCcount + 1
                     CCCCcount2 = CCCCcount2 + 1
                     CCCCcount3 = CCCCcount3 + 1              
                     CCCCcount4 = CCCCcount4 + 1                            
                     CCCCNotcount5 = CCCCNotcount5 + 1
              

                 #1    #2     #3        #4       #5       #6         #7      #8            #9           #10     #11     #12     #13       #14      #15         #16       #17         #18       #19             #20       #21    #22      #23      #24        #25        #26       #27        #28         #29          #30         #31    #32      #33       #34       #35       #36        #37        #38          #39          #40                                                      
        arr = [count,Ccount,CCcount,CCCcount,CCCCcount,Notcount,CNotcount,CCNotcount,CCCNotcount,CCCCNotcount,count2,Ccount2,CCcount2,CCCcount2,CCCCcount2,Notcount2,CNotcount2,CCNotcount2,CCCNotcount2,CCCCNotcount2,count3,Ccount3,CCcount3,CCCcount3,CCCCcount3,Notcount3,CNotcount3,CCNotcount3,CCCNotcount3,CCCCNotcount3,count4,Ccount4,CCcount4,CCCcount4,CCCCcount4,Notcount4,CNotcount4,CCNotcount4,CCCNotcount4,CCCCNotcount4]       
        return arr

 