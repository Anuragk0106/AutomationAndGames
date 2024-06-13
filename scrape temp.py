import requests
from bs4 import BeautifulSoup
import time

def get_temperature():
    url = 'https://forecast.weather.gov/MapClick.php?lat=42.9371&lon=-75.6107'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Locate the temperature value on the webpage
        # Note: Update the below selector based on the actual HTML structure
        temperature_div = soup.find(id='current_conditions-summary')
        if temperature_div:
            temperature = temperature_div.find(class_='myforecast-current-lrg').get_text()
            return temperature
        else:
            return "Temperature element not found"
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"

def main():
    while True:
        temperature = get_temperature()
        print(f"Current Temperature: {temperature}")
        time.sleep(60)  # Wait for 1 minute before scraping again

if __name__ == "__main__":
    main()
