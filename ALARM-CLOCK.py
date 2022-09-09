# importing the necessary modules 


from tkinter import *
import winsound

import datetime
import time

# setting up the ain screen
root = Tk()
root.title('my Alarm clock')
root.geometry('270x300')
root.resizable(False,False)


# creating and placing all the components of the window
Label(root, text = "when do you want to wake up ?\n(Enter in 24-hour format)", font = ("Cosmic Sans MS", 13), wraplength=root. winfo_width()).place( x= 0, y = 0)

Label(root, text = 'Hour', font = ("Book Antiqua", 11), wraplength = root.winfo_width()).place(x = 50, y = 70)

Label(root, text = 'Minute', font = ("Book Antiqua", 11), wraplength= root. winfo_width()).place( x =100, y = 70)

Label(root, text = 'Second', font = ("Book Antiqua", 11), wraplength= root. winfo_width()).place( x = 160, y = 70)

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
minutes =  ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] 
seconds =  ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']

for x in range(10, 24):
    hours.append(x)

for x in range(10, 61):
    minutes.append(x)
    seconds.append(x)

hours = StringVar(root)
hours.set(hours[0])
OptionMenu(root, hours, *hours). place(x = 40, y = 100)

minutes = StringVar(root)
minutes.set(minutes[0])
OptionMenu(root, minutes, *minutes). place(x = 100, y = 100)

seconds = StringVar(root)
seconds.set(seconds[0])
OptionMenu(root, seconds, *seconds).place(x =160, y = 100)

submit_btn = Button(root, text = 'Submit', bg = "CadetBlue4", command = lambda: alarm_clock(hours.get()[:2], seconds.get()[:2])) 
submit_btn.place(x = 100, y = 150)

def alarm_clock(hours,minutes, seconds):
    while True:
        alarm_time = f"{hours} : {minutes} : {seconds}"

        # Getting current time by using. striftime() method of the datetime modules datetime files now a function
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if  current_time == alarm_time:
            time.sleep(1)
            print("Time to wake up, my people! ")
            # playing a sound when current  time is the same as the alarm time
            # The wav file  should be in the same directory as the python code
            winsound.PlaySound('C:/Users/hp/Desktop/mixkit-battleship-alarm-1001.wav', winsound.SND_ASYNC)
            





