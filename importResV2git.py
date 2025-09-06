import time
import sqlite3
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
DB1 = ROOT / "football.sqlite"   # single SQLite database
DB2 = ROOT / "football.sqlite"
LEAGUES = ROOT / "leagues26Res.txt"

# --- Firefox headless ---
options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)

def dataLookUp(ScotlandA24, matchUpsCount):
    # Connect to database (SQLite)
    conn = sqlite3.connect(DB1)
    cursor = conn.cursor()
    query = f"SELECT * FROM {ScotlandA24}"
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

cookiRan = False

for lnk in content:
    linnk = lnk.split(" ")[0]
    if linnk != "#" and linnk != " ":
        try:
         browser.get(linnk)
        except:
            done = 0
            break;
        # Wait until page fully loads
        def is_ready(browser):
            return browser.execute_script("return document.readyState === 'complete'")
        WebDriverWait(browser, 30).until(is_ready)

        browser.maximize_window()
        time.sleep(10)

        if cookiRan is False:
            try:
                findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
                findCookie.click()
                cookiRan = True
                time.sleep(5)
            except NoSuchElementException:
                pass

        # Keep clicking "Show more matches"
        _flag = True
        while _flag:
            try:
                browser.find_element(By.LINK_TEXT, "Show more matches").click()
                time.sleep(10)
                _flag = True
            except NoSuchElementException:
                _flag = False
        time.sleep(5)

        matchesPopUps = browser.find_elements(By.CLASS_NAME, "eventRowLink") 
        iteloop = dataLookUp(lnk.split()[2], len(matchesPopUps))
        countUps = 0

        for bele in matchesPopUps:
            if countUps > iteloop:
                href = bele.get_attribute("href")
                if href:
                    browser.execute_script(f"window.open('{href}', '_blank');")
                    time.sleep(10)
                browser.switch_to.window(browser.window_handles[-1])
                success = False
                time.sleep(10)

                bjj = browser.find_element(By.CLASS_NAME, "detail__breadcrumbs")
                list_items = bjj.find_elements(By.TAG_NAME, "li")
                bjj = list_items[2].text
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
                        home2ndHScore = ull[2]
                        away2ndHScore = ull[4]
                        ndFound = False
                        ndfoundSec = False

                        for id in kjj:
                            if id == "1ST":
                                ndFound = True
                            else:
                                if ndFound == True and id != "HALF":
                                    home1stHScore = id
                                    away1stHScore = kjj[kjj.index("1ST") + 4]
                                    if home1stHScore == '' and away1stHScore == '':
                                        home1stHScore = 0
                                        away1stHScore = 0
                                    ndFound = False
                            if id == "2ND":
                                ndfoundSec = True
                            else:
                                if ndfoundSec == True and id != "HALF":
                                    ndfoundSec = False

                    dttyl = round + " " + dt + " " + Hteam + " " + Ateam + " " + home2ndHScore + " " +  away2ndHScore + " " + home1stHScore  + " " + away1stHScore 
                    if len(dttyl.split(" ")) > 0:
                        conn = sqlite3.connect(DB2)
                        cursor = conn.cursor()

                        polstriped = dttyl.split(" ")
                        
                        insert_stmt = f"""
                            INSERT INTO {lnk.split(" ")[2]}
                            (Round, Tframe, home, away, hgoal, agoal, hhgoal, ahgoal)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """

                        if "Penalty" in polstriped[2]:
                            data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],
                                    polstriped[5],polstriped[6],polstriped[7],polstriped[8])
                        else:
                            data = (polstriped[0],polstriped[1],polstriped[2],polstriped[3],
                                    polstriped[4],polstriped[5],polstriped[6],polstriped[7])

                        try:
                            cursor.execute(insert_stmt, data)
                        except Exception as e:
                            # fallback if issue
                            data = (polstriped[0],polstriped[1],polstriped[3],polstriped[4],
                                    polstriped[5],polstriped[6],'0','0')
                            cursor.execute(insert_stmt, data)

                        conn.commit()
                        cursor.close()
                        conn.close()

                firstWindow = browser.window_handles[0]
                browser.close()
                browser.switch_to.window(firstWindow)    
            countUps += 1
