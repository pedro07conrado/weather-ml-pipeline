import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather_data():
    api_key = os.getenv("API_KEY")
    city = os.getenv("WEATHER_CITY", "Curitiba")
    units = os.getenv("WEATHER_UNITS", "metric")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "timestamp": data["dt"]
        }
    except Exception as e:
        print(f"Erro ao buscar dados do clima: {e}")
        return None
