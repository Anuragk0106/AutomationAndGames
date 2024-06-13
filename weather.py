import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

def main():
    api_key = "9d4729b4a563e2e21f78d6351d979d20"  # Replace with your actual API key
    city_name = input("Enter city name: ")
    temperature = get_weather(city_name, api_key)
    if temperature is not None:
        print(f"The current temperature in {city_name} is {temperature}°C")
    else:
        print(f"Could not retrieve weather data for {city_name}")

if __name__ == "__main__":
    main()
