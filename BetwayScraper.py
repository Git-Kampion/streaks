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
browser.get("https://www.betway.co.za/sport/soccer/eng/premier_league#")
# Network transport takes time. Wait until the page is fully loaded
def is_ready(browser):
    return browser.execute_script(r"""
        return document.readyState === 'complete'
    """)
WebDriverWait(browser, 30).until(is_ready)

browser.get
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

findCookie.click()
time.sleep(5)

#findCookie = browser.execute_script("document.getElementsByClassName('PaddingScreen')")


findCookie = browser.find_elements(By.XPATH, "//div[contains(@id, 'leagueGroup-ENGPremierLeague')]//a[contains(@class, 'PaddingScreen')]")
href = findCookie[0].get_attribute('href')
browser.get(href)
time.sleep(5)

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

lopI = 1;
for kekk in panelsBodies:
  elemID =  kekk.get_attribute("id"); 
  browser.execute_script("document.getElementById('" + elemID +"').style.display = 'block';")
  panelBody = browser.find_element(By.XPATH, "//div[contains(@id,'" + elemID+ "')]//div[contains(@class, 'panel-body')]").text
  panelText = panels[lopI].text
  lopI = lopI + 1  

time.sleep(5)

""""
for elem in panelsBodies:
     

  
browser.execute_script("document.getElementById('leagueGroup').style.display = 'block';")


panelBody = browser.find_elements(By.XPATH, "//div[contains(@id,'" + pandelID+ "')]//div[contains(@class, 'panel-body')]")
findCookies = findCookie[0].find_element(By.TAG_NAME, "a")    


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

browser.execute_script("document.getElementById('leagueGroup').style.display = 'block';"
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