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

# Load web page
browser.get("https://www.betway.co.za/sport/soccer/eng/premier_league#")
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
time.sleep(2)
#loadFullFix = browser.find_elements(By.CLASS_NAME, "event__more") 
findCookie = browser.find_element(By.ID, "cookiePopupClose")

findCookie.click()
time.sleep(4)

#findCookie = browser.execute_script("document.getElementsByClassName('PaddingScreen')")


findCookie = browser.find_elements(By.XPATH, "//div[contains(@id, 'leagueGroup-ENGPremierLeague')]//a[contains(@class, 'PaddingScreen')]")
href = findCookie[0].get_attribute('href')
browser.get(href)
time.sleep(2)


_flag = True;
_flag1 = True;
while _flag1:
    try:
     almb = browser.find_element(By.ID,"AllMarketsButton").click() 
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
eventName = browser.find_element(By.XPATH, "//span[contains(@class, 'ellipsMultiMarket theFont')]//span").text
dateTime = browser.find_element(By.XPATH, "//div[contains(@class, 'date-heading theFont')]").text   
panels =  browser.find_elements(By.XPATH, "//div[contains(@id, 'accordion')]")
panelsBodies =  browser.find_elements(By.XPATH, "//div[contains(@class, 'acc-header123 panel-collapse collapse')]")

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok\Documents\work\Flashscore\streaks\2022-23Base.accdb')

cursor = conn.cursor()
#BtOr.breakDown(panels)
newMelem = BtOr.removeEmptyPAnels(panels)
   
time.sleep(2)

lastDiv = []
OUres = []
res = []
BTSRes = []
DCRes = []

lopI = 1;
for kekk in panelsBodies:
  elemID =  kekk.get_attribute("id"); 
  browser.execute_script("document.getElementById('" + elemID +"').style.display = 'block';")
  panelBody = browser.find_element(By.XPATH, "//div[contains(@id,'" + elemID+ "')]//div[contains(@class, 'panel-body')]").text
  
  panelText = panels[lopI].text
  
  #refinedRes = BtOr.MatchRes(panelText,panelBody) 

  match panelText:
    case "Match Result (1X2)":
       refinedRes = BtOr.MatchRes(panelText,panelBody) 
    case "Both Teams To Score":
         refinedBTS = BtOr.Bts(panelText,panelBody) 
    case "Double Chance":
         refinedDC = BtOr.Dc(panelText,panelBody)
    case "Draw No Bet":
         refinedDnB = BtOr.DrawNoBet(panelText,panelBody)
    case "Overs/Under":
         refinedDnB = BtOr.OverUndeBreakdown(panelText,panelBody)
    case "Handicap":
         refinedDnB = BtOr.Handicap(panelText,panelBody)
    case "1st Goal":
         refinedDnB = BtOr.FirstGoal(panelText,panelBody)
    case "10 Minutes - 1X2 From 1 To 10":
         refinedDnB = BtOr.TenMin(panelText,panelBody) 
    case "Both Halves Over 1.5":
         refinedDnB = BtOr.BothHalfsOever(panelText,panelBody) 
    case "Both Halves Under 1.5":
         refinedDnB = BtOr.BothHalfsUnder(panelText,panelBody)
    case "Multigoals":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody)  
    case "Sending Off":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody) 
    case "1st Half - 1X2":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody)
    case "1st Half - Both Teams To Score":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody)   
    case "1st Half - Double Chance":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody) 
    case "1st Half - Overs/Unders":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody) 
    case "1st Half - Handicap":
         refinedDnB = BtOr.MultiGoals(panelText,panelBody)  
   
  lopI = lopI + 1  

time.sleep(5)

