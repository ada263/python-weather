from services.weather_service import get_weather
from services.excel_service import save_to_excel
import time


def start():
    while True:

        weather = get_weather()
        save_to_excel(weather)
        print("zapisane dane")
        time.sleep(30)
def 
start()