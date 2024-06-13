from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_to_website():
    # Setup the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get("https://the-internet.herokuapp.com/login")

        # Enter the username
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("tomsmith")

        # Enter the password
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Wait for a few seconds to see the logged in interface
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    login_to_website()
