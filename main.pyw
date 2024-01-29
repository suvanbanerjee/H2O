from plyer import notification
import time
import psutil

battery_state = psutil.sensors_battery().power_plugged
battery_level = int(psutil.sensors_battery().percent)

if not(battery_state) or battery_level < 30:
    exit()
    
while True:
    notification.notify(
        title="Drink Water",
        message="It's time to drink water",
        timeout=10
    )
    time.sleep(60*120)