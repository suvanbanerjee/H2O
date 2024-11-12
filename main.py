from plyer import notification
import time
import psutil
import json
import requests

json_path = "./config.json" #Replace this with the path to your config.json file

def calculate_intake(age, weight, height, activity, lat, lon):
    humidity, temp = weather(lat, lon)

    base_intake = weight * 0.033  # L/day
    base_caloric_expenditure = 10 * weight + 6.25 * height - 5 * age  # Miffin-St Equation (Kcal/day)

    if activity == "Low":
        activity_factor = 1.2
    elif activity == "Medium":
        activity_factor = 1.55
    elif activity == "High":
        activity_factor = 1.9
    caloric_expenditure = base_caloric_expenditure * activity_factor
    if base_intake < caloric_expenditure / 1000:
        base_intake = caloric_expenditure / 1000
    intake = base_intake
    add_intake = ((0.033*(temp-31)+0.0025*(temp-31)**2+0.8148)*(1+0.02*(humidity-50)*0.01))/30
    intake += add_intake
    no_of_glasses = intake / 0.25 # 1 glass = 250 ml
    interval = 57600 / no_of_glasses # 16 hours in a day (57600 seconds)

    print("Daily Intake (Ltr): ", intake)
    print("Interval (Sec): ", interval)

    return interval

def main():
    notification.notify(
        title="Water Intake Reminder",
        message="Time to drink water!",
        timeout=5
    )

def weather(lat, lon):
    return 50, 20
    url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=relative_humidity_2m&daily=temperature_2m_max".format(lat, lon)
    try:
        data = requests.get(url).json()
        humidity = data["current"]["relative_humidity_2m"]
        temp = data["daily"]["temperature_2m_max"][0]
        return humidity*100, temp
    except Exception as e:
        print("Error fetching weather data:", e)
        return 0, 0

if __name__ == "__main__":
    config = json.load(open(json_path))
    age = config["age"]
    weight = config["weight"]
    height = config["height"]
    activity = config["activity"]
    lat = config["lat"]
    lon = config["lon"]

    battery_state = psutil.sensors_battery().power_plugged
    battery_level = int(psutil.sensors_battery().percent)

    # if not battery_state or battery_level < 30:
    #     exit()
    
    while True:
        main()
        time_interval = calculate_intake(age, weight, height, activity, lat, lon)
        time.sleep(time_interval)