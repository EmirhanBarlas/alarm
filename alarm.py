import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    alarm_datetime = datetime.datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
    while datetime.datetime.now() < alarm_datetime:
        pass
    winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)

root = tk.Tk()
root.title("Alarm Uygulaması")

label = tk.Label(root, text="Alarm zamanını girin (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Alarmı Ayarla", command=set_alarm)
button.pack()

root.mainloop()
