import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return {"error": f"Couldn't fetch weather for {city}. Try another city."}

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
