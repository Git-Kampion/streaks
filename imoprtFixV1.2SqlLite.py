import time
import sqlite3
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Paths
ROOT = Path(__file__).resolve().parent
DB = ROOT / "footballFixtures.sqlite"
LEAGUES = ROOT / "leagues2Fix.txt"

# Chrome options
options = Options()
# options.add_argument("--headless=new")  # Uncomment for headless on GitHub Actions
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver (adjust if needed)
chrome_driver_path = "/usr/bin/chromedriver"  # GitHub Actions default path

browser = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

def dataLookUp(ScotlandA24, matchUpsCount):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {ScotlandA24}")
        sql_data = cursor.fetchall()
        dataNum = len(sql_data) if sql_data else 0
    except:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

def dataLookUp2(tea, ScotlandA24):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    try:
        insert_stmt2 = f"SELECT * FROM {ScotlandA24} WHERE Home='{tea.split()[0]}' AND Away='{tea.split()[1]}'"
        cursor.execute(insert_stmt2)
        sql_data = cursor.fetchall()
        dataNum = len(sql_data) if sql_data else 0
    except:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

# Load leagues file
with LEAGUES.open("r", encoding="utf-8") as file:
    content = file.read().splitlines()

cookiRan = False

for lnk in content:
    linnk = lnk.split(" ")[0]
    if linnk not in ("#", " "):
        browser.get(linnk)
        WebDriverWait(browser, 30).until(lambda b: b.execute_script("return document.readyState === 'complete'"))
        browser.maximize_window()
        time.sleep(10)

        if not cookiRan:
            try:
                findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
                findCookie.click()
                cookiRan = True
                time.sleep(5)
            except NoSuchElementException:
                pass

        _flag = True
        while _flag:
            try:
                show_more = browser.find_element(By.LINK_TEXT, "Show more matches")
                browser.execute_script("arguments[0].scrollIntoView(true);", show_more)
                browser.execute_script("arguments[0].click();", show_more)
                time.sleep(20)
            except NoSuchElementException:
                _flag = False
        time.sleep(5)

        matchesPopUps = browser.find_elements(By.CLASS_NAME, "event__match")

        for bele in matchesPopUps:
            ull = bele.text.split("\n")
            dateTime = ull[0].split(" ")[0]
            mm = dateTime.split(".")
            fullDate = f"2025-{mm[1]}-{mm[0]}-{ull[0].split()[1]}"

            try:
                Hteam = ull[1].replace(" ", "")
            except:
                Hteam = ull[1]
            try:
                Ateam = ull[2].replace(" ", "")
            except:
                Ateam = ull[2]

            round_no = "0"
            dttyl = f"{round_no} {fullDate} {Hteam} {Ateam}"
            polstriped = dttyl.split(" ")

            conn = sqlite3.connect(DB)
            cursor = conn.cursor()
            if "Penalty" in polstriped[2]:
                insert_stmt = f"INSERT INTO {lnk.split()[2]} (Round,Tframe,home,away) VALUES (?, ?, ?, ?)"
                data = (polstriped[0], polstriped[1], polstriped[3], "")
            else:
                insert_stmt = f"INSERT INTO {lnk.split()[2]} (Round,Tframe,home,away) VALUES (?, ?, ?, ?)"
                data = (polstriped[0], polstriped[1], polstriped[2], polstriped[3])
            try:
                cursor.execute(insert_stmt, data)
            except:
                data = (polstriped[0], polstriped[1], polstriped[3], "")
                cursor.execute(insert_stmt, data)

            conn.commit()
            cursor.close()
            conn.close()

browser.quit()
