class HaFilters:
 teams = []
 Ateams = []
 Ateam = []
 numOfGames = []
 FullTimeOvers= ([],[],[])
 def awayFilter(data):
  for bb in data[0]:
   if bb[4] in Ateams:
    t = bb[4]
   else:
    Ateams.append(bb[4])
  
   for w in Ateams:
    t = w
    occurence = 0
    if t in Ateam:
      occurence = 0
    else:
     rfdA = BtOr.refindedDatam(t,data,4)
     afullTimeOver = BtOr.FixOverUnders(t,rfdA,"a",6)
     BtOr.createReport(t,rfdA,afullTimeOver,pd)

     

def homeFilter(data):
  for ee in sql_data[0]:
   if ee[3] in teams:
    t = ee[3]
   else:
    teams.append(ee[3])

