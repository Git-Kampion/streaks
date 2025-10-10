import time
import sqlite3
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException, ElementNotInteractableException,
    NoSuchElementException, TimeoutException, WebDriverException
)
from selenium.webdriver.firefox.options import Options

# --- Paths (relative to repo root) ---
ROOT = Path(__file__).resolve().parent
DB1 = ROOT / "football.sqlite"
DB2 = ROOT / "football.sqlite"
LEAGUES = ROOT / "leagues26Res.txt"

# --- Headless Firefox configuration ---
options = Options()
options.headless = True
options.set_preference("dom.webnotifications.enabled", False)
options.set_preference("dom.push.enabled", False)
options.set_preference("media.autoplay.default", 0)
options.add_argument("--width=1920")
options.add_argument("--height=1080")

browser = webdriver.Firefox(options=options)

# --- Utility: Wait for full page load ---
def is_ready(browser):
    return browser.execute_script("return document.readyState === 'complete'")

# --- Utility: Clean ads and overlays ---
def remove_ads(browser):
    js = """
    document.querySelectorAll('iframe[id^="google_ads_iframe_"]').forEach(e => e.remove());
    document.querySelectorAll('div[id*="overlay"], div[class*="overlay"]').forEach(e => e.remove());
    """
    browser.execute_script(js)

# --- Utility: Safe click helper ---
def safe_click(browser, by, selector, timeout=15):
    try:
        element = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )
        remove_ads(browser)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        browser.execute_script("arguments[0].click();", element)
        return True
    except (NoSuchElementException, TimeoutException):
        return False
    except ElementClickInterceptedException:
        remove_ads(browser)
        try:
            browser.execute_script("arguments[0].click();", element)
            return True
        except Exception:
            return False

# --- Database lookup helper ---
def dataLookUp(ScotlandA24, matchUpsCount):
    conn = sqlite3.connect(DB1)
    cursor = conn.cursor()
    query = f"SELECT * FROM {ScotlandA24}"
    cursor.execute(query)
    sql_data = pd.DataFrame(cursor.fetchall())
    dataNum = len(sql_data) if not sql_data.empty else 0
    cursor.close()
    conn.close()
    return dataNum

# --- Read list of leagues/URLs ---
with open(LEAGUES, "r", encoding="utf-8") as f:
    content = f.read().split("\n")

cookiRan = False

for lnk in content:
    linnk = lnk.split(" ")[0].strip()
    if linnk and linnk != "#":
        try:
            browser.get(linnk)
        except WebDriverException:
            continue

        WebDriverWait(browser, 30).until(is_ready)
        time.sleep(3)
        remove_ads(browser)

        # Handle cookies banner once
        if not cookiRan:
            try:
                findCookie = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                )
                findCookie.click()
                cookiRan = True
                time.sleep(2)
            except (NoSuchElementException, TimeoutException):
                pass

        # Keep clicking "Show more matches" until none remain
        while True:
            clicked = safe_click(browser, By.LINK_TEXT, "Show more matches")
            if not clicked:
                break
            time.sleep(5)

        time.sleep(2)
        remove_ads(browser)

        matchesPopUps = browser.find_elements(By.CLASS_NAME, "eventRowLink")
        iteloop = dataLookUp(lnk.split()[2], len(matchesPopUps))
        countUps = len(matchesPopUps)

        for bele in matchesPopUps:
            if countUps > iteloop:
                href = bele.get_attribute("href")
                if href:
                    browser.execute_script(f"window.open('{href}', '_blank');")
                    time.sleep(5)
                browser.switch_to.window(browser.window_handles[-1])

                try:
                    bjj = browser.find_element(By.CLASS_NAME, "detail__breadcrumbs")
                    list_items = bjj.find_elements(By.TAG_NAME, "li")
                    bjj = list_items[2].text

                    ull = browser.find_element(By.CLASS_NAME, "duelParticipant").text.split("\n")
                    dt = ull[0].split(" ")[0]
                    Hteam = ull[1].replace(" ", "")
                    Ateam = ull[6].replace(" ", "")
                    try:
                        wjj = bjj.index("ROUND")
                        round = bjj[wjj:].split(" ")[1]
                    except:
                        round = "1"

                    if "PLAY" not in bjj and "GROUP" not in bjj and "FINAL" not in bjj:
                        success = False
                        while not success:
                            try:
                                kjj = browser.find_element(By.CLASS_NAME, "smv__verticalSections").text.split()
                                success = True
                            except:
                                time.sleep(1)

                        home1stHScore = ""
                        away1stHScore = ""
                        home2ndHScore = ull[2]
                        away2ndHScore = ull[4]

                        ndFound = False
                        ndfoundSec = False
                        for id in kjj:
                            if id == "1ST":
                                ndFound = True
                            elif ndFound and id != "HALF":
                                home1stHScore = id
                                away1stHScore = kjj[kjj.index("1ST") + 4]
                                ndFound = False
                            if id == "2ND":
                                ndfoundSec = True
                            elif ndfoundSec and id != "HALF":
                                ndfoundSec = False

                        dttyl = f"{round} {dt} {Hteam} {Ateam} {home2ndHScore} {away2ndHScore} {home1stHScore} {away1stHScore}"
                        conn = sqlite3.connect(DB2)
                        cursor = conn.cursor()

                        polstriped = dttyl.split(" ")
                        insert_stmt = f"""
                            INSERT INTO {lnk.split(" ")[2]}
                            (Round, Tframe, home, away, hgoal, agoal, hhgoal, ahgoal)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """

                        try:
                            cursor.execute(insert_stmt, polstriped[:8])
                        except Exception:
                            fallback = (polstriped[0], polstriped[1], polstriped[3], polstriped[4],
                                        polstriped[5], polstriped[6], '0', '0')
                            cursor.execute(insert_stmt, fallback)

                        conn.commit()
                        cursor.close()
                        conn.close()

                finally:
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
            countUps -= 1

browser.quit()
