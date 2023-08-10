import time
from tkinter import Tk
from tkinter import Label

root = Tk()
root.title("DigitalClock")

def present_time():
    display_time = time.strftime("%I:%M:%S")
    digit_Clock.config(text=display_time)
    digit_Clock.after(200,present_time)

digit_Clock = Label(root, font=("arial", 100), bg="green", fg="white")

digit_Clock.pack()

present_time()

root.mainloop()