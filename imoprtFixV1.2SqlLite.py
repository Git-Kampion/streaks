import time
import sqlite3
import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options

# --- Paths ---
ROOT = Path(__file__).resolve().parent
DB = ROOT / "footballFixtures.sqlite"
LEAGUES = ROOT / "leagues2Fix.txt"   # text file with fixture URLs

# --- Chrome headless ---
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=chrome_options)

def dataLookUp(table_name):
    """Check how many rows already exist in a given table"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    try:
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)
        dataNum = cursor.fetchone()[0]
    except Exception:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

# --- Load leagues list ---
with open(LEAGUES, "r", encoding="utf-8") as f:
    content = f.read().split("\n")

cookiRan = False

for lnk in content:
    linnk = lnk.split(" ")[0]
    if linnk != "#" and linnk.strip() != "":
        try:
            browser.get(linnk)
        except WebDriverException:
            continue

        # Wait for page
        WebDriverWait(browser, 30).until(
            lambda b: b.execute_script("return document.readyState === 'complete'")
        )

        time.sleep(5)

        # Accept cookies once
        if cookiRan is False:
            try:
                findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
                findCookie.click()
                cookiRan = True
                time.sleep(3)
            except NoSuchElementException:
                pass

        # Keep clicking "Show more matches"
        while True:
            try:
                browser.find_element(By.LINK_TEXT, "Show more matches").click()
                time.sleep(5)
            except NoSuchElementException:
                break

        time.sleep(2)
        matchesPopUps = browser.find_elements(By.CLASS_NAME, "event__match")

        iteloop = dataLookUp(lnk.split()[2])
        countUps = 0

        for bele in matchesPopUps:
            if countUps >= iteloop:
                try:
                    ull = bele.text.split("\n")
                    dateTime = ull[0].split(" ")[0]
                    mm = dateTime.split(".")
                    fullDate = f"2025-{mm[1]}-{mm[0]} {ull[0].split(' ')[1]}"

                    Hteam = ull[1].replace(" ", "")
                    Ateam = ull[2].replace(" ", "")
                    round_no = "0"

                    conn = sqlite3.connect(DB)
                    cursor = conn.cursor()

                    insert_stmt = f"""
                        INSERT INTO {lnk.split()[2]} (Round, Tframe, home, away)
                        VALUES (?, ?, ?, ?)
                    """
                    data = (round_no, fullDate, Hteam, Ateam)

                    try:
                        cursor.execute(insert_stmt, data)
                    except Exception as e:
                        print(f"Insert failed: {e}")

                    conn.commit()
                    cursor.close()
                    conn.close()
                except Exception as e:
                    print(f"Skipping match: {e}")

            countUps += 1
