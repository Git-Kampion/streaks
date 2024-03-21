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
browser.get("https://www.betway.co.za/sport/soccer/ita/serie_a#")
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


findCookie = browser.find_elements(By.XPATH, "//div[contains(@id, 'leagueGroup-ITASerieA')]//a[contains(@class, 'PaddingScreen')]")
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
for elem in panelsBodies:
    innt = len(lastDiv)
    divId = elem.get_property("id")  
    browser.execute_script("document.getElementById('"+divId+"').style.display = 'block';")
    for melem in newMelem:

     if melem not in lastDiv:
        lastDiv.append(melem)

        #if innt == 1: 
        txt = melem.split("\n")[0]
        elem =  elem.text.split("\n")
        match txt:
            case "Overs/Unders":
              OUres =  BtOr.OverUndeBreakdown(elem)
            case "Match Result (1X2)":
              res =  BtOr.MatchResbreakDown(elem)
            case "Both Teams To Score":
              BTSRes =  BtOr.BothTSBreakDown(elem)            
            case "DC":
                BtOr.DcBreakDown(elem)
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

            case "1st Half - Away Overs/Unders":
              firstHAOU =  BtOr.firstAwaOverUnderBreakDown(elem)
        break;
insert_stmt = "INSERT INTO EplBetOdds(ATeam,HTeam,MatchResHome,MatchResAway,DCHome,DCAway,DCHomeAway,BTSYes,BTSNo,MatchResOverZ,MatchResOverOne,MatchResOverTwo,MatchResOverThree,MatchResOverFour,MatchResOverFive,MatchResUnderZ,MatchResUnderOne,MatchResUnderTwo,MatchResUnderThree,MatchResUnderFour,MatchResUnderFive,firstHalvHomeWin,firstHalvAwayWin,firstHalvBTSYes,firstHalvBTSNo,firstHalvAwayHome,firstHalvAwayDraw,firstHalvHomeDraw,firstHalvOverZero,firstHalvOverOne,firstHalvOverTwo,firstHalvUnderZero,firstHalvUnderOne,firstHalvUnderTwo,firstHalvHomeOverZero,firstHalvHomeOverOne,firstHalvHomeOverTwo,firstHalvHomeUnderZero,firstHalvHomeUnderOne,firstHalvHomeUnderTwo,firstHalvAwayOverZero,firstHalvAwayOverOne,firstHalvAwayOverTwo,firstHalvAwayUnderZero,firstHalvAwayUnderOne,firstHalvAwayUnderTwo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
data = (res[1],res[0],res[2],res[3],DCRes[0],DCRes[1],DCRes[2],BTSRes[0],BTSRes[1],OUres[0],OUres[1],OUres[2],OUres[3],OUres[4],OUres[5],OUres[6],OUres[7],OUres[8],OUres[9],OUres[10],OUres[11],firstHRes[2],firstHRes[3],firstHBTS[0],firstHBTS[1],firstHDC[0],firstHDC[1],firstHDC[2],firstHOU[0],firstHOU[1],firstHOU[2],firstHOU[3],firstHOU[4],firstHOU[5],firstHHOU[0],firstHHOU[1],firstHHOU[2],firstHHOU[3],firstHHOU[4],firstHHOU[5],firstHAOU[0],firstHAOU[1],firstHAOU[2],firstHAOU[3],firstHAOU[4],firstHAOU[5])
cursor.execute(insert_stmt, data)
cursor.commit()
    


""""
panelBody = browser.find_elements(By.XPATH, "//div[contains(@id,'" + pandelID+ "')]//div[contains(@class, 'panel-body')]")
findCookies = findCookie[0].find_element(By.TAG_NAME, "a")    


insert_stmt = "INSERT INTO EplBetOdds(ATeam,Hteam,MatchResHome,MatchResAway,DCHome,DCAway,DCHomeAway,BTS/Yes,BTS/No,MatchResOverZ,MatchResOverOne,MatchResOverTwo,MatchResOverThree,MatchResOverFour,MatchResOverFive,MatchResUnderZ,MatchResUnderOne,MatchResUnderTwo,MatchResUnderThree,MatchResUnderFour,MatchResUnderFive) VALUES (?,?, ?, ?, ?,?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
data = (res[1],res[0],res[2],res[3],DCRes[0],DCRes[1],DCRes[2],BTSRes[0],BTSRes[1],OUres[0],OUres[1],OUres[2],OUres[3],OUres[4],OUres[5],OUres[6],OUres[7],OUres[8],OUres[9],OUres[10],OUres[11])
cursor.execute(insert_stmt, data)
cursor.commit()



print(browser.find_element_by_css_selector("p.PaddingScreen > a").get_attribute('href'))

href = findCookies.get_attribute('href')
browser.get(href)
time.sleep(10)
"""
"""
try:
 almb = browser.find_element(By.ID,"AllMarketsButton").click()
except(NoSuchElementException):
    while _flag:
        try:
           lmb = browser.find_element(By.ID,"loadMoreButton").click()
           _flag = True
           time.sleep(5)
        except(NoSuchElementException):
                _flag = False
                time.sleep(10)	  

"""

#eventName = browser.find_element(By.CLASS_NAME, "ellipsMultiMarket theFont")

#WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#btnSearch"))).click()

#findCookies[0].click()
#time.sleep(5)

"""
findCookie = browser.find_element(By.ID, "leagueGroup")

browser.execute_script("document.getElementById('leagueGroup').style.display = 'block';")
time.sleep(5)
loadFullFix = browser.find_elements(By.CLASS_NAME, "dropdown-submenu") 
browser.execute_script("document.getElementsByClassName('dropdown-submenu')[0].setAttribute('class', 'dropdown-submenu open')")
browser.execute_script(loadFullFix[0]+".setAttribute('class', 'dropdown-submenu open')")
browser.execute_script("document.getElementsByClassName('state-icon glyphicon glyphicon-unchecked')[0].setAttribute('class', 'state-icon glyphicon glyphicon-check')")
loadFullFix2 = browser.execute_script("document.getElementsByClassName('state-icon glyphicon glyphicon-unchecked')")
browser.execute_script(loadFullFix2[0]+".setAttribute('class', 'state-icon glyphicon glyphicon-check')")
findCooki = browser.find_element(By.ID, "continueBtn")
findCooki.click()
time.sleep(5)
"""
"""
for elem in loadFullFix:
    browser.execute_script(elem+".setAttribute('class', 'dropdown-submenu open')")
    loadFullFix2 = browser.execute_script("document.getElementByClassName('state-icon glyphicon glyphicon-unchecked')")
    for belem in loadFullFix2:
         browser.execute_script(belem+".setAttribute('class', 'state-icon glyphicon glyphicon-check')")
         break;
#browser.execute_script("document.getElementsByClassName('dropdown-submenu')[0].setAttribute('class', 'dropdown-submenu open')");
#browser.execute_script("document.getElementByClassName('dropdown-submenu').setAttribute('class', 'dropdown-submenu open')");
#browser.execute_script("arguments[0].setAttribute('class','vote-link up voted')", element)
"""
time.sleep(5)