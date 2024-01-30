import PySimpleGUI as sg
import os.path
import json
import geopy

age=["7-12","13-18","19-30","31-50","51-65","65+"]

sg.theme("default")

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
            age = 1
        elif age == "13-18":
            age = 2
        elif age == "19-30":
            age = 3
        elif age == "31-50":
            age = 4
        elif age == "51-65":
            age = 5
        elif age == "65+":
            age = 6
        if activity == "Low":
            activity = 1
        elif activity == "Medium":
            activity = 2
        elif activity == "High":
            activity = 3
        if location == "":
            sg.popup("Please enter a location.")
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
        break