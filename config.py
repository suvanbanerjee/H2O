import os.path
import json
from tkinter import messagebox
try:
    import geopy
    import PySimpleGUI as sg
except ModuleNotFoundError:
    messagebox.showerror("Modules Not Found", "Please install required modules\nRun 'pip install -r requirements.txt' in the terminal.")
    exit()
if os.path.exists("config.json"):
    sg.theme("SystemDefaultForReal")
    sg.popup("Config file already exists.\nPlease delete the existing config file to generate a new one.")
    exit()


age=["7-12","13-18","19-30","31-50","51-65","65+"]

sg.theme("SystemDefaultForReal")

layout = [
    [sg.Text("Age")],
    [sg.Combo(age, default_value=age[2], key="age")],
    [sg.Text("Weight (kg)")],
    [sg.InputText(key="weight")],
    [sg.Text("Height (cm)")],
    [sg.InputText(key="height")],
    [sg.Text("Physical Activity")],
    [sg.Combo(["Low","Medium","High"], default_value="Medium", key="activity")],
    [sg.Text("Location")],
    [sg.InputText(key="location")],
    [sg.Button("Generate")]
    ]

window = sg.Window("Water Intake Calculator", layout)
while True:
    try:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Generate":
            age = values["age"]
            weight = values["weight"]
            height = values["height"]
            activity = values["activity"]
            location = values["location"]
            if age == "7-12":
                age = 0.6
            elif age == "13-18":
                age = 1.2
            elif age == "19-30":
                age = 1
            elif age == "31-50":
                age = 1
            elif age == "51-65":
                age = 0.8
            elif age == "65+":
                age = 0.7
            if activity == "Low":
                activity = 0.8
            elif activity == "Medium":
                activity = 1
            elif activity == "High":
                activity = 1.7
            if location == "":
                sg.popup("Please enter a location.")
                continue
            if weight < 0 or height < 0:
                sg.popup("Please enter a valid weight and height.")
                continue
            geolocator = geopy.Nominatim(user_agent="Water Intake Calculator")
            location = geolocator.geocode(location)
            if location == None:
                sg.Popup("Location not found. Please try again.")
                continue
            lat = location.latitude
            lon = location.longitude
            with open("config.json", "w") as f:
                json.dump({"age": age, "weight": weight, "height": height, "activity": activity, "lat": lat, "lon": lon}, f)
            sg.popup("Config file generated.")
            break
    except TypeError:
        sg.popup("Enter a valid number for weight and height.")
