from plyer import notification
import time
import psutil
import json
import requests
import time

battery_state = psutil.sensors_battery().power_plugged
battery_level = int(psutil.sensors_battery().percent)
config = json.load(open("config.json"))
age = config["age"]
weight = config["weight"]
height = config["height"]
activity = config["activity"]
lat = config["lat"]
lon = config["lon"]
global interval
generate_time = time.time()
interval = 1.5 * 60 * 60

def Calculate_Intake(age, weight, height, activity):

    temp,humidity = weather(lat, lon)
    intake = 0 # Some Math Required 
    interval = intake / 0.2

def main():
    notification.notify(
        title = "Water Intake Reminder",
        message = "Time to drink water!",
        timeout = 10
    )
    time.sleep(interval)

    if time.time() - generate_time > 86400:
        intake = Calculate_Intake(age, weight, height, activity)
        generate_time = time.time()
        
def weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=relative_humidity_2m&daily=temperature_2m_max".format(lat, lon)
    data = requests.get(url).json()
    humidity = data["current"]["relative_humidity_2m"]
    temp = data["daily"]["temperature_2m_max"][0]
    return humidity, temp

if __name__ == "__main__":
    if not(battery_state) or battery_level < 30:
        exit()
    else:
        while True:
            main()