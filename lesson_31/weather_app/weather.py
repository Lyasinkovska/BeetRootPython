"""
The Weather app

Write a console application which takes as an input a city name and returns current weather in the format of your
choice. For the current task, you can choose any weather API or website or use https://openweathermap.org """
import datetime

import requests

API_KEY = "5427760c69c4dc5e32753401a5b52094"


def get_weather_by_city(city_name: str) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    resp = requests.get(url)
    return resp.json()


def collect_weather_info(result: dict) -> dict:
    return {
        "name": result.get('name'),
        "date": datetime.datetime.fromtimestamp(result.get('dt')).date(),
        "country": result.get('sys').get('country'),
        "min_temp": result.get('main').get('temp_min'),
        "max_temp": result.get('main').get('temp_max'),
        "wind_speed": result.get('wind').get('speed'),
        "description": result.get('weather')[0].get('description'),
        "sunrise": datetime.datetime.fromtimestamp(result.get('sys').get('sunrise')).time(),
        "sunset": datetime.datetime.fromtimestamp(result.get('sys').get('sunset')).time()}


def generate_answer(data: dict) -> str:
    return f'''
The weather in {data.get('name')}, {data.get('country')} today on {data.get('date')}:

temperature: {data.get('min_temp')} ... {data.get('max_temp')} Celcius,
wind speed: {data.get('wind_speed')} m/s
description: {data.get('description')}
sunrise: {data.get('sunrise')}
sunset: {data.get('sunset')}
'''


def find_weather_by_city() -> str:
    city_name = input('Enter city: ')
    try:
        data = collect_weather_info(get_weather_by_city(city_name))
    except TypeError:
        raise Exception("Wrong city name")
    return generate_answer(data)


if __name__ == '__main__':
    print(find_weather_by_city())
