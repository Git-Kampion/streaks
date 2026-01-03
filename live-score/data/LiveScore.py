from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    """Set up Chrome driver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def click_live_matches(driver):
    """Navigate to FlashScore and click on Live button"""
    try:
        # Navigate to FlashScore
        print("Navigating to FlashScore...")
        driver.get("https://www.flashscore.com/")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Wait a moment for dynamic content to load
        time.sleep(3)
        
        # Try to find and click the Live button
        print("Looking for Live button...")
        
        # Multiple possible selectors for the Live button
        live_selectors = [
            "//a[contains(@class, 'live')]",
            "//a[contains(text(), 'Live')]",
            "//div[contains(@class, 'filters')]//a[contains(@class, 'live')]",
            "//a[contains(@href, 'live')]",
            "//button[contains(text(), 'Live')]"
        ]
        
        live_button = None
        for selector in live_selectors:
            try:
                live_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                print(f"Found Live button with selector: {selector}")
                break
            except:
                continue
        
        if live_button:
            # Scroll into view and click
            driver.execute_script("arguments[0].scrollIntoView(true);", live_button)
            time.sleep(1)
            live_button.click()
            print("Successfully clicked on Live button!")
            
            # Wait for live matches to load
            time.sleep(3)
            
            # Get current URL to confirm we're on live page
            current_url = driver.current_url
            print(f"Current URL: {current_url}")
            
            if "live" in current_url.lower():
                print("Successfully navigated to live matches page!")
            else:
                print("May not have reached live matches page - checking content...")
            
            return True
        else:
            print("Could not find Live button with any selector")
            return False
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

def get_live_scores(driver):
    """Extract live match information"""
    try:
        print("\nAttempting to extract live match data...")
        
        # Wait for match elements to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "event__match"))
        )
        
        # Find all live matches
        matches = driver.find_elements(By.CLASS_NAME, "event__match")
        
        print(f"Found {len(matches)} live matches")
        
        for i, match in enumerate(matches[:5]):  # Show first 5 matches
            try:
                # Extract team names and score
                teams = match.find_elements(By.CLASS_NAME, "event__participant")
                score = match.find_elements(By.CLASS_NAME, "event__score")
                
                if len(teams) >= 2 and len(score) >= 1:
                    team1 = teams[0].text
                    team2 = teams[1].text
                    match_score = score[0].text
                    
                    print(f"Match {i+1}: {team1} {match_score} {team2}")
                    
            except Exception as e:
                print(f"Could not extract match {i+1}: {str(e)}")
                continue
                
    except Exception as e:
        print(f"Error extracting scores: {str(e)}")

def main():
    driver = None
    try:
        # Setup driver
        driver = setup_driver()
        
        # Click on Live button
        success = click_live_matches(driver)
        
        if success:
            # Extract and display live scores
            get_live_scores(driver)
            
            # Keep browser open for a while to see results
            print("\nBrowser will close in 10 seconds...")
            time.sleep(10)
        else:
            print("Failed to click Live button")
            
    except Exception as e:
        print(f"Script failed: {str(e)}")
        
    finally:
        if driver:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    main()