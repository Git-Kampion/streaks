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
browser.get("https://www.betway.co.za/sport/soccer#")
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

findCookie.click()
time.sleep(5)

#findCookie = browser.find_element(By.ID, "leagueGroup")

browser.execute_script("document.getElementById('leagueGroup').style.display = 'block';")
time.sleep(5)
#loadFullFix = browser.find_elements(By.CLASS_NAME, "dropdown-submenu") 
browser.execute_script("document.getElementsByClassName('dropdown-submenu')[0].setAttribute('class', 'dropdown-submenu open')")
#browser.execute_script(loadFullFix[0]+".setAttribute('class', 'dropdown-submenu open')")
browser.execute_script("document.getElementsByClassName('state-icon glyphicon glyphicon-unchecked')[0].setAttribute('class', 'state-icon glyphicon glyphicon-check')")
#loadFullFix2 = browser.execute_script("document.getElementsByClassName('state-icon glyphicon glyphicon-unchecked')")
#browser.execute_script(loadFullFix2[0]+".setAttribute('class', 'state-icon glyphicon glyphicon-check')")
findCooki = browser.find_element(By.ID, "continueBtn")
findCooki.click()
time.sleep(5)
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