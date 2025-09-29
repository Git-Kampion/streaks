from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def get_geckodriver_path():
    """Locate geckodriver executable"""
    possible_paths = [
        'geckodriver.exe',
        os.path.join(os.getcwd(), 'C:\\Users\\letenok.DWA\\Documents\\streaks\\geckodriver-v0.33.0-win64\\geckodriver.exe'),
        r'C:\Program Files\geckodriver\geckodriver.exe'
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Geckodriver not found. Please download and install it.")

def get_firefox_profile_path():
    """Get the default Firefox profile path"""
    app_data = os.getenv('APPDATA')
    profile_path = os.path.join(app_data, 'Mozilla', 'Firefox', 'Profiles')
    profiles = [d for d in os.listdir(profile_path) 
               if d.endswith('.default-release') or d.endswith('.default')]
    if not profiles:
        raise FileNotFoundError("No Firefox profile found")
    return os.path.join(profile_path, profiles[0])

def init_driver():
    """Initialize Firefox with existing profile and maximize window"""
    options = Options()
    options.profile = get_firefox_profile_path()
    
    # Disable automation flags
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    
    # Configure service
    service = Service(executable_path=get_geckodriver_path())
    
    # Kill existing Firefox processes
    os.system('taskkill /f /im firefox.exe')
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()  # Maximize the browser window
    return driver

def accept_cookies(driver):
    """Handle cookie consent if it appears"""
    try:
        cookie_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept') or contains(., 'Got it')]")))
        cookie_btn.click()
        print("Accepted cookies")
    except:
        print("No cookie consent found")

def navigate_to_soccer(driver):
    """Navigate to soccer section on new Betway site"""
    try:
        # Go directly to new soccer URL
        driver.get("https://new.betway.co.za/sports/soccer")
        
        # Alternative navigation through menu
        # menu_btn = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Menu')]")))
        # menu_btn.click()
        # soccer_link = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Soccer')]")))
        # soccer_link.click()
        
        print("Successfully navigated to soccer section")
    except Exception as e:
        print(f"Failed to navigate to soccer: {str(e)}")
        raise

def click_leagues_div(driver):
    """Click on the div containing 'Leagues' span"""
    try:
        # Wait for and click the Leagues div
        
        #leagues_div = driver.find_element(  By.XPATH,"//span[text()='Leagues']")

        wait = WebDriverWait(driver, 30)
       
        leagues_span = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Old Site']")))
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", leagues_span)
        wait = WebDriverWait(driver, 30)
        #leagues_span = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='img-responsive banner-img']")))
        #leagues_span = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'img-responsive banner-img')]")))
      
        # Find the banner element
        banner = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, "img.img-responsive.banner-img")
        )
        
        # Use JavaScript to click (bypasses element visibility issues)
        driver.execute_script("arguments[0].click();", banner)
        print("Banner clicked using JavaScript!")

        league_element = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div.league-filter-box.filtersBox")
        )
        
        # Scroll to element first
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", league_element)
        print("✅ Element scrolled into view")
        
        # Wait a moment for scrolling to complete
        import time
        time.sleep(5)
        
        # Then click
        league_element = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div.league-filter-box.filtersBox")
            )
    
    # Click immediately after finding
        driver.execute_script("arguments[0].click();", league_element)
        # Scroll into view and click using JavaScript
        #driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", leagues_span)
        print("Successfully clicked on Leagues div")
        return True
    except Exception as e:
        print(f"Failed to click Leagues div: {str(e)}")
        return False

def main():
    driver = None
    try:
        print("Initializing browser...")
        driver = init_driver()
        
        # Navigate to new Betway site
        navigate_to_soccer(driver)
        accept_cookies(driver)
        
        # Wait for content to load
        '''
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'events-container')]")))
        print("Page loaded successfully")
        '''
        
        # Click on Leagues div
        click_leagues_div(driver)
        
        # Keep browser open for inspection
        input("Press Enter to close browser...")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        if driver:
            driver.save_screenshot("error.png")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()