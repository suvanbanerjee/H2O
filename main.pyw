from plyer import notification
import time
import psutil
import json
import requests

battery_state = psutil.sensors_battery().power_plugged
battery_level = int(psutil.sensors_battery().percent)
config = json.load(open("config.json"))

def Calculate_Intake(age, weight, height, activity):
    if age == 1:
        age = 0.5
    elif age == 2:
        age = 0.6
    elif age == 3:
        age = 0.7
    elif age == 4:
        age = 0.8
    elif age == 5:
        age = 0.9
    elif age == 6:
        age = 1
    if activity == 1:
        activity = 0.5
    elif activity == 2:
        activity = 0.6
    elif activity == 3:
        activity = 0.7
    return (weight * 0.033) + (height * 0.023) + (age * 0.033) + (activity * 0.033)

def main(interval):
    notification.notify(
        title = "Water Intake Reminder",
        message = "Time to drink water!",
        timeout = 10
    )
    time.sleep(interval)
    
def weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=relative_humidity_2m&daily=temperature_2m_max".format(lat, lon)
    data = requests.get(url).json()
    print(data)
    # temp = data["main"]["temp"]
    # return temp

if __name__ == "__main__":
    if not(battery_state) or battery_level < 30:
        exit()
    else:
        # main()
        weather(28.6273928, 77.1716954)