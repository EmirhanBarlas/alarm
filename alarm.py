import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)
            break

root = tk.Tk()
root.title("Alarm Uygulaması")

label = tk.Label(root, text="Alarm zamanını girin (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Alarmı Ayarla", command=set_alarm)
button.pack()

root.mainloop()
