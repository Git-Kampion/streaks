import time
import pyodbc
from TypesObjectRet import BtOr
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException

# Launch Chrome browser in headless mode
options = webdriver.FirefoxOptions()
#options.add_argument("headless")
browser = webdriver.Firefox(options=options)
#https://www.betway.co.za/sport/soccer/germany/bundesliga#
# Load web page
file = open("leagues.txt", "r")
content = file.read().split("\n")
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\odds.accdb')

cursor = conn.cursor()
for lnk in content:
 linnk = lnk.split(" ")[0]
 if linnk != "#":
  browser.get(linnk)
  # Network transport takes time. Wait until the page is fully loaded
  def is_ready(browser):
      return browser.execute_script(r"""
          return document.readyState === 'complete'
      """)
  WebDriverWait(browser, 30).until(is_ready)

  # Scroll to bottom of the page to trigger JavaScript action
  #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  #time.sleep(1)
  #WebDriverWait(browser, 30).until(is_ready)
  browser.maximize_window()
  # Search for news headlines and print
  loops = 3
  #loadFullFix = browser.find_elements(By.LINK_TEXT, "Show more mataches")
  time.sleep(5)
  #loadFullFix = browser.find_elements(By.CLASS_NAME, "event__more") 
  findCookie = browser.find_element(By.ID, "cookiePopupClose")

  try:
    findCookie.click()
  except:
   f = ""
  time.sleep(5)
  links = []
  cookies = browser.find_elements(By.XPATH, "//div[contains(@id, '" + lnk.split(" ")[2] +"')]//a[contains(@class, 'PaddingScreen')]")
  for lll in cookies:
   links.append(lll.get_attribute('href'))

  #findCookie = browser.execute_script("document.getElementsByClassName('PaddingScreen')")
  
    #BtOr.breakDown(panels)

  for biscuit in links:
    #href = biscuit.get_attribute('href')
    browser.get(biscuit)
    time.sleep(2)
    eventName = browser.find_element(By.XPATH, "//span[contains(@class, 'ellipsMultiMarket theFont')]//span").text

    dd = BtOr.checkDataBase(conn,eventName,lnk.split(" ")[1]);
    if len(dd) < 1:
      _flag = True;
      _flag1 = True;
      while _flag1:
        try:
          lmb = browser.find_element(By.ID,"AllMarketsButton").click() 
          time.sleep(5)
        except(ElementNotInteractableException):
              _flag1 = False
              while _flag:
                  try:
                     
                      lmb = browser.find_element(By.ID,"loadMoreButton").click()
                      _flag = True
                      time.sleep(5)
                  except(ElementNotInteractableException):
                    _flag = False

      
      #eventName = browser.find_element(By.CLASS_NAME, "ellipsMultiMarket theFont")
      dateTime = browser.find_element(By.XPATH, "//div[contains(@class, 'date-heading theFont')]").text   
      panels =  browser.find_elements(By.XPATH, "//div[contains(@id, 'accordion')]")
      panelsBodies =  browser.find_elements(By.XPATH, "//div[contains(@class, 'acc-header123 panel-collapse collapse')]")

    
      newMelem = BtOr.removeEmptyPAnels(panels)
        
      time.sleep(2)

      lastDiv = []
      OUres = []
      res = []
      BTSRes = []
      DCRes = []
      homeTotal =[]
      awayTotal =[]
      homeTotalDone = False

      lopI = 1;
      for elem in panelsBodies:
        innt = len(lastDiv)
        divId = elem.get_property("id")  
        browser.execute_script("document.getElementById('"+divId+"').style.display = 'block';")
        try:
          for melem in newMelem:
          
            if melem not in lastDiv:
              lastDiv.append(melem)

              #if innt == 1: 
              txt = melem.split("\n")[0]
              elem =  elem.text.split("\n")
              elem =  BtOr.checkBolts(elem)
              match txt:
                  case "Overs/Unders":
                    OUres =  BtOr.OverUndeBreakdown(elem)
                  case "Match Result (1X2)":
                    res =  BtOr.MatchResbreakDown(elem)
                    homeTeam = elem[0]
                    awayTeam = elem[4]
                  case "Both Teams To Score":
                    BTSRes =  BtOr.BothTSBreakDown(elem)            
                  case "Double Chance":
                    DCRes =  BtOr.DcBreakDown(elem)
                  
                  case "1st Half - 1X2":
                    firstHRes =  BtOr.firstHalvWin(elem)
                  case "1st Half - Both Teams To Score":
                    firstHBTS =  BtOr.firstBothTSBreakDown(elem)
                  case "1st Half - Double Chance":
                    firstHDC =  BtOr.firstDCBreakDown(elem)
                  case "1st Half - Overs/Unders":
                    firstHOU =  BtOr.firstOverUnderBreakDown(elem)
                  case "1st Half - Home Overs/Unders":
                    firstHHOU =  BtOr.firstHomOverUnderBreakDown(elem)
                  case "1st Half - Away Overs/Unders":
                    firstHAOU =  BtOr.firstAwaOverUnderBreakDown(elem)

                  case "2nd Half 1X2":
                    secHRes =  BtOr.firstHalvWin(elem)
                  case "2nd Half Double Chance":
                    secHDC =  BtOr.firstDCBreakDown(elem)
                  case "2nd Half Both Teams To Score":
                    secHBTS =  BtOr.firstBothTSBreakDown(elem)
                  case "2nd Half - Overs/Unders":
                    secHOU =  BtOr.firstOverUnderBreakDown(elem)
            
            
              if txt.split()[-1] == "Total" and homeTotalDone == False:
                homeTotal =  BtOr.OverUndeBreakdown(elem)
                homeTotalDone =True
                break;
            
                
              if txt.split()[-1] == "Total" and homeTotalDone == True:
                awayTotal =  BtOr.OverUndeBreakdown(elem)
                homeTotalDone == False
              break;
        except:
          g = 0      
      insert_stmt = "INSERT INTO "+lnk.split(" ")[1]+"(ATeam,HTeam,MatchResHome,MatchResAway,DCHome,DCAway,DCHomeAway,BTSYes,BTSNo,MatchResOverZ,MatchResOverOne,MatchResOverTwo,MatchResOverThree,MatchResOverFour,MatchResOverFive,MatchResUnderZ,MatchResUnderOne,MatchResUnderTwo,MatchResUnderThree,MatchResUnderFour,MatchResUnderFive,firstHalvHomeWin,firstHalvAwayWin,firstHalvBTSYes,firstHalvBTSNo,firstHalvAwayHome,firstHalvAwayDraw,firstHalvHomeDraw,firstHalvOverZero,firstHalvOverOne,firstHalvOverTwo,firstHalvUnderZero,firstHalvUnderOne,firstHalvUnderTwo,firstHalvHomeOverZero,firstHalvHomeOverOne,firstHalvHomeOverTwo,firstHalvHomeUnderZero,firstHalvHomeUnderOne,firstHalvHomeUnderTwo,firstHalvAwayOverZero,firstHalvAwayOverOne,firstHalvAwayOverTwo,firstHalvAwayUnderZero,firstHalvAwayUnderOne,firstHalvAwayUnderTwo,secHalvHomeWin,secHalvAwayWin,secHalvBTSYes,secHalvBTSNo,secHalvAwayHome,secHalvAwayDraw,secHalvHomeDraw,secHalvOverZero,secHalvOverOne,secHalvOverTwo,secHalvUnderZero,secHalvUnderOne,secHalvUnderTwo,HomeOverZero,HomeOverOne,HomeOverTwo,HomeOverThree,HomeOverFour,HomeOverFive,HomeUnderZero,HomeUnderOne,HomeUnderTwo,HomeUnderThree,HomeUnderFour,HomeUnderFive,AwayOverZero,AwayOverOne,AwayOverTwo,AwayOverThree,AwayOverFour,AwayOverFive,AwayUnderZero,AwayUnderOne,AwayUnderTwo,AwayUnderThree,AwayUnderFour,AwayUnderFive) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
      

      try:
        data = (res[1],res[0],res[2],res[3],DCRes[0],DCRes[1],DCRes[2],BTSRes[0],BTSRes[1],OUres[0],OUres[1],OUres[2],OUres[3],OUres[4],OUres[5],OUres[6],OUres[7],OUres[8],OUres[9],OUres[10],OUres[11],firstHRes[2],firstHRes[3],firstHBTS[0],firstHBTS[1],firstHDC[0],firstHDC[1],firstHDC[2],firstHOU[0],firstHOU[1],firstHOU[2],firstHOU[3],firstHOU[4],firstHOU[5],firstHHOU[0],firstHHOU[1],firstHHOU[2],firstHHOU[3],firstHHOU[4],firstHHOU[5],firstHAOU[0],firstHAOU[1],firstHAOU[2],firstHAOU[3],firstHAOU[4],firstHAOU[5],secHRes[2],secHRes[3],secHBTS[0],secHBTS[1],secHDC[0],secHDC[1],secHDC[2],secHOU[0],secHOU[1],secHOU[2],secHOU[3],secHOU[4],secHOU[5],homeTotal[0],homeTotal[1],homeTotal[2],homeTotal[3],homeTotal[4],homeTotal[5],homeTotal[6],homeTotal[7],homeTotal[8],homeTotal[9],homeTotal[10],homeTotal[11],awayTotal[0],awayTotal[1],awayTotal[2],awayTotal[3],awayTotal[4],awayTotal[5],awayTotal[6],awayTotal[7],awayTotal[8],awayTotal[9],awayTotal[10],awayTotal[11])     
      except:
        data = (res[1],"N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A")

      cursor.execute(insert_stmt, data)
      cursor.commit()  
      time.sleep(5)
    else:
      a = 0

