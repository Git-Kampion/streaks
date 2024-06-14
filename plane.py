import time
import pyodbc
from datetime import datetime
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
time_now = datetime.now()
file = open(str(time_now.date())+".txt", 'a') 
browser.get("https://www.betway.co.za/lobby/casino games/launchgame/casino games/trending/Aviator")
def is_ready(browser):
      return browser.execute_script(r"""
          return document.readyState === 'complete'
      """)
WebDriverWait(browser, 30).until(is_ready)

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


try:
 lmb = browser.find_element(By.ID,"menuMobileNumber")
 lmb.send_keys('632285662')
 inputElement = browser.find_element(By.ID,"menuPassword")
 inputElement.send_keys('Dingdong.2')
 inputElement.submit() 
 
except:
 s = 5
time.sleep(20)

lmb = browser.find_element(By.ID,"lobby_game")
browser.switch_to.frame(lmb);
time.sleep(5)
cc = 1000000000000000000000000000000000000000000000000
arr = []
previousLAstVAlue = ""
while cc > 1:
  lmb = browser.find_element(By.CLASS_NAME,"payouts-block").text
  time_now = datetime.now()
  current_time = time_now.strftime("%H:%M:%S")
  kl = len(lmb.split("\n")) - 1
  gt = lmb.split("\n")[kl]
  
  pr = lmb.split("\n")[kl - 1]
  if gt !=pr and previousLAstVAlue != gt:
    previousLAstVAlue = gt
    arr = [str(current_time) + " " +lmb.split("\n")[0]] + arr
    #arr.append([current_time,lmb.split("\n")[0]])
    cc-=1
    time.sleep(5)
for ii in arr:
 file.write(ii)
file.close



