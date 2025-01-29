

from constants.Weather import Weather
import time
import requests

def get_weather():


    url=f"https://api.openweathermap.org/data/2.5/weather?q={Weather.CITY}&appid={Weather.API_KEY}"

    try:
        response=requests.get(url)
        data =response.json()
        weather_data={
        "timestump":time.strftime("%Y.%m.%d %H:%M:%S"),
        "city" :data ["name"],
        "pressure" :data["main"]["pressure"],
        "tempmimn" : data["main"]["temp_min"],
        "temp"  :data["main"]["temp"],
        "wind"  :data["wind"]["speed"],
        "feels_like"  :data["main"]["feels_like"],
        "weather_description":data["weather"][0]["description"],
        }
        return weather_data
        # print(weather_data)
    except Exception as error:

        print(error)
resoult =get_weather()
