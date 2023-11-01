#BetTypesObjectRet.py
class BtOr:
    def MatchRes(Title,body):
        arr = []
        cl1 =  body.split("\n")
       # HomeName = cl1[0]
        HomeWinOdd = cl1[1]
       # DrawName = cl1[2]
       # DrawOdd = cl1[3]
       # AwayName = cl1[4]
        AwayWinOdd = cl1[5] 
        arr[0] = HomeWinOdd
        arr[0] = AwayWinOdd
        return   arr

      
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

    def OverUnder(Title,body):
        cl1 =  body.split("\n")
        OverSingleGoalLabel = cl1[0]
        OverSingleGoal = cl1[1]
        UnderSingleGoalLabel = cl1[2]
        UnderSingleGoal = cl1[3]
        OvertwoGoalLabel = cl1[4]
        OvertwoeGoal = cl1[5]           
        UnderTwoGoalLabel = cl1[6]
        UnderTwoGoal = cl1[7]
        OverThreeGoalLabel = cl1[8]
        OverThreeGoal = cl1[9]  
        UnderThreeGoalLabel = cl1[10]
        UnderThreeGoal = cl1[11]
        OverFourGoalLabel = cl1[12]
        OverFourGoal = cl1[13]
        UnderFourGoalLabel = cl1[14]
        UnderFourGoal = cl1[15]
        OverFiveGoalLabel = cl1[16]
        OverFiveGoal = cl1[17]  
        UnderFiveGoalLabel = cl1[18]
        UnderFiveGoal = cl1[19] 

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