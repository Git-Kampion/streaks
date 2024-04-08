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

browser.get("https://www.flashscore.com/football/italy/serie-b/results/")


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
findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")

findCookie.click()
time.sleep(10)

""""
_flag = True
while _flag:
		try:
			browser.find_element(By.LINK_TEXT,"Show more matches").click()
			time.sleep(10)
			_flag = True
		except(NoSuchElementException):
			_flag = False
time.sleep(10)	  
"""
""""
matchesPopUps = browser.find_elements(By.CLASS_NAME, "event__match") 
homeaway2ndHScore = ([],[])


for bele in matchesPopUps:
 elem = bele.click()
 secWindow = browser.window_handles[1]
 browser.switch_to.window(secWindow)
 time.sleep(10)
 kjj = browser.find_element(By.CLASS_NAME,"smv__verticalSections").text.split()
 home2ndHScore = []
 away2ndHScore = []
 ndFound = False
 ndfoundSec = False
 SecHalfDash = False
 for id in kjj:
    if id == "2ND":
       ndFound = True
    else:
      if ndFound == True and id != "HALF":
          home2ndHScore.append(id)
          ndFound = False
          SecHalfDash = True
      if id == "-" and SecHalfDash == True:
        ndfoundSec = True
        SecHalfDash = False
      else:
        if ndfoundSec == True:
          away2ndHScore.append(id)
          ndfoundSec = False
 homeaway2ndHScore[0].append(home2ndHScore)
 homeaway2ndHScore[1].append(away2ndHScore)
 firstWindow = browser.window_handles[0]
 browser.close()
 browser.switch_to.window(firstWindow)
 """

matches = browser.find_elements(By.ID, "live-table") 
#rounds = browser.find_elements(By.CLASS_NAME, "event__round") 
rounds = matches[0].text.split("ROUND")
for elem in rounds:
 matchRound = 0;
 firstIter = 0;
 soccerMAtch = "";
 skipLeagueNAme = False
 flag = False;
 soccerList = []

 if "ITALY" in elem:
    skipLeagueNAme = 0
 else:
   
       sdsc = elem.splitlines()
       for matcd in sdsc:
        if matchRound == 0:
           matchRound = matcd.strip()           
        else:
          if matchRound != 0:
                  dateTime= matcd.strip().split(" ")
                  if len(dateTime) > 1:
                    matcd = dateTime[0] + dateTime[1]
                  soccerMAtch = soccerMAtch + " " + matcd
                  firstIter = firstIter + 1  
          if firstIter == 5:
                if soccerMAtch != "":
                  soccerList.append(matchRound  + soccerMAtch + " " + "5" + " " +"8")
                  soccerMAtch = "";
                  firstIter =0;
            
           
       #soccerList.append(matchRound + " " + soccerMAtch.strip())   
 
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
      
      if "Pen" in polstriped[2]:
          insert_stmt = "INSERT INTO serieBB(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
          data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],polstriped[5],polstriped[6],polstriped[7],polstriped[8])
      else:
          insert_stmt = "INSERT INTO serieBB(Round,Tframe,home,away,hgoal,agoal,hhgoal,ahgoal) VALUES (?,?, ?, ?, ?,?, ?, ?)"
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
