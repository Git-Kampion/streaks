import time
import pyodbc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException


# Launch Chrome browser in headless mode
options = webdriver.FirefoxOptions()
#options.add_argument("headless")
browser = webdriver.Firefox(options=options)

# Load web page
file = open("leagues2.txt", "r")
content = file.read().split("\n")
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')
cookiRan = False
cursor = conn.cursor()
for lnk in content:
 linnk = lnk.split(" ")[0]
 if linnk != "#" and linnk != " ":
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
  time.sleep(10)
  #loadFullFix = browser.find_elements(By.CLASS_NAME, "event__more") 
  if cookiRan == False:
    findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    cookiRan = True
    findCookie.click()
    time.sleep(10)

 
  _flag = True
  while _flag:
      try:
        browser.find_element(By.LINK_TEXT,"Show more matches").click()
        time.sleep(10)
        _flag = True
      except(NoSuchElementException):
        _flag = False
  time.sleep(10)	  
  
  matchesPopUps = browser.find_elements(By.CLASS_NAME, "event__match") 
  
  homeaway2ndHScore = ([],[])
  soccerList = []

  for bele in matchesPopUps:
    elem = bele.click()
    secWindow = browser.window_handles[1]
    browser.switch_to.window(secWindow)
    success = False
    time.sleep(12)
    
    bjj = browser.find_element(By.CLASS_NAME,"tournamentHeaderDescription").text
    ull = browser.find_element(By.CLASS_NAME,"duelParticipant").text.split("\n")
    dt = ull[0].split(" ")[0]
    Hteam = ull[1].replace(" ", "")
    Ateam = ull[6].replace(" ", "")
    
    
    if "PLAY" not in bjj and "GROUP" not in bjj and "FINAL" not in bjj:
      while success != True:
        try:
          kjj = browser.find_element(By.CLASS_NAME,"smv__verticalSections").text.split()
          success = True
        except:
          success = False
        #home2ndHScore = ""
        #away2ndHScore = ""
        home1stHScore = ""
        away1stHScore = ""
        ndFound = False
        ndfoundSec = False
        SecHalfDash = False
        try:
         wjj = bjj.index("ROUND")
         round = bjj[wjj:].split(" ")[1]
        except:
          round = "1"
        home2ndHScore = ull[2]
        away2ndHScore = ull[4]
        for id in kjj:
            if id == "1ST":
              ndFound = True
            else:
              if ndFound == True and id != "HALF":
                  #home2ndHScore = id
                  #away2ndHScore = kjj[kjj.index("1ST") + 4]
                  home1stHScore = id
                  away1stHScore = kjj[kjj.index("1ST") + 4]
                  ndFound = False
                  #SecHalfDash = True
            if id == "2ND":
              ndfoundSec = True
            else:
              if ndfoundSec == True and id != "HALF":
                  #home1stHScore = id
                  #away1stHScore = kjj[kjj.index("2ND") + 4]
                  ndfoundSec = False
                  #SecHalfDash = True
              
      #homeaway2ndHScore[0].append(home2ndHScore)
      #homeaway2ndHScore[1].append(away2ndHScore)
      soccerList.append(round + " " + dt + " " + Hteam + " " + Ateam + " "  + home2ndHScore + " " +  away2ndHScore + " " + home1stHScore  + " " + away1stHScore  )  
    firstWindow = browser.window_handles[0]
    browser.close()
    browser.switch_to.window(firstWindow)
    

  if len(soccerList) > 0:

      conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb;')
      cursor = conn.cursor()
            #cursor.execute("Insert Into EnglishPremData (Round,Time,Home,Away,HScore,AScore) VALUES ('38','2023-04-01','Arsenal','Watford','4','3')")
      countdown = len(soccerList)
      for pol in soccerList:
        # home = ""
        # away = ""
          polstriped = pol.split(" ")
        # if len(polstriped) > 8:         
          #  home = 
          
          if "Penalty" in polstriped[2]:
              insert_stmt = "INSERT INTO "+lnk.split(" ")[2]+"(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
              data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],polstriped[5],polstriped[6],polstriped[7],polstriped[8])
          else:
              insert_stmt = "INSERT INTO "+lnk.split(" ")[2]+"(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
              data = (polstriped[0],polstriped[1],polstriped[2],polstriped[3],polstriped[4],polstriped[5],polstriped[6],polstriped[7])
          cursor.execute(insert_stmt, data)
          cursor.commit()
          countdown =  countdown - 1
          if countdown == 0:
            cursor.close()
            
                  #create list with first item
          
    #print(rounds[2])



    #cursor.execute('Insert Into EnglishPremData (Round,Time,Home,Away,HScore,AScore) VALUES ()')+ " " + specRound[3] + " " + specRound[4] + " " + specRound[5] + " " + specRound[6] + " " + specRound[7]
      
    


    #browser.close() print(elem.text)
    #
    # Close the browser once finish
