import requests
from config import API_KEY, BASE_URL

def get_weather(city_name):
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"
    print(f"Request URL: {complete_url}")  # Debug information
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response Data: {data}")  # Debug information
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temp = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]
            
            weather_data = (f"Temperature: {temp}K\n"
                            f"Atmospheric Pressure: {pressure} hPa\n"
                            f"Humidity: {humidity}%\n"
                            f"Description: {description}")
        else:
            weather_data = "City Not Found"
    else:
        print(f"Error: {response.status_code} - {response.text}")  # Debug information
        weather_data = "Error fetching data"
    
    return weather_data
