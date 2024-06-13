from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Set Chrome options
    chrome_options = webdriver.ChromeOptions()
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
                                             
    # Navigate to the weather website
    driver.get("https://www.ventusky.com")
    
    # Wait for the page to load
    time.sleep(50) 
    
    # Find the search input box and type a city (e.g., New York)
    search_box = driver.find_element(By.ID, "search-input")
    search_box.send_keys("New York")
    
    # Press Enter to search for the city's weather
    search_box.send_keys(Keys.ENTER)
    
    # Wait for the weather information to load
    time.sleep(5)
    
    # You can add more actions here if needed, like scraping weather information
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
