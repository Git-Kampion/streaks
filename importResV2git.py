import time
import pyodbc
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    ElementClickInterceptedException, ElementNotInteractableException,
    NoSuchElementException, TimeoutException, WebDriverException
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# --- Paths (relative to repo root) ---
ROOT = Path(__file__).resolve().parent
DB1 = ROOT /  "2026.accdb"
DB2 = ROOT /  "2026.accdb"
LEAGUES = ROOT / "leagues26Res.txt"

# --- Firefox headless ---
options = Options()
options.headless = True  # (or) options.add_argument("-headless")
browser = webdriver.Firefox(options=options)

def dataLookUp(ScotlandA24, matchUpsCount):
    # Connect to database (DB1)
    conn = pyodbc.connect(
        rf"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB1}"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM " + ScotlandA24
    cursor.execute(query)
    sql_data = pd.DataFrame(cursor.fetchall())
    try:
        dataNum = len(sql_data[0])
    except Exception:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

# Load web page list
with open(LEAGUES, "r", encoding="utf-8") as f:
    content = f.read().split("\n")


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
  if cookiRan is False:
    try:
        findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
        findCookie.click()
        cookiRan = True
        time.sleep(5)
    except NoSuchElementException:
        pass


<<<<<<< HEAD
        for bele in matchesPopUps:
            if countUps > iteloop:
                href = bele.get_attribute("href")
                if href:
                    browser.execute_script(f"window.open('{href}', '_blank');")
                    time.sleep(10)
                browser.switch_to.window(browser.window_handles[-1])
                success = False
                time.sleep(10)
=======
 
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
>>>>>>> parent of 22c0f94 (SqlLiteSolution)

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
      bjj = browser.find_elements(By.CLASS_NAME,"wcl-breadcrumbItem_CiWQ7")
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
          conn = pyodbc.connect(rf"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB2}")
          cursor = conn.cursor()
           
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

  
            

   
