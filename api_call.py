import requests
from constants import *


def get_forecast(city: str, lang: str = 'en', units: str = 'metric', api_key: str = API_KEY) -> dict:
    """Requests 24-hours(3 hour step) weather forecast from https://openweathermap.org"""

    url = f"http://api.openweathermap.org/data/2.5/forecast?appid={api_key}&lang={lang}&q={city}&units={units}&cnt=8"
    response = requests.get(url)
    forecast_json = response.json()

    return forecast_json


def get_sunrise_sunset(lat: float, lon: float, date: str) -> dict:
    """Requests sunrise, sunset and other miscellaneous data from https://sunrisesunset.io"""

    url = f"https://api.sunrisesunset.io/json?lat={lat}&lng={lon}&date={date}"
    response = requests.get(url)
    sun_time_json = response.json()

    return sun_time_json
