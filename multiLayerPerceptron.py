class mlp:
 def aConHCon(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[5]) 
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[6])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
 def aScorHScor(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[6]) 
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
 def aScorHFsc(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[6]) 
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
 def aScorHFsc(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[6]) 
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
 def aConHFsc(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[5]) 
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
 def aFHFsc(t,sql_data,betype,inx):
  overs = ([],[],[],[],[])
  unders = ([],[],[],[],[])
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
  indxFound = False
  index = 0
  for ee in sql_data[0]:
   
   if index == 0 or index == ee[0]:
    index = 0
    indxFound = False
    if ee[4] == t:
     fullt =  int(ee[5]) +  int(ee[6])
     index = ee[0]
     if fullt > 4:
      fullt = 4
     match fullt:
        case 0:
         index = 0
        case 1:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4 
           index = hm[0]
           match fulltH:
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
             underovr4 += 1
            case 4:
             countovr1 += 1
             countovr2 += 1
             countovr3 += 1
             countovr4 += 1
           break;
        
        case 2:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNunderovr4 += 1
            case 4:
             HNexcountovr1 += 1
             HNexcountovr2 += 1
             HNexcountovr3 += 1
             HNexcountovr4 += 1
           break;
        case 3:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           index = hm[0]
           if fulltH > 4:
             fulltH = 4
           match fulltH:
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
             HNTunderovr4 += 1
           
            case 4:
             HNTexcountovr1 += 1
             HNTexcountovr2 += 1
             HNTexcountovr3 += 1
             HNTexcountovr4 += 1
           break;
        case 4:
         for hm in sql_data[0]:
          if index == hm[0]:
           indxFound = True
          if hm[3] == t and indxFound == True:
           fulltH =  int(hm[5]) +  int(hm[6])
           if fulltH > 4:
             fulltH = 4
           index = hm[0]
           indxFound = False
           match fulltH:
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
             HNTTunderovr4 += 1

            case 4:
             HNTTexcountovr1 += 1
             HNTTexcountovr2 += 1
             HNTTexcountovr3 += 1
             HNTTexcountovr4 += 1
           break;
            #0          #1        #2      #3        #4        #5        #6        #7          #8            #9           #10            #11       #12          #13          #14           #15         #16             #17           #18          #19          #20             #21           #22           #23            #24           #25            26              27              28              29            30            31                                            
  arr = [countovr1,underovr1,countovr2,underovr2,countovr3,underovr3,countovr4,underovr4,HNexcountovr1,HNunderovr1,HNexcountovr2,HNunderovr2,HNexcountovr3,HNunderovr3,HNexcountovr4,HNunderovr4,HNTexcountovr1,HNTunderovr1,HNTexcountovr2,HNTunderovr2,HNTexcountovr3,HNTunderovr3,HNTexcountovr4,HNTunderovr4,HNTTexcountovr1,HNTTunderovr1,HNTTexcountovr2,HNTTunderovr2,HNTTexcountovr3,HNTTunderovr3,HNTTexcountovr4,HNTTunderovr4]
  return arr
  
 

         
  
  