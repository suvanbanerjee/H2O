from plyer import notification
import psutil
import time

battery_state = psutil.sensors_battery().power_plugged #Fetch battery state 
battery_level = int(psutil.sensors_battery().percent) # Fetch battery level

global interval
interval = 1 # in hours
interval = interval * 60 * 60 # Convert hours to sec

def main():
    notification.notify(
        title = "Water Intake Reminder", #Change the title or message if required
        message = "Time to drink water!",
        timeout = 10
    )
    time.sleep(interval)
if __name__ == "__main__":
    '''
    battery_state checks if device is pluged in or not. not(battery_state) is to exit if laptop is
    below a critical level (to conserver battery) desktop users can remove this if the want.
    '''
    if battery_state or battery_level < 30:
        exit()
    else:
        while True:
            main()