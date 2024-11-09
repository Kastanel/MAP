import requests
from dotenv import dotenv_values
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs.log")
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
weather_api_key = dotenv_values(".env").get("WEATHER_API_KEY")


def API_ENDPOINT(city_name):
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric"


def degrees_to_compass(degrees):
    directions = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]
    degrees = (degrees + 360) % 360
    index = int((degrees + 11.25) // 22.5) % 16
    return directions[index]


city = input("Type in the city name: ")
response = requests.get(API_ENDPOINT(city))

if response.status_code == 200:
    data = response.json()
    weather_status = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    wind_speed = data["wind"]["speed"]
    wind_direction = data["wind"]["deg"]

    logger.info(f"location: {city}")
    logger.info(f"status: {weather_status}")
    logger.info(f"temp: {temp}")
    logger.info(f"feels_like: {feels_like}")
    logger.info(f"wind speed: {wind_speed}")
    logger.info(f"wind direction: {degrees_to_compass(wind_direction)}")
else:
    print("Encountered error when getting weather data!")
