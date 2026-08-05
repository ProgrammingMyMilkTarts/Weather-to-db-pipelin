
import requests
import datetime as dt
import csv
import os

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "b220f95507eb7d5324d6d87fcd1a7fb5"
CITY = "Potchefstroom"

def kelvin_to_celsius(kelvin):
  return kelvin - 273.15

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
temp_kelvin = response["main"]["temp"]
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(
    response["sys"]["sunrise"] + response["timezone"]
)
sunset_time = dt.datetime.fromtimestamp(
    response["sys"]["sunset"] + response["timezone"]
)

headers = [
    "Timestamp",
    "Temperature (K)",
    "Temperature (C)",
    "Feels Like (C)",
    "Wind Speed (m/s)",
    "Humidity (%)",
    "Description",
    "Sunrise Time",
    "Sunset Time",
]

weather_data = [
    timestamp,
    temp_kelvin,
    temp_celsius,
    feels_like_celsius,
    wind_speed,
    humidity,
    description,
    sunrise_time,
    sunset_time,
]

BASE_DIR = "/home/poppingmybooty20/Desktop/DevWork/WeatherAPIProject/Weather-to-db-pipelin"
file_path = os.path.join(BASE_DIR, "weather_data.csv")

file_exists = os.path.isfile(file_path)

with open(file_path, mode = 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(headers)

    writer.writerow(weather_data)



