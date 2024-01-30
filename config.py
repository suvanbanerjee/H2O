import PySimpleGUI as sg
import os.path
import json
import python_weather

age=["7-12","13-18","19-30","31-50","51-65","65+"]

layout = [
    [sg.Text("Age")],
    [sg.Combo(age, default_value=age[0], key="age")],
    [sg.Text("Weight (kg)")],
    [sg.InputText(key="weight")],
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
    