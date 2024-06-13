import requests
from bs4 import BeautifulSoup
import time

def get_temperature():
    url = 'https://www.accuweather.com/en/in/kudwari/2991388/current-weather/2991388'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Adding headers to mimic a regular browser request. This helps bypass restrictions that block automated scraping.
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Locate the temperature value on the webpage
        # Note: Update the below selector based on the actual HTML structure
        temperature_div = soup.find(class_='current-weather-info')
        if temperature_div:
            temperature = temperature_div.find(class_='display-temp').get_text()
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
