import time
import pyodbc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException, ElementNotInteractableException,
    NoSuchElementException, TimeoutException, WebDriverException
)

# ---------- Virtual Environment Safe Firefox Driver Setup ----------
def create_browser():
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")  # Optional
    return webdriver.Firefox(options=options)

browser = create_browser()

# ---------- Database Lookup Functions ----------
def dataLookUp(table_name, matchUpsCount):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb;')
    cursor = conn.cursor()
    query = "SELECT * FROM " + table_name
    cursor.execute(query)
    try:
        sql_data = pd.DataFrame(cursor.fetchall())
        dataNum = len(sql_data[0])
    except:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

def dataLookUp2(tea, table_name):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb;')
    cursor = conn.cursor()
    try:
        home, away = tea.split(" ")
        query = f"SELECT * FROM {table_name} WHERE Home = '{home}' AND Away = '{away}'"
        cursor.execute(query)
        sql_data = pd.DataFrame(cursor.fetchall())
        dataNum = len(sql_data[0])
    except:
        dataNum = 0
    cursor.close()
    conn.close()
    return dataNum

# ---------- Main Scraping Logic ----------
def run_scraper():
    cookiRan = False

    with open("leagues2Fix.txt", "r") as file:
        content = file.read().splitlines()

    for lnk in content:
        linnk = lnk.split(" ")[0]
        if linnk.strip() == "#" or not linnk.strip():
            continue

        browser.get(linnk)

        # Wait for full load
        WebDriverWait(browser, 30).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        browser.maximize_window()
        time.sleep(10)

        # Accept cookies once per session
        if not cookiRan:
            try:
                findCookie = browser.find_element(By.ID, "onetrust-accept-btn-handler")
                findCookie.click()
                cookiRan = True
                time.sleep(5)
            except NoSuchElementException:
                pass

        # Click "Show more matches" repeatedly
        while True:
            try:
                browser.find_element(By.LINK_TEXT, "Show more matches").click()
                time.sleep(10)
            except NoSuchElementException:
                break

        time.sleep(5)

        matchesPopUps = browser.find_elements(By.CLASS_NAME, "eventRowLink")
        iteloop = dataLookUp(lnk.split()[2], len(matchesPopUps))
        countUps = 0

        for bele in matchesPopUps:
            if countUps > iteloop:
                href = bele.get_attribute("href")
                if href:
                    browser.execute_script(f"window.open('{href}', '_blank');")
                    time.sleep(5)
                    browser.switch_to.window(browser.window_handles[-1])

                    try:
                        bjj_parts = browser.find_elements(By.CLASS_NAME, "wcl-breadcrumbItem_CiWQ7")
                        bjj = " ".join([b.text for b in bjj_parts])
                        ull = browser.find_element(By.CLASS_NAME, "duelParticipant").text.split("\n")
                        dt = ull[0].split(" ")[0]
                        Hteam = ull[1].replace(" ", "")
                        Ateam = ull[3].replace(" ", "")
                        round_num = "1"
                        try:
                            round_num = bjj.split("ROUND")[1].strip().split(" ")[0]
                        except:
                            pass

                        dttyl = f"{round_num} {dt} {Hteam} {Ateam}"

                        if len(dttyl.split(" ")) > 0:
                            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\letenok.DWA\Documents\streaks\Fixtures25.accdb;')
                            cursor = conn.cursor()
                            polstriped = dttyl.split(" ")

                            if "Penalty" in polstriped[2]:
                                insert_stmt = f"INSERT INTO {lnk.split()[2]} (Round,Tframe,home,away) VALUES (?,?,?,?)"
                                data = (polstriped[0], polstriped[1], polstriped[3], polstriped[4])
                            else:
                                insert_stmt = f"INSERT INTO {lnk.split()[2]} (Round,Tframe,home,away) VALUES (?,?,?,?)"
                                data = (polstriped[0], polstriped[1], polstriped[2], polstriped[3])

                            try:
                                cursor.execute(insert_stmt, data)
                            except:
                                pass

                            cursor.commit()
                            cursor.close()
                            conn.close()
                    finally:
                        browser.close()
                        browser.switch_to.window(browser.window_handles[0])
            countUps += 1

try:
    run_scraper()
finally:
    browser.quit()  # Always quit browser cleanly at the end
