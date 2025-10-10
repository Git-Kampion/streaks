import time
import pyodbc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
 
# Launch Chrome browser in headless mode
options = webdriver.FirefoxOptions()

options.add_argument("headless")
browser = webdriver.Firefox(options=options)
def dataLookUp(ScotlandA24,matchUpsCount):
 
  # Connect to database
  conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\2026.accdb')
  cursor = conn.cursor()

  # Select query
  query = "SELECT * FROM " + ScotlandA24

  # Execute and fetch results
  cursor.execute(query)
  sql_data = pd.DataFrame(cursor.fetchall())
  try:
   dataNum  = len(sql_data[0])
  except:
     dataNum = 0
  # Cleanup
  cursor.close()
  conn.close()

  return dataNum
# Load web page
file = open("leagues26Res.txt", "r")
content = file.read().split("\n")
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb')
cookiRan = False
#cursor = conn.cursor()

#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb')
cookiRan = False
#cursor = conn.cursor()

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
    time.sleep(5)

 
  _flag = True
  while _flag:
      try:
        browser.find_element(By.LINK_TEXT,"Show more matches").click()
        time.sleep(10)
        _flag = True
      except(NoSuchElementException):
        _flag = False
  time.sleep(5)	  
  
  #matchRounds = browser.find_elements(By.CLASS_NAME,"event__round")
  
  #
  matchesPopUps = browser.find_elements(By.CLASS_NAME, "eventRowLink") 
  
  
  homeaway2ndHScore = ([],[])

  iteloop = dataLookUp(lnk.split()[2],len( matchesPopUps))
  countUps = 0
    #matchesPopUps = eachh.find_elements(By.TAG_NAME, 'div') 
  for bele in matchesPopUps:
    
    if countUps > iteloop:
      
      href = bele.get_attribute("href")
      
      #elem = bele.click()
      if href:
        browser.execute_script(f"window.open('{href}', '_blank');")
        time.sleep(5)
      browser.switch_to.window(browser.window_handles[-1])
      #secWindow = browser.window_handles[0]
      #browser.switch_to.window(secWindow)
      success = False
      time.sleep(5)
      
      #bjj = browser.find_element(By.CLASS_NAME,"tournamentHeaderDescription").text --- Previously is the class name that contains the Round number was tournamentHeaderDescription
      bjj = browser.find_element(By.CLASS_NAME,"wcl-overline_uwiIT wcl-scores-overline-03_KIU9F")
      bjj = bjj[0].text + " " + bjj[1].text + " " + bjj[2].text
      ull = browser.find_element(By.CLASS_NAME,"duelParticipant").text.split("\n")
      dt = ull[0].split(" ")[0]
      Hteam = ull[1].replace(" ", "")
      Ateam = ull[6].replace(" ", "")
      try:
          wjj = bjj.index("ROUND")
          round = bjj[wjj:].split(" ")[1]   
          round2 = int(round)
      except:
            round = "1"
      
      
      if "PLAY" not in bjj and "GROUP" not in bjj and "FINAL" not in bjj :
        while success != True:
          try:
            kjj = browser.find_element(By.CLASS_NAME,"smv__verticalSections").text.split()
            success = True
          except:
            success = False
          home1stHScore = ""
          away1stHScore = ""
          ndFound = False
          ndfoundSec = False
          SecHalfDash = False
          
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
                    if home1stHScore == '' and away1stHScore == '':
                       home1stHScore = 0
                       away1stHScore = 0
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
        dttyl = round + " " + dt + " " + Hteam + " " + Ateam + " "  + home2ndHScore + " " +  away2ndHScore + " " + home1stHScore  + " " + away1stHScore 
        if len(dttyl.split(" ")) > 0:
          conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\2026.accdb;')
          cursor = conn.cursor()
                #cursor.execute("Insert Into EnglishPremData (Round,Time,Home,Away,HScore,AScore) VALUES ('38','2023-04-01','Arsenal','Watford','4','3')")
          
          # home = ""
          # away = ""
          polstriped = dttyl.split(" ")
          # if len(polstriped) > 8:         
            #  home = 
            
          if "Penalty" in polstriped[2]:
                insert_stmt = "INSERT INTO "+lnk.split(" ")[2]+"(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
                data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],polstriped[5],polstriped[6],polstriped[7],polstriped[8])

          else:
              insert_stmt = "INSERT INTO "+lnk.split(" ")[2]+"(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
              data = (polstriped[0],polstriped[1],polstriped[2],polstriped[3],polstriped[4],polstriped[5],polstriped[6],polstriped[7])

          try:
              cursor.execute(insert_stmt, data)
          except:
                data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],polstriped[5],polstriped[6],'0','0')
              
          cursor.commit()
          cursor.close()
          conn.close()  
      firstWindow = browser.window_handles[0]
      browser.close()
      browser.switch_to.window(firstWindow)    
    countUps = countUps +1

  
            

   
